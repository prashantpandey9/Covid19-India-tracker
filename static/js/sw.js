'use strict';
const cacheName = 'corona';
const startPage = '/';
const offlinePage = '/news';
const filesToCache = [startPage, offlinePage];
self.addEventListener('install', function(e) {
    console.log('SuperPWA service worker installation');
    e.waitUntil(caches.open(cacheName).then(function(cache) {
        console.log('SuperPWA service worker caching dependencies');
        filesToCache.map(function(url) {
            return cache.add(url).catch(function(reason) {
                return console.log('SuperPWA: ' + String(reason) + ' ' + url);
            });
        });
    }));
});
self.addEventListener('activate', function(e) {
    console.log('SuperPWA service worker activation');
    e.waitUntil(caches.keys().then(function(keyList) {
        return Promise.all(keyList.map(function(key) {
            if (key !== cacheName) {
                console.log('SuperPWA old cache removed', key);
                return caches.delete(key);
            }
        }));
    }));
    return self.clients.claim();
});
self.addEventListener('fetch', function(e) {
    if (!e.request.url.match(/^(http|https):\/\//i))
        return;
    if (new URL(e.request.url).origin !== location.origin)
        return;
    if (e.request.method !== 'GET') {
        e.respondWith(fetch(e.request).catch(function() {
            return caches.match(offlinePage);
        }));
        return;
    }
    if (e.request.mode === 'navigate' && navigator.onLine) {
        e.respondWith(fetch(e.request).then(function(response) {
            return caches.open(cacheName).then(function(cache) {
                cache.put(e.request, response.clone());
                return response;
            });
        }));
        return;
    }
    e.respondWith(caches.match(e.request).then(function(response) {
        return response || fetch(e.request).then(function(response) {
            return caches.open(cacheName).then(function(cache) {
                cache.put(e.request, response.clone());
                return response;
            });
        });
    }).catch(function() {
        return caches.match(offlinePage);
    }));
});