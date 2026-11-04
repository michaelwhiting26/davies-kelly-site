/* Menu drawer + hero slideshow. No dependencies. */
(function () {
  "use strict";
  // ---- Menu drawer
  var btn = document.querySelector(".menu-btn"), drawer = document.getElementById("site-menu");
  if (btn && drawer) {
    var closeBtn = drawer.querySelector(".menu-close"), main = document.querySelectorAll("body > :not(#site-menu):not(script)");
    btn.removeAttribute("href"); btn.setAttribute("tabindex", "0");
    btn.addEventListener("keydown", function (e) { if (e.key === " " || e.key === "Enter") { e.preventDefault(); open(); } });
    function focusables() { return drawer.querySelectorAll("a[href],button:not([disabled])"); }
    function open() {
      drawer.classList.add("open"); drawer.removeAttribute("hidden"); btn.setAttribute("aria-expanded", "true");
      document.body.classList.add("menu-open");
      main.forEach(function (el) { el.setAttribute("inert", ""); });
      var f = focusables(); if (f.length) f[0].focus();
    }
    function close() {
      drawer.classList.remove("open"); btn.setAttribute("aria-expanded", "false");
      document.body.classList.remove("menu-open");
      main.forEach(function (el) { el.removeAttribute("inert"); });
      btn.focus();
    }
    btn.addEventListener("click", function (e) { e.preventDefault(); open(); });
    closeBtn && closeBtn.addEventListener("click", close);
    drawer.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { close(); return; }
      if (e.key !== "Tab") return;
      var f = focusables(), first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  }

  // ---- Hero slideshow
  var hero = document.querySelector(".hero-media");
  if (!hero) return;
  var slides = hero.querySelectorAll(".slide"), dots = hero.querySelectorAll(".dot"), pauseBtn = hero.querySelector(".pause");
  var i = 0, timer = null, stopped = false;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function hydrate(s) {
    s.querySelectorAll("[data-srcset]").forEach(function (el) { el.setAttribute("srcset", el.getAttribute("data-srcset")); el.removeAttribute("data-srcset"); });
    var im = s.querySelector("img[data-src]"); if (im) { im.src = im.getAttribute("data-src"); im.removeAttribute("data-src"); }
  }
  function go(n) {
    slides[i].classList.remove("on"); dots[i].removeAttribute("aria-current");
    slides[i].setAttribute("aria-hidden", "true");
    i = (n + slides.length) % slides.length;
    hydrate(slides[i]);
    slides[i].classList.add("on"); slides[i].removeAttribute("aria-hidden"); dots[i].setAttribute("aria-current", "true");
  }
  function play() { if (stopped || reduce) return; clearInterval(timer); timer = setInterval(function () { go(i + 1); }, 7000); }
  function pause() { clearInterval(timer); timer = null; }
  function stop() { stopped = true; pause(); setPauseUI(true); }
  function setPauseUI(p) {
    if (!pauseBtn) return;
    pauseBtn.setAttribute("aria-label", p ? "Play slideshow" : "Pause slideshow");
    pauseBtn.innerHTML = p ? '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>' : '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>';
  }
  dots.forEach(function (d, k) { d.addEventListener("click", function () { go(k); stop(); }); });
  if (pauseBtn) pauseBtn.addEventListener("click", function () {
    if (stopped) { stopped = false; setPauseUI(false); go(i + 1); play(); } else { stop(); }
  });
  hero.addEventListener("mouseenter", pause); hero.addEventListener("mouseleave", play);
  hero.addEventListener("focusin", pause); hero.addEventListener("focusout", play);
  document.addEventListener("visibilitychange", function () { document.hidden ? pause() : play(); });
  var x0 = null;
  hero.addEventListener("pointerdown", function (e) { x0 = e.clientX; });
  hero.addEventListener("pointerup", function (e) {
    if (x0 === null) return; var dx = e.clientX - x0; x0 = null;
    if (Math.abs(dx) > 40) { go(dx < 0 ? i + 1 : i - 1); stop(); }
  });
  if (reduce) { setPauseUI(true); stopped = true; }
  window.addEventListener("load", function () {
    setTimeout(function () { slides.forEach(function (s, k) { if (k) hydrate(s); }); }, 1500);
    play();
  });
})();

