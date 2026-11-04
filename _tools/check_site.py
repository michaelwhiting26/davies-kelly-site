"""Static checks (spec H.13, J.1, J.3). Python 3 stdlib only. Run from repo root: python3 -I _tools/check_site.py"""
import glob, json, os, re, sys, xml.dom.minidom
from html.parser import HTMLParser

BANNED = ["on your side", "winning", "client's interests first", "clients' interests first", "clients’ interests first", "unrelenting client focus", "best chances of success", "make or break", "no one else", "innovative solutions", "guarantee ", "we will prove", "world-class", "legally qualified"]
NAMES = ["Hamad", "Dubai Tram", "Barzan", "Doha Metro", "Al Bayt", "Marina 101", "Princess Tower", "Langham", "Al Bustan", "King Abdullah", "Wadi Safar", "Dabb", "Badra", "Mirfa", "Etihad Rail", "Meena Plaza", "Abu Dhabi Plaza", "Fujairah", "Aabenraa", "Frankfurt", "Bahrain Bay", "Melamchi", "Colombo", "Riga", "HS2", "World Cup", "SHLNG", "GLNG", "North–South Railway", "Lusail", "Ruwais", "Grampian", "Pearl GTL", "Crossrail", "Samsung", "Pinsent", "Envision", "NEOM", "Kuehne", "Broomielaw", "Aramco"]
ALLOWED_EXT = ("https://davieskelly.com", "https://www.linkedin.com/company/davies-kelly/", "https://www.google.com/maps/", "https://wa.me/", "mailto:", "tel:", "#", "data:")


class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.h1 = 0; s.links = []; s.imgs = []; s.title = ""; s._t = False; s.desc = None; s.canon = None; s.ld = []; s._ld = False; s.text = []
    def handle_starttag(s, t, a):
        a = dict(a)
        if t == "h1": s.h1 += 1
        if t == "title": s._t = True
        if t in ("a", "link") and a.get("href"): s.links.append(a["href"])
        if t in ("img", "source", "script") and (a.get("src") or a.get("srcset")):
            if a.get("srcset"): s.links += [x.strip().split(" ")[0] for x in a["srcset"].split(",")]
            if a.get("src") and not a["src"].startswith("data:"): s.links.append(a["src"])
        if t == "img": s.imgs.append(a)
        if t == "meta" and a.get("name") == "description": s.desc = a.get("content")
        if t == "link" and a.get("rel") == "canonical": s.canon = a.get("href")
        if t == "script" and a.get("type") == "application/ld+json": s._ld = True
    def handle_endtag(s, t):
        if t == "title": s._t = False
        if t == "script": s._ld = False
    def handle_data(s, d):
        if s._t: s.title += d
        if s._ld: s.ld.append(d)
        else: s.text.append(d)


fails, ph_ids = [], {}
files = [f for f in glob.glob("**/*.html", recursive=True) if not f.startswith(("_legacy", "_tools", "contact-us"))]
for f in sorted(files):
    src = open(f, encoding="utf-8").read()
    p = P(); p.feed(src)
    for m in re.findall(r'data-id="([A-Z]\d+)"', src):
        ph_ids[m] = ph_ids.get(m, 0) + 1
    if p.h1 != 1: fails.append(f"{f}: {p.h1} h1")
    if len(p.title) > 60: fails.append(f"{f}: title {len(p.title)} chars")
    if not p.desc or len(p.desc) > 160: fails.append(f"{f}: description length")
    if f != "404.html" and (not p.canon or not p.canon.startswith("https://davieskelly.com/")): fails.append(f"{f}: canonical")
    for blob in p.ld:
        try:
            j = json.loads(blob)
        except Exception as ex:
            fails.append(f"{f}: JSON-LD parse {ex}"); continue
        if "CONFIRM" in blob or "class=" in blob: fails.append(f"{f}: placeholder in JSON-LD")
    for im in p.imgs:
        if "alt" not in im or "width" not in im or "height" not in im: fails.append(f"{f}: img missing alt/width/height {im.get('src')}")
    text = " ".join(p.text).lower()
    for b in BANNED:
        if b.lower() in text: fails.append(f"{f}: banned phrase '{b}'")
    for n in NAMES:
        if n.lower() in src.lower(): fails.append(f"{f}: confidential name '{n}'")
    for l in p.links:
        if l.startswith(ALLOWED_EXT) or not l: continue
        if l.startswith("http"): fails.append(f"{f}: external origin {l}"); continue
        path = l.split("#")[0].split("?")[0]
        if not path: continue
        tgt = path.lstrip("/")
        if not (os.path.isfile(tgt) or os.path.isfile(os.path.join(tgt, "index.html"))): fails.append(f"{f}: broken link {l}")
    if len(src.encode()) > 50_000: fails.append(f"{f}: HTML {len(src.encode())} bytes > 50 KB")
for mf in ("robots.txt", "sitemap.xml", "llms.txt") + tuple(glob.glob("vcard/*.vcf")):
    s = open(mf, encoding="utf-8").read()
    if "CONFIRM" in s or "[" in s.replace("](", "").replace("[M", "").replace("[J", "").replace("[S", "").replace("[D", "") and mf != "llms.txt": fails.append(f"{mf}: placeholder")
    if "CONFIRM" in s: fails.append(f"{mf}: CONFIRM placeholder")
xml.dom.minidom.parse("sitemap.xml")
print("pages checked:", len(files))
print("placeholder markers:", sum(ph_ids.values()), "unique IDs:", len(ph_ids), sorted(ph_ids, key=lambda x: (x[0], int(x[1:]))))
print("FAILS:", len(fails))
for x in fails: print("  FAIL", x)
sys.exit(1 if fails else 0)
