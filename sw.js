/* Service Worker - 提升重复访问速度（保守策略） */
var CACHE = 'puronglong-v4';
var CORE = [
  '/',
  '/index.html',
  '/assets/css/bundle.min.css',
  '/assets/js/index.min.js',
  '/assets/js/cursor_effects.js',
  '/assets/fonts/Merriweather-Black.woff2',
  '/assets/fonts/Merriweather-Light.woff2'
];

function okRes(r) {
  return (r && r.status === 200) ? r : undefined;
}

function fallbackResponse() {
  return new Response('', { status: 503, statusText: 'Service Unavailable' });
}

self.addEventListener('install', function (e) {
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(function (c) {
    return c.addAll(CORE.map(function (u) { return new Request(u, { cache: 'reload' }); }));
  }).catch(function () {}));
});

self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.map(function (k) {
      if (k !== CACHE) return caches.delete(k);
    }));
  }).then(function () { return self.clients.claim(); }));
});

self.addEventListener('message', function (e) {
  if (e.data && e.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;
  var url = new URL(req.url);

  // 页面导航：network-first，失败回退缓存
  if (req.mode === 'navigate') {
    e.respondWith(fetch(req).catch(function () {
      return caches.match(req).then(function (r) { return r || caches.match('/index.html'); });
    }).then(function (r) { return r || fallbackResponse(); }));
    return;
  }

  // 同源静态资源：cache-first，后台更新
  if (url.origin === self.location.origin) {
    e.respondWith(caches.match(req).then(function (cached) {
      var network = fetch(req).then(function (res) {
        if (okRes(res)) {
          var cp = res.clone();
          caches.open(CACHE).then(function (c) { c.put(req, cp); });
        }
        return res;
      }).catch(function () {
        return cached || caches.match(req);
      });
      return Promise.resolve(cached || network).then(function (r) { return r || fallbackResponse(); });
    }));
    return;
  }

  // 跨域（OSS 图片等）：仅对图片做 no-cors 缓存，脚本/统计等放行
  if (req.destination === 'image' || url.hostname.indexOf('aliyuncs.com') > -1) {
    e.respondWith(caches.open(CACHE).then(function (c) {
      return c.match(req).then(function (cached) {
        var net = fetch(req, { mode: 'no-cors' }).then(function (res) {
          if (res) {
            try { c.put(req, res.clone()); } catch (err) {}
          }
          return res;
        }).catch(function () { return cached; });
        return Promise.resolve(cached || net).then(function (r) { return r || fallbackResponse(); });
      });
    }));
  }
});