/* Team rotator: random start, rotates every 5.5s, tap a thumbnail to feature a person */
window.DKteam = function (scope) {
  var root = (scope || document).querySelector(".team-rot"); if (!root || root.dataset.on) return; root.dataset.on = "1";
  var feats = root.querySelectorAll(".tr-feature"), thumbs = root.querySelectorAll(".tr-thumb"), dets = root.querySelectorAll(".tr-detail");
  var n = feats.length, i = 0, timer = null, paused = false;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function show(k) {
    i = (k + n) % n;
    [feats, thumbs, dets].forEach(function (list) { list.forEach(function (el) { el.classList.toggle("on", +el.dataset.i === i); }); });
  }
  function start() { if (reduce) return; clearInterval(timer); timer = setInterval(function () { if (!paused && !document.hidden) show(i + 1); }, 5500); }
  thumbs.forEach(function (b) { b.addEventListener("click", function () { show(+b.dataset.i); start(); }); });
  root.addEventListener("pointerenter", function (e) { if (e.pointerType === "mouse") paused = true; });
  root.addEventListener("pointerleave", function (e) { if (e.pointerType === "mouse") paused = false; });
  root.addEventListener("focusin", function () { paused = true; });
  root.addEventListener("focusout", function () { paused = false; });
  show(0); start();
};
window.DKteam();

/* Sticky CTA hides over the footer/contact areas */
(function () {
  var cta = document.querySelector(".sticky-cta"); if (!cta || !("IntersectionObserver" in window)) return;
  var targets = document.querySelectorAll("footer, .cta-band, form, .hero, .team-rot, .tr-details, .case-rot"); var visible = new Set();
  var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) visible.add(e.target); else visible.delete(e.target); }); cta.classList.toggle("hide", visible.size > 0); });
  targets.forEach(function (t) { io.observe(t); });
})();

/* Selected experience rotator (phones): cycles every 7s, dots, swipe; pauses on interaction */
window.DKcases = function (scope) {
  var root = (scope || document).querySelector(".case-rot"); if (!root || root.dataset.on) return; root.dataset.on = "1";
  var items = root.querySelectorAll(".cr-item"), dots = root.querySelectorAll(".cr-dot"), n = items.length, i = 0, timer, held = false;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function show(k) { i = (k + n) % n; items.forEach(function (el) { var on = +el.dataset.i === i; el.classList.toggle("on", on); el.setAttribute("aria-hidden", on ? "false" : "true"); }); dots.forEach(function (d) { d.classList.toggle("on", +d.dataset.i === i); }); }
  function start() { if (reduce) return; clearInterval(timer); timer = setInterval(function () { if (!held && !document.hidden) show(i + 1); }, 7000); }
  dots.forEach(function (d) { d.addEventListener("click", function () { show(+d.dataset.i); start(); }); });
  var x0 = null;
  root.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; held = true; }, { passive: true });
  root.addEventListener("touchend", function (e) { held = false; if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) { show(i + (dx < 0 ? 1 : -1)); start(); } x0 = null; });
  root.addEventListener("focusin", function () { held = true; }); root.addEventListener("focusout", function () { held = false; });
  start();
};
window.DKcases();


/* One continuous scroll: internal pages open in a panel over the home page, with a large close (X).
   Each page keeps its own address (deep links, search and no-JS still work). Back button and Esc close it. */
