#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
蒲荣龙博客 — 统计数据生成脚本

用法：
    python dev/gen_blog_stats.py                # 生成 _data/blog_stats.json
    python dev/gen_blog_stats.py --check-links  # 额外检测外链死链（联网，较慢）

字数口径（口径⑤，全站唯一口径）：
    汉字按字 + 英文按词 + 数字按字符
    排除：围栏代码块、行内代码、Markdown 标记、链接 URL、图片、HTML 标签、标点、空白

本脚本位于 dev/，已在 _config.yml 的 exclude 列表中，不参与 Jekyll 构建。
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from itertools import combinations
from pathlib import Path
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "_posts"
OUT_FILE = ROOT / "_data" / "blog_stats.json"
SITE_HOSTS = {"puronglong.com", "www.puronglong.com"}

# ---------------------------------------------------------------- 正则

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
FILE_RE = re.compile(r"^(\d{4})-(\d{1,2})-(\d{1,2})-(.+)\.md$")

CJK_CLASS = r"\u4e00-\u9fff\u3400-\u4dbf"
CJK_RE = re.compile(f"[{CJK_CLASS}]")
LATIN_RE = re.compile(r"[A-Za-z]+")
DIGIT_RE = re.compile(r"\d")

CODE_BLOCK_RE = re.compile(r"```[\s\S]*?```")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
IMG_MD_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
LINK_MD_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
HTML_TAG_RE = re.compile(r"<[^>]+>")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s*", re.M)

# 外链提取（覆盖四种写法）
EXT_INLINE_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
EXT_REFDEF_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(https?://\S+)", re.M)
EXT_A_HREF_RE = re.compile(r"<a\s[^>]*href=[\"'](https?://[^\"']+)[\"']", re.I)
EXT_BARE_RE = re.compile(r"(?<![(\[\"'=])(https?://[^\s)\]\"'<>]+)")

# 图片提取
IMG_EXT_MD_RE = re.compile(r"!\[[^\]]*\]\((https?://[^)\s]+)\)")
IMG_EXT_HTML_RE = re.compile(r"<img\s[^>]*src=[\"'](https?://[^\"']+)[\"']", re.I)
IMG_ANY_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)|<img\s[^>]*src=[\"'][^\"']+[\"']", re.I)

# 站内链接：先抓 ]( 之后到空白的内容，再按 .html 边界修剪（兼容 URL 内的括号）
INTERNAL_TARGET_RE = re.compile(r"\]\(\s*([^\s]*)")


def extract_internal_targets(body):
    out = []
    for m in INTERNAL_TARGET_RE.finditer(body):
        u = m.group(1)
        if not u or not (u.startswith("/") or "puronglong.com" in u):
            continue
        u = u[: u.index(".html") + 5] if ".html" in u else u.split(")")[0]
        u = u.split("#")[0].rstrip("/")
        if len(u) > 1:
            out.append(u)
    return out

# 单篇字数直方图分箱
DIST_BINS = [(0, 500), (500, 1000), (1000, 1500), (1500, 2000),
             (2000, 3000), (3000, 5000), (5000, 10000), (10000, 10**9)]
DIST_LABELS = ["0-500", "500-1000", "1000-1500", "1500-2000",
               "2000-3000", "3000-5000", "5000-10000", "10000+"]

WEEKDAY_CN = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


# ---------------------------------------------------------------- 解析

# Jekyll URL 生成规则（已用 _site/sitemap.xml 全量校验 183/183 一致）：
#   slug 走 pretty 模式——[^alnum._~!$&'()+,;=@]+ 替换为 "-"
#   再做 URI escape，保留 URI::DEFAULT_PARSER 的安全字符集
SLUG_KEEP = set("._~!$&'()+,;=@-")
SLUG_SAFE = "/!~*'();:@&=+$,[]"


def jekyll_slug(name):
    return re.sub(r"-+", "-", "".join(
        c if c.isalnum() or c in SLUG_KEEP else "-" for c in name)).strip("-")


def post_url(y, mo, d, slug):
    return f"/{y:04d}/{mo:02d}/{d:02d}/{quote(jekyll_slug(slug), safe=SLUG_SAFE)}.html"


def split_front_matter(raw):
    m = FM_RE.match(raw)
    if not m:
        return {}, raw
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, raw[m.end():]


