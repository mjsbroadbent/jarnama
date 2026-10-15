"""Small toolkit for era-styled animated GIF banners (PIL only).

    from banner import *
    b = Banner(468, 60)
    f = b.frame("#000080")                      # new frame filled with a colour
    text(f, (10, 8), "ATTELKOM DIAL-UP", font("impact", 30), "#ffff00", outline="#000")
    b.add(f, 600)                               # hold for 600 ms
    b.save("ads/attelkom/dialup_468x60.gif", colors=64)

Fonts: the Windows fonts real banners used (Impact, Tahoma, Verdana, Comic Sans)
are not installed here, so the aliases below map to the nearest free fonts.
`font(name, size, pixel=True)` turns off antialiasing for the jagged 1990s look.
Fonts marked latin_only have no Cyrillic; `font()` falls back for Cyrillic text
when you pass the text as `for_text`.
"""
import math
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

T = "/usr/share/fonts/truetype/"
G = "/usr/share/texmf/fonts/opentype/public/tex-gyre/"
FONTS = {
    # alias: (path, has_cyrillic)
    "arial": (T + "liberation/LiberationSans-Regular.ttf", True),
    "arialb": (T + "liberation/LiberationSans-Bold.ttf", True),
    "arialbi": (T + "liberation/LiberationSans-BoldItalic.ttf", True),
    "times": (T + "liberation/LiberationSerif-Regular.ttf", True),
    "timesb": (T + "liberation/LiberationSerif-Bold.ttf", True),
    "timesbi": (T + "liberation/LiberationSerif-BoldItalic.ttf", True),
    "verdana": (T + "dejavu/DejaVuSans.ttf", True),
    "verdanab": (T + "dejavu/DejaVuSans-Bold.ttf", True),
    "tahoma": (T + "dejavu/DejaVuSansCondensed.ttf", True),
    "tahomab": (T + "dejavu/DejaVuSansCondensed-Bold.ttf", True),
    "tahomabi": (T + "dejavu/DejaVuSansCondensed-BoldOblique.ttf", True),
    "georgia": (T + "dejavu/DejaVuSerif.ttf", True),
    "georgiab": (T + "dejavu/DejaVuSerifCondensed-Bold.ttf", True),
    "mono": (T + "liberation/LiberationMono-Regular.ttf", True),
    "monob": (T + "liberation/LiberationMono-Bold.ttf", True),
    "courier": (T + "freefont/FreeMonoBold.ttf", True),
    "impact": (G + "texgyreheroscn-bold.otf", False),  # condensed heavy sans, Latin only
    "impacti": (G + "texgyreheroscn-bolditalic.otf", False),
    "helv": (G + "texgyreheros-regular.otf", False),
    "helvb": (G + "texgyreheros-bold.otf", False),
    "poppins": (T + "google-fonts/Poppins-Regular.ttf", False),
    "poppinsm": (T + "google-fonts/Poppins-Medium.ttf", False),
    "poppinsb": (T + "google-fonts/Poppins-Bold.ttf", False),
    "inter": ("/usr/share/fonts/opentype/inter/Inter-Regular.otf", True),
    "interb": ("/usr/share/fonts/opentype/inter/Inter-Bold.otf", True),
    "interx": ("/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf", True),
    "interblk": ("/usr/share/fonts/opentype/inter/Inter-Black.otf", True),
}
CYR_FALLBACK = {"impact": "tahomab", "impacti": "tahomabi", "helv": "arial", "helvb": "arialb",
                "poppins": "inter", "poppinsm": "inter", "poppinsb": "interb"}

_cache = {}


class _Font:
    def __init__(self, f, pixel):
        self.f, self.pixel = f, pixel


