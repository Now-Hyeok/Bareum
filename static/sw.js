if(!self.define){let e,i={};const n=(n,s)=>(n=new URL(n+".js",s).href,i[n]||new Promise((i=>{if("document"in self){const e=document.createElement("script");e.src=n,e.onload=i,document.head.appendChild(e)}else e=n,importScripts(n),i()})).then((()=>{let e=i[n];if(!e)throw new Error(`Module ${n} didn’t register its module`);return e})));self.define=(s,o)=>{const r=e||("document"in self?document.currentScript.src:"")||location.href;if(i[r])return;let c={};const d=e=>n(e,r),f={module:{uri:r},exports:c,require:d};i[r]=Promise.all(s.map((e=>f[e]||d(e)))).then((e=>(o(...e),c)))}}define(["./workbox-fa446783"],(function(e){"use strict";self.skipWaiting(),e.clientsClaim(),e.precacheAndRoute([{url:"assets/index-13f0b708.css",revision:null},{url:"assets/index-6434c589.js",revision:null},{url:"index.html",revision:"a9f3279634ec0b4b388f5ab331d259ec"},{url:"registerSW.js",revision:"1872c500de691dce40960bb85481de07"},{url:"icons/android-chrome-192x192.png",revision:"c8918faace4e164a4f56d62c127d2898"},{url:"icons/android-chrome-512x512.png",revision:"1448d2b141e2d2674093c6b3a7a6a2e5"},{url:"icons/apple-touch-icon.png",revision:"dd37c59fdfbf88e4a2962b4b8c1dcf36"},{url:"icons/browserconfig.xml",revision:"68c9044fa4a08749efb85bb2a4edaede"},{url:"icons/favicon-16x16.png",revision:"40dc2bfa421a7bbbe8225a52ae15747f"},{url:"icons/favicon-32x32.png",revision:"e404d3cef075fdb5867b8b00b6025d99"},{url:"icons/favicon.ico",revision:"b43fc8df38c6209483a3949064c6ec31"},{url:"icons/mstile-150x150.png",revision:"fb15071ae7bba6ec2740b204fd2786a3"},{url:"icons/pen.png",revision:"eaded72a93647640cf76963eab360a20"},{url:"icons/site.webmanifest",revision:"22a36b7df2717d75493d9174d28391be"},{url:"manifest.webmanifest",revision:"f5178490c414fb1508f5b79ef9172ca2"}],{}),e.cleanupOutdatedCaches(),e.registerRoute(new e.NavigationRoute(e.createHandlerBoundToURL("index.html")))}));