def parse_tags(raw):
    """兼容 `tags: [生活, 读书]` 与 `tags: 生活,读书` 两种写法"""
    if not raw:
        return []
    t = raw.strip()
    if t.startswith("["):
        t = t.strip("[]")
    return [x.strip().strip("\"'") for x in t.split(",") if x.strip()]


def clean_for_count(body):
    """剥掉代码块/Markdown 标记/URL/标签，只留可读正文"""
    t = CODE_BLOCK_RE.sub(" ", body)
    t = INLINE_CODE_RE.sub(" ", t)
    t = IMG_MD_RE.sub(" ", t)
    t = LINK_MD_RE.sub(r"\1", t)
    t = HTML_TAG_RE.sub(" ", t)
    t = HEADING_RE.sub(" ", t)
    return t


def count_words(body):
    """口径⑤：汉字按字 + 英文按词 + 数字按字符"""
    t = clean_for_count(body)
    han = len(CJK_RE.findall(t))
    latin = len(LATIN_RE.findall(t))
    digits = len(DIGIT_RE.findall(t))
    return han + latin + digits, han, latin, digits


def count_code_chars(body):
    """围栏代码块内的非空白字符数"""
    return sum(len(re.sub(r"\s", "", m)) - 6 for m in CODE_BLOCK_RE.findall(body))


def count_images(body):
    """正文图片引用数（排除代码块内的示例代码）"""
    t = CODE_BLOCK_RE.sub(" ", body)
    return len(re.findall(r"!\[[^\]]*\]\(", t)) + len(re.findall(r"<img\s", t, re.I))


def load_posts():
    posts = []
    for path in sorted(POSTS_DIR.glob("*.md")):
        m = FILE_RE.match(path.name)
        if not m:
            print(f"  [跳过] 文件名不符合 yyyy-m-d-slug.md: {path.name}", file=sys.stderr)
            continue
        y, mo, d, slug = int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4)
        fm, body = split_front_matter(path.read_text(encoding="utf-8"))
        words, han, latin, digits = count_words(body)
        posts.append({
            "file": path.name,
            "date": f"{y:04d}-{mo:02d}-{d:02d}",
            "dt": datetime(y, mo, d),
            "title": fm.get("title", slug),
            "url": post_url(y, mo, d, slug),
            "tags": parse_tags(fm.get("tags")),
            "words": words,
            "han": han,
            "latin": latin,
            "digits": digits,
            "code_chars": count_code_chars(body),
            "images": count_images(body),
            "body": body,
        })
    posts.sort(key=lambda p: p["dt"])
    return posts


# ---------------------------------------------------------------- 外链

def extract_ext_links(body):
    """返回正文外链 URL 列表（排除站内、排除代码块内的示例链接）"""
    t = CODE_BLOCK_RE.sub(" ", body)
    urls = []
    urls += EXT_INLINE_RE.findall(t)
    urls += EXT_REFDEF_RE.findall(t)
    urls += EXT_A_HREF_RE.findall(t)
    imgs = set(IMG_EXT_MD_RE.findall(t)) | set(IMG_EXT_HTML_RE.findall(t))
    known = set(urls) | imgs
    for u in EXT_BARE_RE.findall(t):
        if u not in known and u not in imgs:
            urls.append(u)
    out = []
    for u in urls:
        if u in imgs:
            continue
        host = urlparse(u).netloc.lower()
        if not host or host in SITE_HOSTS:
            continue
        out.append((u, host))
    return out


