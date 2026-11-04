/* Contact form: GOV.UK-style validation, then a mailto hand-off with a copy fallback.
   It never claims the enquiry was sent: it cannot know. */
(function () {
  "use strict";
  var form = document.getElementById("enquiry");
  if (!form) return;
  var TO = form.getAttribute("data-to");
  var rules = [
    ["need", function (f) { return f.need.value ? "" : "Select what you need"; }],
    ["appointment", function (f) { return f.appointment.value ? "" : "Select the kind of appointment"; }],
    ["forum", function (f) { return f.forum.value ? "" : "Select where the matter is"; }],
    ["parties", function (f) { return f.parties.value.trim().length >= 3 ? "" : "Enter the names of the parties"; }],
    ["project", function (f) { return f.project.value.trim() ? "" : "Enter the project and country"; }],
    ["outline", function (f) { var v = f.outline.value.trim(); return !v ? "Enter a short outline" : v.length < 20 ? "Add a little more detail, at least 20 characters" : ""; }],
    ["name", function (f) { return f.name.value.trim() ? "" : "Enter your name"; }],
    ["organisation", function (f) { return f.organisation.value.trim() ? "" : "Enter your organisation"; }],
    ["email", function (f) { var v = f.email.value.trim(); return !v ? "Enter your email address" : /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? "" : "Enter an email address in the correct format, like name@example.com"; }],
    ["phone", function (f) { var v = f.phone.value.trim(); return !v || /^\+?[0-9 ()-]{6,30}$/.test(v) ? "" : "Enter a phone number using digits, spaces and a leading +"; }],
    ["ack", function (f) { return f.ack.checked ? "" : "Confirm you have not included confidential information"; }]
  ];
  var touched = false;
  function wrap(name) { return document.getElementById("f-" + name); }
  function clear() {
    form.querySelectorAll(".err").forEach(function (e) { e.remove(); });
    form.querySelectorAll(".invalid").forEach(function (e) { e.classList.remove("invalid"); });
    form.querySelectorAll("[aria-invalid]").forEach(function (e) { e.removeAttribute("aria-invalid"); });
    var s = document.getElementById("error-summary"); if (s) s.remove();
  }
  function validate(showSummary) {
    clear();
    var errors = [];
    rules.forEach(function (r) {
      var msg = r[1](form.elements);
      if (!msg) return;
      errors.push([r[0], msg]);
      var w = wrap(r[0]); if (!w) return;
      w.classList.add("invalid");
      var p = document.createElement("p"); p.className = "err"; p.id = "err-" + r[0]; p.textContent = msg;
      var anchor = w.querySelector("input,select,textarea,.chipset");
      if (w.tagName === "FIELDSET") w.insertBefore(p, w.querySelector(".chipset") || w.firstChild.nextSibling);
      else anchor.parentNode.insertBefore(p, anchor);
      w.querySelectorAll("input,select,textarea").forEach(function (el) {
        el.setAttribute("aria-invalid", "true");
        var d = (el.getAttribute("aria-describedby") || "").replace(/\s*err-\S+/g, "");
        el.setAttribute("aria-describedby", (d + " err-" + r[0]).trim());
      });
    });
    if (errors.length && showSummary) {
      var box = document.createElement("div"); box.className = "error-summary"; box.id = "error-summary"; box.tabIndex = -1;
      box.innerHTML = "<h2>There is a problem</h2><ul></ul>";
      errors.forEach(function (e) {
        var li = document.createElement("li"), a = document.createElement("a");
        a.href = "#f-" + e[0]; a.textContent = e[1];
        a.addEventListener("click", function (ev) { ev.preventDefault(); var t = wrap(e[0]).querySelector("input,select,textarea"); t && t.focus(); });
        li.appendChild(a); box.querySelector("ul").appendChild(li);
      });
      form.insertBefore(box, form.firstChild); box.focus();
    }
    return errors.length === 0;
  }
  form.addEventListener("input", function () { if (touched) validate(false); });
  form.addEventListener("change", function () { if (touched) validate(false); });
  var outline = form.elements.outline, counter = document.getElementById("outline-count");
  if (outline && counter) outline.addEventListener("input", function () {
    var left = 1000 - outline.value.length; counter.textContent = left + " characters left";
  });
  function compose() {
    var f = form.elements;
    var body = [
      "Website enquiry: Davies Kelly", "",
      "Need: " + f.need.value, "Appointment: " + f.appointment.value, "Forum: " + f.forum.value, "",
      "Parties: " + f.parties.value.trim(), "Instructing firm or counsel: " + (f.counsel.value.trim() || "-"),
      "Project and country: " + f.project.value.trim(), "Key date: " + (f.keydate.value.trim() || "-"), "",
      "Outline: " + f.outline.value.trim(), "",
      "Name: " + f.name.value.trim(), "Organisation: " + f.organisation.value.trim(), "Role: " + (f.role.value.trim() || "-"),
      "Email: " + f.email.value.trim(), "Phone: " + (f.phone.value.trim() || "-"), "",
      "Sender confirmed: no confidential or privileged information included; no engagement created."
    ].join("\n");
    return { subject: "Website enquiry: " + f.need.value + ", " + f.project.value.trim(), body: body };
  }
  form.addEventListener("submit", function (e) {
    e.preventDefault(); touched = true;
    var f = form.elements;
    if (f.company_website.value) return; // honeypot
    if (!validate(true)) return;
    var m = compose();
    var body = m.body.length > 1800 ? m.body.slice(0, 1780) + "\n[shortened: see copy on the website form]" : m.body;
    var href = "mailto:" + TO + "?subject=" + encodeURIComponent(m.subject) + "&body=" + encodeURIComponent(body);
    var res = document.getElementById("result");
    res.querySelector("textarea").value = "To: " + TO.replace(/,/g, ", ") + "\nSubject: " + m.subject + "\n\n" + m.body;
    res.hidden = false;
    var h = res.querySelector("h2"); h.focus();
    window.location.href = href;
  });
  var copy = document.getElementById("copy-enquiry");
  if (copy) copy.addEventListener("click", function () {
    var t = document.querySelector("#result textarea"), st = document.getElementById("copy-status");
    (navigator.clipboard ? navigator.clipboard.writeText(t.value) : Promise.reject()).then(function () {
      st.textContent = "Copied. Paste it into an email to " + TO.replace(/,/g, " and ") + ".";
    }, function () { t.select(); st.textContent = "Select the text above and copy it."; });
  });
})();