def font(name, size, pixel=False, for_text=None):
    """A font by alias. pixel=True draws it without antialiasing."""
    if for_text and not FONTS[name][1] and any("Ѐ" <= c <= "ӿ" for c in for_text):
        name = CYR_FALLBACK.get(name, "arialb")
    key = (name, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(FONTS[name][0], size)
    return _Font(_cache[key], pixel)


def rgb(c):
    if isinstance(c, tuple):
        return c
    c = c.lstrip("#")
    if len(c) == 3:
        c = "".join(ch * 2 for ch in c)
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    a, b = rgb(a), rgb(b)
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


# ---------------------------------------------------------------- frames

class Banner:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.frames, self.durations = [], []

    def frame(self, bg="#ffffff"):
        return Image.new("RGB", (self.w, self.h), rgb(bg))

    def add(self, img, ms=100):
        self.frames.append(img.copy())
        self.durations.append(int(ms))

    def hold(self, ms):
        """Lengthen the last frame."""
        self.durations[-1] += int(ms)

    def save(self, path, colors=128, dither=False, loop=0, border=None):
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        frames = self.frames
        if border:
            frames = [outline_box(f.copy(), border) for f in frames]
        if path.endswith(".png") or len(frames) == 1 and not path.endswith(".gif"):
            frames[0].save(path)
            return path
        # one shared palette keeps colours steady from frame to frame
        strip = Image.new("RGB", (self.w, self.h * min(len(frames), 24)))
        step = max(1, len(frames) // 24)
        for i, f in enumerate(frames[::step][:24]):
            strip.paste(f, (0, i * self.h))
        pal = strip.quantize(colors, method=Image.Quantize.MEDIANCUT)
        d = Image.Dither.FLOYDSTEINBERG if dither else Image.Dither.NONE
        out = [f.quantize(palette=pal, dither=d) for f in frames]
        out[0].save(path, save_all=True, append_images=out[1:], duration=self.durations,
                    loop=loop, optimize=False, disposal=1)
        return path


def outline_box(img, color="#000000", width=1):
    d = ImageDraw.Draw(img)
    for i in range(width):
        d.rectangle([i, i, img.width - 1 - i, img.height - 1 - i], outline=rgb(color))
    return img


# ---------------------------------------------------------------- text

def _draw(img, pixel):
    d = ImageDraw.Draw(img)
    d.fontmode = "1" if pixel else "L"
    return d


def tsize(s, f, spacing=0):
    b = f.f.getbbox(s)
    return b[2] - b[0] + spacing * max(0, len(s) - 1), b[3] - b[1]


def text(img, xy, s, f, fill="#000", outline=None, ow=1, shadow=None, sxy=(1, 1),
         anchor="la", spacing=0, align="left"):
    """Draw text. anchor uses PIL codes ('la' left-ascender, 'mm' centre, 'rs' ...).
    outline draws a stroke; shadow a drop shadow offset by sxy. spacing = letter spacing."""
    d = _draw(img, f.pixel)
    if spacing:
        w, _ = tsize(s, f, spacing)
        x, y = xy
        if anchor[0] == "m":
            x -= w / 2
        elif anchor[0] == "r":
            x -= w
        a = "l" + anchor[1]
        for ch in s:
            text(img, (x, y), ch, f, fill, outline, ow, shadow, sxy, a)
            x += f.f.getlength(ch) + spacing
        return
    if shadow:
        d.text((xy[0] + sxy[0], xy[1] + sxy[1]), s, font=f.f, fill=rgb(shadow), anchor=anchor,
               stroke_width=ow if outline else 0, stroke_fill=rgb(shadow), align=align)
    d.text(xy, s, font=f.f, fill=rgb(fill), anchor=anchor, align=align,
           stroke_width=ow if outline else 0, stroke_fill=rgb(outline) if outline else None)


def fit_font(name, s, max_w, max_size, min_size=6, pixel=False):
    """Largest size of font `name` at which s fits in max_w pixels."""
    for size in range(max_size, min_size - 1, -1):
        f = font(name, size, pixel, for_text=s)
        if tsize(s, f)[0] <= max_w:
            return f
    return font(name, min_size, pixel, for_text=s)


def gradient_text(img, xy, s, f, top, bottom, outline=None, ow=1, anchor="la"):
    """Text filled with a vertical gradient (the WordArt look)."""
    mask = Image.new("L", img.size, 0)
    md = ImageDraw.Draw(mask)
    md.fontmode = "1" if f.pixel else "L"
    md.text(xy, s, font=f.f, fill=255, anchor=anchor)
    box = mask.getbbox()
    if outline:
        text(img, xy, s, f, outline, outline=outline, ow=ow, anchor=anchor)
    if not box:
        return
    grad = Image.new("RGB", img.size)
    gradient(grad, (0, box[1], img.width, box[3]), top, bottom)
    img.paste(grad, (0, 0), mask)


# ---------------------------------------------------------------- shapes

def gradient(img, box, c1, c2, vertical=True):
    x0, y0, x1, y1 = [int(v) for v in box]
    d = ImageDraw.Draw(img)
    n = (y1 - y0) if vertical else (x1 - x0)
    for i in range(max(n, 1)):
        c = mix(c1, c2, i / max(n - 1, 1))
        if vertical:
            d.line([(x0, y0 + i), (x1 - 1, y0 + i)], fill=c)
        else:
            d.line([(x0 + i, y0), (x0 + i, y1 - 1)], fill=c)
    return img


def rect(img, box, fill=None, outline=None, width=1, radius=0):
    d = ImageDraw.Draw(img)
    if radius:
        d.rounded_rectangle(box, radius, fill=rgb(fill) if fill else None,
                            outline=rgb(outline) if outline else None, width=width)
    else:
        d.rectangle(box, fill=rgb(fill) if fill else None,
                    outline=rgb(outline) if outline else None, width=width)


def starburst(img, center, r_out, r_in, points=16, fill="#ff0", outline="#c00", rot=0, width=2):
    cx, cy = center
    pts = []
    for i in range(points * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.pi * i / points + rot
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d = ImageDraw.Draw(img)
    d.polygon(pts, fill=rgb(fill), outline=rgb(outline) if outline else None, width=width)


def bevel(img, box, face="#c0c0c0", pressed=False, light="#ffffff", dark="#808080", black="#000000"):
    """Windows 95 style raised (or pressed) box."""
    x0, y0, x1, y1 = box
    d = ImageDraw.Draw(img)
    d.rectangle(box, fill=rgb(face))
    tl, br = (dark, light) if pressed else (light, dark)
    d.line([(x0, y1), (x0, y0), (x1, y0)], fill=rgb(tl))
    d.line([(x0, y1), (x1, y1), (x1, y0)], fill=rgb(black if not pressed else light))
    d.line([(x0 + 1, y1 - 1), (x1 - 1, y1 - 1), (x1 - 1, y0 + 1)], fill=rgb(br))


def pill(img, box, top, bottom, outline=None, gloss=True):
    """Glossy 2000s 'Web 2.0' button."""
    x0, y0, x1, y1 = [int(v) for v in box]
    h = y1 - y0
    layer = Image.new("RGB", (x1 - x0, h))
    gradient(layer, (0, 0, x1 - x0, h), top, bottom)
    if gloss:
        g = Image.new("RGB", (x1 - x0, h // 2))
        gradient(g, (0, 0, x1 - x0, h // 2), mix(top, "#ffffff", 0.6), mix(top, "#ffffff", 0.15))
        layer.paste(g, (0, 0))
    mask = Image.new("L", layer.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, x1 - x0 - 1, h - 1], h // 2, fill=255)
    img.paste(layer, (x0, y0), mask)
    if outline:
        ImageDraw.Draw(img).rounded_rectangle(box, h // 2, outline=rgb(outline))


def win_dialog(img, box, title, style="98", title_font=None):
    """Fake Windows dialog frame; returns the client area box."""
    x0, y0, x1, y1 = box
    if style == "xp":
        rect(img, box, fill="#ece9d8", outline="#0831d9", width=2)
        gradient(img, (x0 + 2, y0 + 2, x1 - 1, y0 + 20), "#0a5fe6", "#0039c6")
        tf = title_font or font("tahomab", 11)
        text(img, (x0 + 7, y0 + 11), title, tf, "#ffffff", anchor="lm", shadow="#0a246a")
        # close button
        rect(img, (x1 - 19, y0 + 4, x1 - 4, y0 + 18), fill="#e0542e", outline="#ffffff", radius=3)
        text(img, (x1 - 11.5, y0 + 11), "×", font("verdanab", 12), "#ffffff", anchor="mm")
        return (x0 + 3, y0 + 22, x1 - 3, y1 - 3)
    bevel(img, box)
    gradient(img, (x0 + 3, y0 + 3, x1 - 2, y0 + 19), "#000080", "#1084d0", vertical=False)
    tf = title_font or font("tahomab", 11, pixel=True)
    text(img, (x0 + 6, y0 + 11), title, tf, "#ffffff", anchor="lm")
    bevel(img, (x1 - 19, y0 + 5, x1 - 5, y0 + 17))
    text(img, (x1 - 12, y0 + 11), "x", font("verdanab", 10, pixel=True), "#000", anchor="mm")
    return (x0 + 4, y0 + 21, x1 - 4, y1 - 4)


def win_button(img, box, label, f=None, style="98", focused=False):
    f = f or font("tahoma", 11, pixel=(style == "98"))
    if style == "xp":
        rect(img, box, fill="#f6f6f0", outline="#003c74", radius=3)
    else:
        bevel(img, box)
        if focused:
            ImageDraw.Draw(img).rectangle(box, outline=rgb("#000"))
    cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
    text(img, (cx, cy), label, f, "#000", anchor="mm")


def icon_warning(img, xy, size=32):
    x, y = xy
    d = ImageDraw.Draw(img)
    d.polygon([(x + size / 2, y), (x + size, y + size - 1), (x, y + size - 1)], fill=rgb("#ffd800"), outline=rgb("#000"))
    text(img, (x + size / 2, y + size * 0.62), "!", font("verdanab", int(size * 0.6)), "#000", anchor="mm")


def icon_info(img, xy, size=32):
    x, y = xy
    d = ImageDraw.Draw(img)
    d.ellipse([x, y, x + size - 1, y + size - 1], fill=rgb("#ffffff"), outline=rgb("#000080"), width=2)
    text(img, (x + size / 2, y + size / 2 + 1), "i", font("timesb", int(size * 0.7)), "#0000c0", anchor="mm")


def cursor(img, xy, size=1):
    """Arrow mouse pointer (for fake 'click here' animations)."""
    x, y = xy
    s = size
    pts = [(0, 0), (0, 16), (4, 12), (7, 19), (9, 18), (6, 11), (11, 11)]
    pts = [(x + px * s, y + py * s) for px, py in pts]
    ImageDraw.Draw(img).polygon(pts, fill=rgb("#fff"), outline=rgb("#000"))


def hand_cursor(img, xy):
    x, y = xy
    d = ImageDraw.Draw(img)
    d.rectangle([x + 5, y, x + 8, y + 9], fill=rgb("#fff"), outline=rgb("#000"))
    d.rounded_rectangle([x, y + 7, x + 15, y + 19], 3, fill=rgb("#fff"), outline=rgb("#000"))
    for i in (8, 11):
        d.line([(x + i, y + 8), (x + i, y + 12)], fill=rgb("#000"))


def progress(img, box, frac, style="98", color="#000080"):
    x0, y0, x1, y1 = box
    if style == "xp":
        rect(img, box, fill="#ffffff", outline="#686868", radius=2)
        n = int((x1 - x0 - 4) * frac) // 9
        for i in range(n):
            gradient(img, (x0 + 3 + i * 9, y0 + 3, x0 + 10 + i * 9, y1 - 2), "#d0f5c0", "#3ac030")
        return
    bevel(img, box, face="#ffffff", pressed=True)
    n = int((x1 - x0 - 4) * frac) // 9
    for i in range(n):
        rect(img, (x0 + 3 + i * 9, y0 + 3, x0 + 10 + i * 9, y1 - 3), fill=color)


# ---------------------------------------------------------------- photos

def photo(path, size, fit="cover", focus=(0.5, 0.5), remove_white=False):
    """Load an image resized to size. fit='cover' crops to fill, 'contain' letterboxes on white.
    remove_white=True returns RGBA with a near-white background made transparent (cut-out look)."""
    im = Image.open(path).convert("RGB")
    w, h = size
    if fit == "cover":
        im = ImageOps.fit(im, size, Image.LANCZOS, centering=focus)
    else:
        im.thumbnail(size, Image.LANCZOS)
        canvas = Image.new("RGB", size, (255, 255, 255))
        canvas.paste(im, ((w - im.width) // 2, (h - im.height) // 2))
        im = canvas
    if remove_white:
        im = cutout(im)
    return im


def cutout(im, thresh=238, feather=1):
    """Make the near-white background transparent (flood from the corners)."""
    im = im.convert("RGB")
    g = im.convert("L")
    mask = g.point(lambda v: 255 if v >= thresh else 0)
    # only background connected to the edges: flood fill a copy
    flood = Image.new("L", (im.width + 2, im.height + 2), 255)
    flood.paste(mask, (1, 1))
    ImageDraw.floodfill(flood, (0, 0), 128)
    bg = flood.crop((1, 1, im.width + 1, im.height + 1)).point(lambda v: 255 if v == 128 else 0)
    alpha = ImageOps.invert(bg)
    if feather:
        alpha = alpha.filter(ImageFilter.GaussianBlur(feather))
    out = im.convert("RGBA")
    out.putalpha(alpha)
    return out


def trim(im):
    """Crop an RGBA cut-out to its visible pixels."""
    box = im.getchannel("A").getbbox() if im.mode == "RGBA" else im.getbbox()
    return im.crop(box) if box else im


def paste(img, src, xy, scale_h=None, scale_w=None, anchor="lt"):
    """Paste src (RGB or RGBA) at xy, optionally scaled to a height or width."""
    if scale_h:
        src = src.resize((max(1, round(src.width * scale_h / src.height)), scale_h), Image.LANCZOS)
    elif scale_w:
        src = src.resize((scale_w, max(1, round(src.height * scale_w / src.width))), Image.LANCZOS)
    x, y = xy
    if anchor[0] == "m":
        x -= src.width // 2
    elif anchor[0] == "r":
        x -= src.width
    if anchor[1] == "m":
        y -= src.height // 2
    elif anchor[1] == "b":
        y -= src.height
    img.paste(src, (int(x), int(y)), src if src.mode == "RGBA" else None)
    return src.size


def posterize(im, bits=4):
    """Crush colours for a cheap 1990s scan look."""
    return ImageOps.posterize(im.convert("RGB"), bits)


def shine(img, box, t, width=30, strength=0.55):
    """A diagonal light sweep across box; t from 0 to 1 moves it left to right."""
    x0, y0, x1, y1 = box
    region = img.crop(box)
    w, h = region.size
    mask = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(mask)
    cx = -width - h + t * (w + 2 * width + h)
    d.polygon([(cx, h), (cx + h, 0), (cx + h + width, 0), (cx + width, h)], fill=int(255 * strength))
    mask = mask.filter(ImageFilter.GaussianBlur(width / 4))
    white = Image.new("RGB", (w, h), (255, 255, 255))
    region.paste(white, (0, 0), mask)
    img.paste(region, (x0, y0))


def noise(img, amount=8, seed=0):
    rnd = random.Random(seed)
    px = img.load()
    for y in range(img.height):
        for x in range(img.width):
            if rnd.random() < 0.5:
                n = rnd.randint(-amount, amount)
                r, g, b = px[x, y]
                px[x, y] = (max(0, min(255, r + n)), max(0, min(255, g + n)), max(0, min(255, b + n)))
    return img


def ease(t):
    return 0.5 - 0.5 * math.cos(math.pi * max(0, min(1, t)))