def collect_links(posts):
    link_count = Counter()
    uniq_by_host = defaultdict(set)
    posts_by_host = defaultdict(set)
    img_count = Counter()
    img_uniq = defaultdict(set)
    internal_inbound = defaultdict(set)
    all_ext_urls = set()

    for p in posts:
        body_nocode = CODE_BLOCK_RE.sub(" ", p["body"])

        for u in set(IMG_EXT_MD_RE.findall(body_nocode)) | set(IMG_EXT_HTML_RE.findall(body_nocode)):
            host = urlparse(u).netloc.lower()
            img_count[host] += 1
            img_uniq[host].add(u)

        for u, host in extract_ext_links(p["body"]):
            link_count[host] += 1
            uniq_by_host[host].add(u)
            posts_by_host[host].add(p["file"])
            all_ext_urls.add(u)

        for tgt in extract_internal_targets(body_nocode):
            internal_inbound[tgt].add(p["file"])

    by_url = {p["url"].rstrip("/"): p for p in posts}
    by_slug = {}
    for p in posts:
        by_slug[p["url"].split("/")[-1].replace(".html", "")] = p

    internal = []
    for tgt, srcs in internal_inbound.items():
        tgt_slug = tgt.split("/")[-1].replace(".html", "")
        target = by_url.get(tgt) or by_slug.get(tgt_slug)
        internal.append({
            "target": target["title"] if target else tgt,
            "url": target["url"] if target else tgt,
            "resolved": target is not None,
            "count": len(srcs),
        })
    internal.sort(key=lambda x: (-x["count"], x["target"]))

    return {
        "ext_links": sorted(
            ({"host": h, "count": c, "unique": len(uniq_by_host[h]),
              "posts": len(posts_by_host[h])} for h, c in link_count.items()),
            key=lambda x: (-x["count"], x["host"])),
        "ext_total": sum(link_count.values()),
        "ext_unique": len(all_ext_urls),
        "ext_domains": len(link_count),
        "image_hosts": sorted(
            ({"host": h, "count": c, "unique": len(img_uniq[h])} for h, c in img_count.items()),
            key=lambda x: (-x["count"], x["host"])),
        "image_ext_total": sum(img_count.values()),
        "image_ext_unique": len(set().union(*img_uniq.values())) if img_uniq else 0,
        "internal_links": internal,
        "internal_posts": len({s for srcs in internal_inbound.values() for s in srcs}),
        "all_ext_urls": sorted(all_ext_urls),
    }


# ---------------------------------------------------------------- 死链

def check_links(urls, timeout=8, workers=12):
    import urllib.request
    from concurrent.futures import ThreadPoolExecutor

    def probe(u):
        for method in ("HEAD", "GET"):
            try:
                req = urllib.request.Request(
                    u, method=method,
                    headers={"User-Agent": "Mozilla/5.0 (blog link checker)"})
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    return u, r.status
            except Exception as e:
                code = getattr(e, "code", None)
                if code:
                    return u, code
        return u, 0

    with ThreadPoolExecutor(max_workers=workers) as ex:
        results = list(ex.map(probe, urls))
    return [{"url": u, "status": s} for u, s in results]


# ---------------------------------------------------------------- 统计

