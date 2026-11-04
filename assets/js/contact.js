/* Enquiry form, three short steps (adapted from avonstowe.com): 1 who and where, 2 your details, 3 overview + review.
   Required: role, stage, name, email. Optional: organisation, phone, overview. Sends by opening the visitor's email app. */
(function () {
  "use strict";
  var form = document.getElementById("enquiry");
  if (!form || form.dataset.on) return; form.dataset.on = "1";
  var TO = form.getAttribute("data-to"), step = 1, started = Date.now();
  var LABELS = { role: "You are", stage: "Where the matter is now", name: "Name", organisation: "Organisation", email: "Email", phone: "Phone or WhatsApp", outline: "Overview" };
  var panels = form.querySelectorAll(".cf-panel"), bar = form.querySelector(".cf-progress span"), stepEl = form.querySelector(".cf-step"),
      summary = form.querySelector(".cf-summary"), back = form.querySelector("[data-back]"), submit = form.querySelector('button[type="submit"]');
  function val(k) { var el = form.elements[k]; if (!el) return ""; if (el.length !== undefined && !el.tagName) { var c = form.querySelector('input[name="' + k + '"]:checked'); return c ? c.value : ""; } return (el.value || "").trim(); }
  function validate(n) {
    var e = {};
    if (n === 1) { if (!val("role")) e.role = "Select who you are"; if (!val("stage")) e.stage = "Select where the matter is now"; }
    if (n === 2) {
      if (!val("name")) e.name = "Enter your name";
      if (!val("email")) e.email = "Enter your email address";
      else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val("email"))) e.email = "Enter an email address in the correct format, like name@example.com";
      if (val("phone") && !/^\+?[0-9 ()-]{6,30}$/.test(val("phone"))) e.phone = "Enter a phone number using digits, spaces and a leading +";
    }
    if (n === 3 && val("outline").length > 1500) e.outline = "Overview must be 1,500 characters or fewer";
    return e;
  }
  function showErrors(e) {
    form.querySelectorAll(".cf-err").forEach(function (p) { p.hidden = true; p.textContent = ""; });
    form.querySelectorAll(".cf-invalid").forEach(function (x) { x.classList.remove("cf-invalid"); x.removeAttribute("aria-invalid"); });
    var keys = Object.keys(e), ul = summary.querySelector("ul"); ul.innerHTML = "";
    keys.forEach(function (k) {
      var f = form.querySelector("#f-" + k), p = f && f.querySelector(".cf-err"); if (p) { p.textContent = e[k]; p.hidden = false; }
      var inp = form.querySelector("#cf-" + k); if (inp) { inp.classList.add("cf-invalid"); inp.setAttribute("aria-invalid", "true"); }
      var li = document.createElement("li"), a = document.createElement("a"); a.href = "#f-" + k; a.textContent = e[k]; li.appendChild(a); ul.appendChild(li);
    });
    summary.hidden = !keys.length; if (keys.length) summary.focus();
    return keys.length === 0;
  }
  function render() {
    panels.forEach(function (p) { p.hidden = +p.dataset.step !== step; });
    bar.style.width = (step / 3 * 100) + "%"; stepEl.querySelector("b").textContent = step;
    back.hidden = step === 1; submit.textContent = step < 3 ? "Continue" : "Send enquiry";
    if (step === 3) {
      form.querySelector('[data-r="who"]').textContent = [val("role"), val("stage")].filter(Boolean).join(" · ");
      form.querySelector('[data-r="details"]').textContent = [val("name"), val("organisation"), val("email"), val("phone")].filter(Boolean).join(" · ");
    }
  }
  function text() { return Object.keys(LABELS).filter(function (k) { return val(k); }).map(function (k) { return LABELS[k] + ": " + val(k); }).join("\n"); }
  function go(n) { summary.hidden = true; step = n; render(); stepEl.focus(); }
  form.querySelectorAll(".cf-chip input").forEach(function (r) { r.addEventListener("change", function () {
    form.querySelectorAll('input[name="' + r.name + '"]').forEach(function (o) { o.closest(".cf-chip").classList.toggle("is-on", o.checked); });
    var p = form.querySelector("#f-" + r.name + " .cf-err"); if (p) p.hidden = true; }); });
  form.querySelectorAll("[data-go]").forEach(function (b) { b.addEventListener("click", function () { go(+b.dataset.go); }); });
  back.addEventListener("click", function () { go(step - 1); });
  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    if (step < 3) { if (showErrors(validate(step))) go(step + 1); return; }
    var all = {}; [1, 2, 3].forEach(function (n) { var e = validate(n); for (var k in e) all[k] = e[k]; });
    if (!showErrors(all)) return;
    if (form.querySelector("#cf-website").value || Date.now() - started < 3000) return;
    var subject = ("Enquiry: " + val("role") + (val("organisation") ? ", " + val("organisation") : "")).slice(0, 120);
    var t = text();
    document.getElementById("copy-text").value = t;
    var r = document.getElementById("result"); r.hidden = false;
    window.location.href = "mailto:" + TO + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(t.slice(0, 1800));
    var h = r.querySelector("h2"); h && h.focus();
  });
  var cp = document.getElementById("copy-enquiry");
  cp && cp.addEventListener("click", function () {
    var t = document.getElementById("copy-text").value, s = document.getElementById("copy-status");
    (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { s.textContent = "Copied"; }, function () { document.getElementById("copy-text").select(); s.textContent = "Press Ctrl+C or Cmd+C to copy"; });
  });
  render();
})();
