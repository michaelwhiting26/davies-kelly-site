"""Build responsive images, icons and Open Graph images.
Run from the repo root:  python3 -I _tools/images.py
Sources: _legacy/img-original/ (kept out of git). Output: assets/img/, og/, favicon files.
"""
import os
from PIL import Image, ImageDraw, ImageFont

SRC = "_legacy/img-original"
OUT = "assets/img"
os.makedirs(f"{OUT}/hero", exist_ok=True)
os.makedirs(f"{OUT}/sectors", exist_ok=True)
os.makedirs(f"{OUT}/people", exist_ok=True)
os.makedirs(f"{OUT}/logo", exist_ok=True)
os.makedirs("og", exist_ok=True)

TEAL = (40, 100, 101)
NAVY = (20, 37, 61)
MUTED = (92, 102, 112)


def crop(im, ratio, fx=0.5, fy=0.5):
    """Crop to width/height ratio around focal point (fx, fy as fractions)."""
    w, h = im.size
    if w / h > ratio:
        nw, nh = int(h * ratio), h
    else:
        nw, nh = w, int(w / ratio)
    left = min(max(int(fx * w - nw / 2), 0), w - nw)
    top = min(max(int(fy * h - nh / 2), 0), h - nh)
    return im.crop((left, top, left + nw, top + nh))


def save_set(im, base, widths, q_avif=50, q_webp=72, q_jpg=76):
    out = []
    for w in widths:
        if w > im.size[0]:
            continue
        r = im.resize((w, round(im.size[1] * w / im.size[0])), Image.LANCZOS)
        r.save(f"{base}-{w}.avif", quality=q_avif)
        r.save(f"{base}-{w}.webp", quality=q_webp, method=6)
        r.convert("RGB").save(f"{base}-{w}.jpg", quality=q_jpg, optimize=True, progressive=True)
        out.append((w, r.size[1]))
    if not out:  # source smaller than every width: keep native size
        w = im.size[0]
        im.save(f"{base}-{w}.avif", quality=q_avif)
        im.save(f"{base}-{w}.webp", quality=q_webp, method=6)
        im.convert("RGB").save(f"{base}-{w}.jpg", quality=q_jpg, optimize=True, progressive=True)
        out.append(im.size)
    return out


# Hero slides (the reactor-site image hero.jpg is deliberately NOT used: spec G.8 / F15)
HERO = {
    "wind": ("hero-2.jpg", 0.62, 0.45),
    "water": ("hero-3.jpg", 0.5, 0.55),
    "tunnel": ("hero-4.jpg", 0.5, 0.5),
}
for name, (f, fx, fy) in HERO.items():
    im = Image.open(f"{SRC}/{f}").convert("RGB")
    for tag, ratio, widths in (("p", 4 / 5, [480, 640, 800]), ("m", 3 / 2, [960, 1280]), ("w", 16 / 9, [1280, 1920, 2400])):
        c = crop(im, ratio, fx, fy)
        sizes = save_set(c, f"{OUT}/hero/{name}-{tag}", widths)
        print("hero", name, tag, sizes)

# Sector tiles (1:1 phone, 4:3 desktop)
SECT = {"energy": ("sector-renewables.jpg", 0.62, 0.45), "water": ("sector-water.jpg", 0.5, 0.5), "transport": ("sector-tunnel.jpg", 0.5, 0.5)}
for name, (f, fx, fy) in SECT.items():
    im = Image.open(f"{SRC}/{f}").convert("RGB")
    save_set(crop(im, 1, fx, fy), f"{OUT}/sectors/{name}-sq", [480, 720])
    save_set(crop(im, 4 / 3, fx, fy), f"{OUT}/sectors/{name}-43", [640, 960])
    save_set(crop(im, 3 / 2, fx, fy), f"{OUT}/sectors/{name}-32", [640, 960])