def build_stats(posts, link_data):
    total_words = sum(p["words"] for p in posts)
    total = len(posts)
    first, last = posts[0], posts[-1]
    longest = max(posts, key=lambda p: p["words"])
    shortest = min(posts, key=lambda p: p["words"])
    span_days = (last["dt"] - first["dt"]).days
    months = (last["dt"].year - first["dt"].year) * 12 + (last["dt"].month - first["dt"].month) + 1

    # 最长断更间隔
    gaps = [(posts[i]["dt"] - posts[i - 1]["dt"]).days for i in range(1, len(posts))]
    max_gap = max(gaps) if gaps else 0
    gap_idx = gaps.index(max_gap) + 1 if gaps else 0

    # 年度
    by_year = defaultdict(lambda: {"posts": 0, "words": 0, "images": 0, "code": 0})
    for p in posts:
        y = p["dt"].year
        by_year[y]["posts"] += 1
        by_year[y]["words"] += p["words"]
        by_year[y]["images"] += p["images"]
        by_year[y]["code"] += p["code_chars"]
    years = sorted(by_year)
    years_full = list(range(years[0], years[-1] + 1))
    words_by_year = [{
        "year": y,
        "posts": by_year[y]["posts"] if y in by_year else 0,
        "words": by_year[y]["words"] if y in by_year else 0,
        "avg": round(by_year[y]["words"] / by_year[y]["posts"])
               if y in by_year and by_year[y]["posts"] else 0,
        "images": by_year[y]["images"] if y in by_year else 0,
        "img_per_post": round(by_year[y]["images"] / by_year[y]["posts"], 1)
                        if y in by_year and by_year[y]["posts"] else 0,
    } for y in years_full]

    # 累计字数曲线
    cum, cumulative = 0, []
    for p in posts:
        cum += p["words"]
        cumulative.append({"date": p["date"], "words": p["words"], "cum": cum})

    # 月度 / 星期
    by_month = Counter(p["dt"].month for p in posts)
    by_weekday = Counter(p["dt"].weekday() for p in posts)

    # 热力图（值用当日字数，"每天 1 篇"没有层次感）
    heat_words, heat_posts = Counter(), Counter()
    for p in posts:
        heat_words[p["date"]] += p["words"]
        heat_posts[p["date"]] += 1

    # 标签
    tag_count, tag_words = Counter(), Counter()
    for p in posts:
        for t in p["tags"]:
            tag_count[t] += 1
            tag_words[t] += p["words"]
    tags = [{"name": t, "count": c, "words": tag_words[t],
             "avg": round(tag_words[t] / c)}
            for t, c in sorted(tag_count.items(), key=lambda x: (-x[1], x[0]))]
    tag_names = [t["name"] for t in tags]

    # 标签 × 年份
    ty = defaultdict(Counter)
    for p in posts:
        for t in p["tags"]:
            ty[p["dt"].year][t] += 1
    tag_year = [{"year": y, "counts": {t: ty[y].get(t, 0) for t in tag_names}}
                for y in years_full]

    # 标签共现
    pair = Counter()
    for p in posts:
        for a, b in combinations(sorted(p["tags"]), 2):
            pair[f"{a} + {b}"] += 1
    tag_pairs = [{"pair": k, "count": v}
                 for k, v in sorted(pair.items(), key=lambda x: (-x[1], x[0])) if v >= 2]

    # 单篇字数分布
    dist = [0] * len(DIST_BINS)
    for p in posts:
        for i, (lo, hi) in enumerate(DIST_BINS):
            if lo <= p["words"] < hi:
                dist[i] += 1
                break
    word_dist = [{"bucket": DIST_LABELS[i], "count": c, "lo": DIST_BINS[i][0]}
                 for i, c in enumerate(dist)]

    # 代码占比
    code_chars = sum(p["code_chars"] for p in posts)
    code_ratio = round(code_chars / (code_chars + total_words) * 100, 1) if total_words else 0
    tech_posts = [p for p in posts if "技术" in p["tags"]]
    tech_code = sum(p["code_chars"] for p in tech_posts)
    tech_words = sum(p["words"] for p in tech_posts)

    # 里程碑
    milestones = []
    for n in (1, 50, 100, 150):
        if n <= total:
            p = posts[n - 1]
            milestones.append({"label": f"第 {n} 篇", "date": p["date"],
                               "title": p["title"], "url": p["url"],
                               "note": f"累计 {sum(x['words'] for x in posts[:n]):,} 字"})
    running = 0
    thresholds = [50000, 100000, 200000]
    for idx, p in enumerate(posts):
        running += p["words"]
        for th in list(thresholds):
            if running >= th:
                milestones.append({"label": f"累计 {th // 10000} 万字", "date": p["date"],
                                   "title": p["title"], "url": p["url"],
                                   "note": f"第 {idx + 1} 篇"})
                thresholds.remove(th)
    milestones.sort(key=lambda m: m["date"])

    return {
        "meta": {
            "generated_at": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M"),
            "word_count_rule": "汉字按字 + 英文按词 + 数字按字符，排除代码块、Markdown 标记与标点",
            "source": "_posts/ 目录（%d 篇）" % total,
        },
        "overview": {
            "total_posts": total,
            "total_words": total_words,
            "total_words_display": f"{total_words:,}",
            "total_words_wan": f"{total_words / 10000:.1f}",
            "avg_words_display": f"{round(total_words / total):,}" if total else "0",
            "total_tags": len(tags),
            "first_post": {"date": first["date"], "title": first["title"], "url": first["url"]},
            "last_post": {"date": last["date"], "title": last["title"], "url": last["url"]},
            "longest_post": {"date": longest["date"], "title": longest["title"],
                             "url": longest["url"], "words": longest["words"],
                             "words_display": f"{longest['words']:,}",
                             "tags": longest["tags"]},
            "shortest_post": {"date": shortest["date"], "title": shortest["title"],
                              "url": shortest["url"], "words": shortest["words"],
                              "words_display": f"{shortest['words']:,}",
                              "tags": shortest["tags"]},
            "span_days": span_days,
            "span_years": round(span_days / 365.25, 1),
            "avg_words": round(total_words / total) if total else 0,
            "total_images": sum(p["images"] for p in posts),
            "ext_total": link_data["ext_total"],
            "ext_unique": link_data["ext_unique"],
            "ext_domains": link_data["ext_domains"],
            "posts_per_month": round(total / months, 2) if months else 0,
            "max_gap_days": max_gap,
            "max_gap_after": posts[gap_idx - 1]["date"] if gap_idx else "",
            "max_gap_before": posts[gap_idx]["date"] if gap_idx else "",
            "han": sum(p["han"] for p in posts),
            "latin": sum(p["latin"] for p in posts),
            "digits": sum(p["digits"] for p in posts),
        },
        "words_by_year": words_by_year,
        "cumulative": cumulative,
        "posts_by_month": [{"month": m, "count": by_month.get(m, 0)} for m in range(1, 13)],
        "posts_by_weekday": [{"day": WEEKDAY_CN[i], "count": by_weekday.get(i, 0)}
                             for i in range(7)],
        "heatmap": [[d, heat_words[d], heat_posts[d]] for d in sorted(heat_words)],
        "milestones": milestones,
        "tags": tags,
        "tag_year": tag_year,
        "tag_pairs": tag_pairs,
        "word_dist": word_dist,
        "code": {
            "code_chars": code_chars,
            "text_chars": total_words,
            "ratio": code_ratio,
            "tech_posts": len(tech_posts),
            "tech_ratio": round(tech_code / (tech_code + tech_words) * 100, 1)
                          if (tech_code + tech_words) else 0,
        },
        "ext_links": link_data["ext_links"],
        "image_hosts": link_data["image_hosts"],
        "image_ext_total": link_data["image_ext_total"],
        "image_ext_unique": link_data["image_ext_unique"],
        "internal_links": link_data["internal_links"],
        "internal_posts": link_data["internal_posts"],
    }