(function () {
  if (!window.fetch || !window.history || !history.pushState || !window.DOMParser) return;
  var home = location.pathname === "/" || location.pathname === "/index.html";
  var sheet = null, lastFocus = null, openedHere = false, scrollY = 0;
  function sheetOpen() { return !!(sheet && sheet.classList.contains("open")); }
  function eligible(a) {
    if (!a || !a.href || a.target || a.hasAttribute("download")) return false;
    var u; try { u = new URL(a.href, location.href); } catch (e) { return false; }
    if (u.origin !== location.origin) return false;
    if (u.pathname === "/" || u.pathname === "/index.html") return false;
    if (u.pathname === location.pathname && !sheetOpen()) return false;
    if (/\.(vcf|pdf|xml|txt|png|jpg|zip)$/i.test(u.pathname)) return false;
    return true;
  }
  function build() {
    sheet = document.createElement("div");
    sheet.className = "sheet"; sheet.setAttribute("role", "dialog"); sheet.setAttribute("aria-modal", "true");
    sheet.innerHTML = '<div class="sheet-panel" tabindex="-1"><button type="button" class="sheet-close" aria-label="Close and return to the home page"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></button><div class="sheet-body"></div></div>';
    document.body.appendChild(sheet);
    sheet.querySelector(".sheet-close").addEventListener("click", function () { close(true); });
    sheet.addEventListener("click", function (e) { if (e.target === sheet) close(true); });
    sheet.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { close(true); return; }
      if (e.key !== "Tab") return;
      var f = sheet.querySelectorAll('a[href],button:not([disabled]),input,select,textarea,[tabindex]:not([tabindex="-1"])');
      if (!f.length) return; var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  }
  function load(url, push) {
    return fetch(url, { credentials: "same-origin" }).then(function (r) { if (!r.ok) throw 0; return r.text(); }).then(function (txt) {
      var doc = new DOMParser().parseFromString(txt, "text/html");
      var main = doc.querySelector("main"); if (!main) throw 0;
      if (!sheet) build();
      var body = sheet.querySelector(".sheet-body");
      body.innerHTML = main.innerHTML;
      body.querySelectorAll(".hero-media").forEach(function (h) { h.remove(); });
      if (!document.body.classList.contains("sheet-open")) { scrollY = window.scrollY; lastFocus = document.activeElement; }
      document.body.classList.add("sheet-open");
      sheet.classList.add("open");
      sheet.querySelector(".sheet-panel").scrollTop = 0;
      document.title = doc.title;
      if (push) { history.pushState({ sheet: url }, "", url); openedHere = true; }
      if (window.DKteam) DKteam(body); if (window.DKcases) DKcases(body);
      if (body.querySelector("#enquiry")) { var sc = document.createElement("script"); var src = (doc.querySelector('script[src*="contact.js"]') || {}).getAttribute; sc.src = src ? doc.querySelector('script[src*="contact.js"]').getAttribute("src") : "/assets/js/contact.js"; body.appendChild(sc); }
      sheet.querySelector(".sheet-close").focus();
    }).catch(function () { location.href = url; });
  }
  function close(viaUi) {
    if (!sheet || !sheet.classList.contains("open")) return;
    if (viaUi && openedHere && history.state && history.state.sheet) { history.back(); return; }
    sheet.classList.remove("open"); document.body.classList.remove("sheet-open");
    document.title = HOME_TITLE; var y = scrollY; requestAnimationFrame(function () { window.scrollTo(0, y); });
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  var HOME_TITLE = document.title;
  document.addEventListener("click", function (e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target.closest && e.target.closest("a");
    if (a && sheetOpen() && a.href) { try { var hu = new URL(a.href, location.href); if (hu.origin === location.origin && (hu.pathname === "/" || hu.pathname === "/index.html") && home) { e.preventDefault(); close(true); return; } } catch (x) {} }
    if (!eligible(a)) return;
    var u = new URL(a.href, location.href);
    var drawer = document.getElementById("site-menu"); if (drawer && drawer.classList.contains("open")) { var mc = drawer.querySelector(".menu-close"); mc && mc.click(); }
    e.preventDefault(); load(u.pathname + u.search + u.hash, true);
  });
  window.addEventListener("popstate", function (e) {
    if (e.state && e.state.sheet) load(e.state.sheet, false);
    else { openedHere = false; close(false); }
  });
})();