# Headshots: 4:5 crop from 600x660 originals, top-weighted
PEOPLE = {"jamie-shafto": "jamie.jpg", "michael-roos": "roos.jpg", "stephen-john": "steve.jpg", "michael-whiting": "whiting.jpg"}
for slug, f in PEOPLE.items():
    im = Image.open(f"{SRC}/{f}").convert("RGB")
    c = crop(im, 4 / 5, 0.5, 0.5)
    for w in (160, 320, 528):
        r = c.resize((w, round(w * 5 / 4)), Image.LANCZOS)
        r.save(f"{OUT}/people/{slug}-{w}.avif", quality=55)
        r.save(f"{OUT}/people/{slug}-{w}.webp", quality=76, method=6)
        r.save(f"{OUT}/people/{slug}-{w}.jpg", quality=80, optimize=True, progressive=True)

# Logo + icons
logo = Image.open(f"{SRC}/davies-kelly-logo.png").convert("RGBA")
logo.save(f"{OUT}/logo/davies-kelly-logo.png", optimize=True)
lw, lh = logo.size
logo.resize((512, round(lh * 512 / lw)), Image.LANCZOS).save(f"{OUT}/logo/davies-kelly-logo-512.png", optimize=True)
# The "K" mark sits at the right of the logo: find its bounding box from alpha
mark = logo.crop((int(lw * 0.8), 0, lw, lh))
bbox = mark.getbbox()
mark = mark.crop(bbox)
side = max(mark.size)
sq = Image.new("RGBA", (side, side), (255, 255, 255, 0))
sq.paste(mark, ((side - mark.size[0]) // 2, (side - mark.size[1]) // 2), mark)
for s, name in ((180, "apple-touch-icon.png"), (512, f"{OUT}/logo/icon-512.png"), (32, f"{OUT}/logo/icon-32.png")):
    bg = Image.new("RGBA", (s, s), (255, 255, 255, 255))
    inner = sq.resize((int(s * 0.84), int(s * 0.84)), Image.LANCZOS)
    bg.paste(inner, ((s - inner.size[0]) // 2, (s - inner.size[1]) // 2), inner)
    bg.convert("RGB").save(name, optimize=True)
fav = Image.open(f"{OUT}/logo/icon-512.png")
fav.save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

# Open Graph images (1200x630)
FB = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FR = "/System/Library/Fonts/Supplemental/Arial.ttf"


def og_base():
    img = Image.new("RGB", (1200, 630), "white")
    d = ImageDraw.Draw(img)
    d.rectangle((0, 618, 1200, 630), fill=TEAL)
    lg = logo.resize((330, round(lh * 330 / lw)), Image.LANCZOS)
    return img, d, lg


img, d, lg = og_base()
img.paste(lg, (72, 64), lg)
f = ImageFont.truetype(FB, 58)
y = 220
for line in ("Independent quantum and", "delay experts for", "construction disputes"):
    d.text((72, y), line, font=f, fill=NAVY)
    y += 74
d.text((1128, 560), "davieskelly.com", font=ImageFont.truetype(FR, 26), fill=MUTED, anchor="ra")
img.save("og/og-default.png", optimize=True)

ROLES = {
    "michael-roos": ("Michael Roos", "Quantum expert"),
    "jamie-shafto": ("Jamie Shafto", "Delay expert"),
    "stephen-john": ("Stephen M John", "Engineering and contracts"),
    "michael-whiting": ("Michael Whiting", "Quantum analysis"),
}
for slug, (name, role) in ROLES.items():
    img, d, lg = og_base()
    head = Image.open(f"{OUT}/people/{slug}-528.jpg").resize((480, 600), Image.LANCZOS)
    img.paste(head, (0, 18))
    img.paste(lg, (560, 72), lg)
    d.text((560, 260), name, font=ImageFont.truetype(FB, 56), fill=NAVY)
    d.text((560, 340), role, font=ImageFont.truetype(FR, 36), fill=TEAL)
    d.text((1128, 560), "davieskelly.com", font=ImageFont.truetype(FR, 26), fill=MUTED, anchor="ra")
    img.save(f"og/{slug}.png", optimize=True)
print("done")
