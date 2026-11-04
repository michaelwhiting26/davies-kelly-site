"""Browser checks (spec J.2). Needs Python Playwright. Serves the repo root on :8791.
Run from repo root: python3 -I _tools/browser_test.py"""
import os, subprocess, sys, time, json
from playwright.sync_api import sync_playwright

PAGES = ["/", "/experts/", "/experts/michael-roos/", "/experts/jamie-shafto/", "/experts/stephen-john/", "/experts/michael-whiting/", "/services/", "/services/quantum/", "/services/delay/", "/services/technical/", "/services/advisory/", "/sectors/", "/experience/", "/independence/", "/about/", "/insights/", "/contact/", "/privacy/", "/cookies/", "/terms/", "/404.html"]
VIEWS = [(360, 740), (390, 844), (768, 1024), (1440, 900), (320, 640)]
os.makedirs("_tools/shots", exist_ok=True)
srv = None  # start separately: python3 -m http.server 8791 --bind 127.0.0.1
fails, notes = [], []
try:
    with sync_playwright() as pw:
        for engine in (pw.chromium, pw.webkit):
            br = engine.launch()
            for w, h in VIEWS:
                ctx = br.new_context(viewport={"width": w, "height": h}, device_scale_factor=1, has_touch=w < 900, is_mobile=False)
                pg = ctx.new_page()
                ext = []
                pg.on("request", lambda r: ext.append(r.url) if not r.url.startswith(("http://127.0.0.1", "data:")) else None)
                for path in PAGES:
                    pg.goto("http://127.0.0.1:8791" + path, wait_until="load")
                    sw = pg.evaluate("document.documentElement.scrollWidth")
                    if sw > w:
                        wide = pg.evaluate("""() => [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > innerWidth + 1).slice(0,4).map(e => e.tagName + '.' + e.className)""")
                        fails.append(f"{engine.name} {w}px {path}: horizontal scroll {sw}>{w} {wide}")
                    small = pg.evaluate("""() => [...document.querySelectorAll('a,button,input,select,textarea,summary')].filter(e => {const r=e.getBoundingClientRect(); const s=getComputedStyle(e); if(!r.width||s.visibility==='hidden'||e.closest('[hidden],.drawer:not(.open),.honey,.vh')) return false; const inline = s.display==='inline' && e.closest('p,li,dd,span'); if(inline) return false; if(e.type==='radio'||e.type==='checkbox') return false; return r.height < 44 || r.width < 24;}).slice(0,5).map(e => (e.tagName+':'+(e.textContent||e.name||'').trim().slice(0,30)+':'+Math.round(e.getBoundingClientRect().height)))""")
                    if small:
                        fails.append(f"{engine.name} {w}px {path}: small targets {small}")
                    if engine.name == "chromium" and path in ("/", "/experts/michael-roos/", "/contact/", "/experience/") and w in (390, 1440, 768, 360):
                        pg.screenshot(path=f"_tools/shots/{path.strip('/').replace('/','_') or 'home'}-{w}.png", full_page=False)
                if ext:
                    fails.append(f"{engine.name} {w}px third-party requests: {set(ext)}")
                # above the fold on phone profile
                if w == 390:
                    pg.goto("http://127.0.0.1:8791/experts/michael-roos/")
                    b = pg.evaluate("document.querySelector('.contact-row').getBoundingClientRect().bottom")
                    if b > h: fails.append(f"{engine.name} 390: profile contact row below fold ({b})")
                    else: notes.append(f"{engine.name} 390: profile contact row bottom at {round(b)}px (fold {h})")
                    # menu
                    pg.goto("http://127.0.0.1:8791/")
                    pg.click(".site-header .menu-btn")
                    pg.wait_for_timeout(300)
                    opened = pg.evaluate("document.getElementById('site-menu').classList.contains('open')")
                    focus_in = pg.evaluate("document.getElementById('site-menu').contains(document.activeElement)")
                    pg.keyboard.press("Escape"); pg.wait_for_timeout(300)
                    closed = not pg.evaluate("document.getElementById('site-menu').classList.contains('open')")
                    back = pg.evaluate("document.activeElement.classList.contains('menu-btn')")
                    if not (opened and focus_in and closed and back): fails.append(f"{engine.name}: menu open={opened} focusIn={focus_in} closed={closed} focusBack={back}")
                    else: notes.append(f"{engine.name}: menu open/focus-trap/Esc/return OK")
                    # slideshow dots + pause
                    pg.click(".dot:nth-child(2)"); pg.wait_for_timeout(200)
                    cur = pg.evaluate("[...document.querySelectorAll('.slide')].findIndex(s => s.classList.contains('on'))")
                    lbl = pg.get_attribute(".pause", "aria-label")
                    if cur != 1 or lbl != "Play slideshow": fails.append(f"{engine.name}: slideshow dot={cur} pause={lbl}")
                    else: notes.append(f"{engine.name}: slideshow dots + pause OK")
                    # form validation
                    pg.goto("http://127.0.0.1:8791/contact/")
                    pg.click("#enquiry button[type=submit]"); pg.wait_for_timeout(200)
                    n = pg.evaluate("document.querySelectorAll('#error-summary li').length")
                    foc = pg.evaluate("document.activeElement.id")
                    if n != 10 or foc != "error-summary": fails.append(f"{engine.name}: form errors={n} focus={foc}")
                    else: notes.append(f"{engine.name}: form error summary (10 errors) + focus OK")
                ctx.close()
            # reduced motion
            ctx = br.new_context(viewport={"width": 390, "height": 844}, reduced_motion="reduce")
            pg = ctx.new_page(); pg.goto("http://127.0.0.1:8791/"); pg.wait_for_timeout(8000)
            cur = pg.evaluate("[...document.querySelectorAll('.slide')].findIndex(s => s.classList.contains('on'))")
            if cur != 0: fails.append(f"{engine.name}: reduced motion still advanced")
            else: notes.append(f"{engine.name}: reduced motion = no auto-advance OK")
            ctx.close(); br.close()
finally:
    pass
for n in notes: print("PASS", n)
print("FAILS", len(fails))
for f in fails: print("FAIL", f)