def verify_urls(posts):
    """与 _site/sitemap.xml 交叉校验 URL 生成规则（需先构建过一次）"""
    sm_path = ROOT / "_site" / "sitemap.xml"
    if not sm_path.exists():
        print("  [校验] 未找到 _site/sitemap.xml，跳过 URL 校验")
        return
    import html as _html
    txt = sm_path.read_text(encoding="utf-8")
    sm = {_html.unescape(re.sub(r"^https?://[^/]+", "", u))
          for u in re.findall(r"<loc>([^<]+)</loc>", txt)
          if re.search(r"/\d{4}/\d{2}/\d{2}/", u)}
    mine = {p["url"] for p in posts}
    miss, extra = sm - mine, mine - sm
    if not miss and not extra:
        print(f"  [校验] URL 与 sitemap 完全一致（{len(sm)} 条）")
    else:
        print(f"  [校验] 提示：sitemap 独有 {len(miss)} 条，本地独有 {len(extra)} 条"
              "（若刚新增/删除文章属正常）")
        for u in sorted(miss)[:3]:
            print("        sitemap:", u)
        for u in sorted(extra)[:3]:
            print("        本地   :", u)


def main():
    ap = argparse.ArgumentParser(description="生成博客统计数据")
    ap.add_argument("--check-links", action="store_true",
                    help="额外检测外链死链（联网，较慢）")
    ap.add_argument("--out", default=str(OUT_FILE), help="输出路径")
    args = ap.parse_args()

    print("读取 _posts/ ...")
    posts = load_posts()
    if not posts:
        print("没有找到文章，退出", file=sys.stderr)
        return 1
    print(f"  解析 {len(posts)} 篇")

    verify_urls(posts)

    link_data = collect_links(posts)
    stats = build_stats(posts, link_data)

    if args.check_links:
        print(f"检测 {len(link_data['all_ext_urls'])} 个外链（联网）...")
        stats["link_check"] = check_links(link_data["all_ext_urls"])
        dead = [r for r in stats["link_check"] if not (200 <= r["status"] < 400)]
        stats["dead_links"] = dead
        print(f"  失效 {len(dead)} 个")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    # 转义 "</"，避免标题等字段里出现 </script> 时提前闭合页面内联脚本
    payload = json.dumps(stats, ensure_ascii=False, indent=2).replace("</", "<\\/")
    out.write_text(payload, encoding="utf-8")

    o = stats["overview"]
    print(f"\n已写入 {out}")
    print(f"  文章 {o['total_posts']} 篇 · {o['total_words']:,} 字 · 篇均 {o['avg_words']:,}")
    print(f"  标签 {o['total_tags']} 个 · 图片 {o['total_images']} 张 · 外链 {o['ext_total']} 条"
          f"（{o['ext_domains']} 个域名）")
    print(f"  跨度 {o['span_years']} 年 · 更新频率 {o['posts_per_month']} 篇/月")
    return 0


if __name__ == "__main__":
    sys.exit(main())
