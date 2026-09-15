#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
校验 _data/blog_stats.json 是否与 _posts/ 当前内容一致

用途：CI 兜底。_data/blog_stats.json 是离线生成的快照，本地 pre-commit 钩子负责自动更新；
     但钩子位于 .git/hooks/（不随仓库分发），换机器、重装或 git commit --no-verify 时会漏跑，
     这里再校验一次，避免统计页静默停留在旧数据上。

用法：
    python dev/check_stats_fresh.py

退出码：0 = 一致；1 = 已过期（打印差异字段与修复方法）
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATS = ROOT / "_data" / "blog_stats.json"
GENERATOR = ROOT / "dev" / "gen_blog_stats.py"


def load(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    # generated_at 每次生成都会变，不参与比对；其余字段全部逐项比较
    if isinstance(data.get("meta"), dict):
        data["meta"].pop("generated_at", None)
    return data


def describe(committed, fresh):
    for key in sorted(set(committed) | set(fresh)):
        old, new = committed.get(key), fresh.get(key)
        if old == new:
            continue
        if isinstance(old, dict) and isinstance(new, dict):
            print(f"  字段 {key}:")
            for k in sorted(set(old) | set(new)):
                if old.get(k) != new.get(k):
                    print(f"    {k}: {old.get(k)!r} → {new.get(k)!r}")
        elif isinstance(old, list) and isinstance(new, list):
            print(f"  字段 {key}: 条目数 {len(old)} → {len(new)}")
        else:
            print(f"  字段 {key}: {old!r} → {new!r}")


def main():
    if not STATS.exists():
        print(f"::error::{STATS.relative_to(ROOT)} 不存在，统计页将拿不到数据")
        return 1
    if not GENERATOR.exists():
        print(f"::error::{GENERATOR.relative_to(ROOT)} 不存在，无法校验")
        return 1

    committed = load(STATS)

    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "blog_stats.json"
        proc = subprocess.run(
            [sys.executable, str(GENERATOR), "--out", str(out)],
            cwd=str(ROOT), capture_output=True, text=True)
        sys.stdout.write(proc.stdout)
        if proc.stderr:
            sys.stderr.write(proc.stderr)
        if proc.returncode != 0:
            print("::error::统计数据生成脚本执行失败，无法完成校验")
            return 1
        fresh = load(out)

    if committed == fresh:
        print("OK: _data/blog_stats.json 与 _posts/ 一致")
        return 0

    print("::error::统计数据已过期——_posts/ 有变更，但 _data/blog_stats.json 未同步更新")
    print("修复：在本地执行 `python dev/gen_blog_stats.py`，然后提交 _data/blog_stats.json")
    describe(committed, fresh)
    return 1


if __name__ == "__main__":
    sys.exit(main())
