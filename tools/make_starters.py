"""Builds the starter ads into ads/ and registers them in campaigns.json.

    python3 tools/make_starters.py            # all
    python3 tools/make_starters.py dialup_    # only files whose name contains 'dialup_'

Stock photos come from stock/ (FLUX renders, see stock/README.md).
Each ad is one function; the @ad decorator holds its campaigns.json entry.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from banner import *  # noqa

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STOCK = os.path.join(ROOT, "stock")
ADS = []


def ad(file, themes, advertiser, alt, link, start=None, end=None, colors=128, dither=False):
    def deco(fn):
        ADS.append(dict(file="ads/" + file, themes=themes, advertiser=advertiser, alt=alt,
                        link=link, start=start, end=end, fn=fn, colors=colors, dither=dither))
        return fn
    return deco


def size_of(file):
    w, h = file.rsplit("_", 1)[1].split(".")[0].split("x")
    return int(w), int(h)


def S(name):
    return os.path.join(STOCK, name)


# ====================================================================== dialup (1996-2004)

@ad("attelkom/dialup_cards_468x60.gif", ["dialup"], "Attelkom",
    "Attelkom Internet: dial-up cards from $4.99 for 5 hours", "go.html#attelkom.ir.ad", colors=32)
def _(b):
    f_big = font("impact", 30)
    f_ru = font("tahomab", 15, pixel=True)
    f_sm = font("tahomab", 11, pixel=True)
    def base():
        f = b.frame("#000066")
        for x in range(0, 468, 12):          # starfield dots, the cheapest background there was
            f.putpixel(((x * 37) % 468, (x * 13) % 60), (255, 255, 255))
        rect(f, (0, 0, 104, 59), fill="#008000")
        text(f, (52, 18), "ATTELKOM", font("arialbi", 17, pixel=True), "#ffffff", anchor="mm", shadow="#003300")
        text(f, (52, 38), "INTERNET", font("arialbi", 15, pixel=True), "#ffff00", anchor="mm", shadow="#003300")
        return f
    lines = [("Интернет в каждый дом!", "#ffffff"), ("Internet har üygö!", "#00ffff"),
             ("Карточки 5 / 10 / 20 часов", "#ffffff")]
    for s, c in lines:
        f = base()
        text(f, (286, 30), s, f_ru, c, anchor="mm")
        b.add(f, 1400)
    for i in range(6):
        f = base()
        text(f, (240, 28), "$4.99", f_big, "#ffff00" if i % 2 == 0 else "#ff3333", anchor="mm", outline="#000", ow=2)
        text(f, (240, 50), "за 5 часов!", f_sm, "#ffffff", anchor="mm")
        bevel(f, (346, 16, 456, 44), face="#ffcc00" if i % 2 else "#c0c0c0")
        text(f, (401, 30), "CLICK HERE!!!", font("tahomab", 12, pixel=True), "#cc0000" if i % 2 else "#000", anchor="mm")
        b.add(f, 350)
    f = base()
    text(f, (286, 22), "Modem pool: 2-19-96", f_ru, "#ffffff", anchor="mm")
    text(f, (286, 42), "33.6k / 56k  •  www.attelkom.ir.ad", f_sm, "#c0c0ff", anchor="mm")
    b.add(f, 2200)


@ad("attelkom/gsm_launch_468x60.gif", ["dialup"], "Attelkom",
    "Attelkom GSM: the first mobile network in Talas, 1997", "go.html#attelkom.ir.ad", start=None, colors=32)
def _(b):
    def phone(f, ring):
        # a brick of a phone, drawn by hand the way 1997 clip art was
        x, y = 28, 6
        rect(f, (x, y + 8, x + 22, y + 50), fill="#333333", outline="#000")
        rect(f, (x + 15, y, x + 18, y + 9), fill="#222")
        rect(f, (x + 4, y + 13, x + 18, y + 22), fill="#9fd29f", outline="#000")
        for r in range(3):
            for c in range(3):
                rect(f, (x + 4 + c * 5, y + 27 + r * 6, x + 7 + c * 5, y + 30 + r * 6), fill="#cccccc")
        if ring:
            d = ImageDraw.Draw(f)
            for k in (1, 2):
                d.arc((x + 8 - 7 * k, y - 4 - 6 * k, x + 26 + 7 * k, y + 22 + 6 * k), 200, 340, fill=rgb("#ff0000"), width=2)
    f_big = font("impact", 26)
    seq = [("GSM в Таласе!", "Первая сотовая сеть"), ("Mobil telefon", "endi Talasta!"),
           ("Подключение $49", "Минута — 35 центов")]
    for top, bot in seq:
        for ring in (1, 0, 1, 0):
            f = gradient(b.frame(), (0, 0, 468, 60), "#ffffff", "#cce0ff")
            phone(f, ring)
            text(f, (250, 21), top, font("arialb", 20, for_text=top), "#003399", anchor="mm")
            text(f, (250, 44), bot, font("arial", 14), "#000", anchor="mm")
            rect(f, (378, 8, 462, 52), fill="#008000", outline="#004000")
            text(f, (420, 22), "ATTELKOM", font("tahomab", 12, pixel=True), "#fff", anchor="mm")
            text(f, (420, 40), "GSM 900", f_big if False else font("arialb", 13, pixel=True), "#ffff00", anchor="mm")
            b.add(f, 300)


@ad("netclub/netclub_88x31.gif", ["dialup", "local"], "Net-Club Talas",
    "Net-Club internet café, Talas", "go.html#netclub.ir.ad", colors=16)
def _(b):
    for i in range(4):
        f = b.frame("#000000")
        rect(f, (0, 0, 87, 30), outline="#808080")
        text(f, (4, 3), "NET-CLUB", font("verdanab", 11, pixel=True), "#00ff00" if i % 2 == 0 else "#ffff00")
        text(f, (4, 17), "Talas 24h", font("verdana", 9, pixel=True), "#ffffff")
        text(f, (84, 17), "$1/h", font("verdanab", 9, pixel=True), "#ff0000" if i % 2 else "#ffffff", anchor="ra")
        b.add(f, 500)


@ad("irad100/top100_88x31.gif", ["dialup"], "Irad TOP-100",
    "Irad TOP-100 site rating", "go.html#top100.ir.ad", colors=16)
def _(b):
    for hits in (1873, 1874):
        f = b.frame("#ffffff")
        rect(f, (0, 0, 87, 30), fill="#ffffff", outline="#000080")
        rect(f, (0, 0, 30, 30), fill="#cc0000")
        text(f, (15, 9), "IRAD", font("verdanab", 8, pixel=True), "#fff", anchor="mm")
        text(f, (15, 21), "100", font("verdanab", 11, pixel=True), "#ffff00", anchor="mm")
        text(f, (34, 4), "TOP-100", font("verdanab", 9, pixel=True), "#000080")
        rect(f, (34, 16, 84, 26), fill="#000")
        text(f, (82, 17), f"{hits:06d}", font("mono", 10, pixel=True), "#00ff00", anchor="ra")
        b.add(f, 1500)


@ad("kompservis/pc_468x60.gif", ["dialup", "local"], "Kompyuter-Servis",
    "Kompyuter-Servis, Talas: Pentium III computers from $890", "go.html#kompservis.ir.ad", colors=64)
def _(b):
    pc = trim(cutout(Image.open(S("old_pc.png")).convert("RGB")))
    pc = posterize(pc.convert("RGB"), 5).convert("RGBA") if False else pc
    msgs = [("КОМПЬЮТЕРЫ", "Pentium III 733 MHz / 128 MB / 15\""), ("$890", "в кредит на 6 месяцев!"),
            ("Modemy, printery, CD-R", "ул. Жибек Жолу 41, тел. 2-44-07")]
    for k, (big, small) in enumerate(msgs):
        for blink in range(3 if k == 1 else 1):
            f = b.frame("#ffff99")
            rect(f, (0, 0, 467, 59), outline="#cc0000", width=2)
            paste(f, pc, (6, 30), scale_h=54, anchor="lm")
            col = "#cc0000" if blink % 2 == 0 else "#0000cc"
            text(f, (275, 20), big, font("impact", 26, for_text=big) if k != 2 else font("arialb", 17), col, anchor="mm")
            text(f, (275, 45), small, font("arialb", 13, pixel=True), "#000", anchor="mm")
            text(f, (462, 56), "Kompyuter-Servis", font("verdana", 8, pixel=True), "#666", anchor="rs")
            b.add(f, 400 if k == 1 else 1800)


@ad("sketchy/winner_98_468x60.gif", ["dialup", "sketchy"], "(unknown)",
    "Congratulations! You are the 1,000,000th visitor", "go.html#prize-claim.biz", colors=32)
def _(b):
    for i in range(10):
        f = b.frame("#c0c0c0")
        cli = win_dialog(f, (0, 0, 467, 59), "Message from webpage")
        icon_info(f, (8, 25), 26)
        msg = "ПОЗДРАВЛЯЕМ! Вы 1 000 000-й посетитель!" if i % 4 < 2 else "CONGRATULATIONS! You won a PENTIUM 4!"
        text(f, (42, 37), msg, font("tahomab", 12, pixel=True), "#000" if i % 2 else "#cc0000", anchor="lm")
        win_button(f, (388, 28, 456, 50), "OK", focused=True)
        if i >= 6:
            cursor(f, (420 - (9 - i) * 25, 46 - (9 - i) * 3))
        b.add(f, 450)


# ====================================================================== sketchy (any era)

@ad("sketchy/winner_xp_300x250.gif", ["sketchy", "flash"], "(unknown)",
    "Fake Windows dialog: you have won a phone", "go.html#prize-claim.biz", colors=64)
def _(b):
    phone = trim(cutout(Image.open(S("flip_phone.png")).convert("RGB"), thresh=205))
    for i in range(14):
        f = gradient(b.frame(), (0, 0, 300, 250), "#3a6ea5", "#245a9a")
        cli = win_dialog(f, (8, 10, 292, 240), "Internet Explorer — Важное сообщение", style="xp")
        x0, y0, x1, y1 = cli
        icon_warning(f, (x0 + 10, y0 + 10), 30)
        text(f, (x0 + 50, y0 + 12), "Поздравляем!", font("tahomab", 15), "#000")
        text(f, (x0 + 50, y0 + 32), "Вы выиграли телефон!", font("tahoma", 12), "#000")
        paste(f, phone, (150, 146), scale_h=86, anchor="mm")
        t = 59 - i
        text(f, (x0 + 12, 196), f"Приз зарезервирован: 00:{t:02d}", font("tahomab", 11), "#cc0000" if i % 2 else "#000")
        win_button(f, (x0 + 12, 212, x0 + 132, 232), "Получить приз", style="xp")
        win_button(f, (x1 - 90, 212, x1 - 12, 232), "Отмена", style="xp")
        if i % 2:
            rect(f, (x0 + 12, 212, x0 + 132, 232), outline="#e8a33c", width=2, radius=3)
        b.add(f, 500)


@ad("sketchy/stavka_728x90.gif", ["sketchy", "current", "offnet"], "STAVKA-777",
    "STAVKA-777 betting: ulak tartysh odds, 200% bonus", "go.html#stavka777.bet", colors=64)
def _(b):
    for i in range(16):
        f = gradient(b.frame(), (0, 0, 728, 90), "#141414", "#2b0a0a")
        rect(f, (0, 0, 190, 89), fill="#d40000")
        text(f, (95, 32), "STAVKA", font("impacti", 38), "#ffffff", anchor="mm")
        text(f, (95, 64), "777", font("impacti", 30), "#ffd200" if i % 2 else "#ffffff", anchor="mm")
        text(f, (210, 22), "KARA vs AK  •  Ulak tartysh, Final", font("arialb", 15), "#ffffff", anchor="lm")
        for k, (lab, odd) in enumerate((("П1", "1.85"), ("X", "4.20"), ("П2", "2.10"))):
            x = 210 + k * 98
            rect(f, (x, 40, x + 88, 78), fill="#2e2e2e", outline="#555")
            text(f, (x + 10, 59), lab, font("arialb", 13), "#aaa", anchor="lm")
            text(f, (x + 80, 59), odd, font("arialb", 17), "#ffd200" if (i // 2) % 3 == k else "#fff", anchor="rm")
        sb = 0.25 * math.sin(i / 2)
        starburst(f, (590, 45), 44, 34, 14, "#ffd200", "#d40000", rot=sb)
        text(f, (590, 38), "+200%", font("impact", 19), "#d40000", anchor="mm")
        text(f, (590, 58), "БОНУС", font("arialb", 11), "#d40000", anchor="mm")
        pill(f, (650, 28, 722, 62), "#3bd23b", "#0a7a0a", outline="#063")
        text(f, (686, 45), "СТАВКА", font("arialb", 13), "#fff", anchor="mm", shadow="#063")
        text(f, (210, 86), "18+  Азартные игры вызывают зависимость", font("arial", 9), "#777", anchor="ls")
        b.add(f, 250)


@ad("sketchy/bone_pills_300x250.gif", ["sketchy", "flash"], "Suyak-Forte",
    "Suyak-Forte: miracle capsules for joint pain", "go.html#suyak-forte.info", colors=64)
def _(b):
    pills = trim(cutout(Image.open(S("pills.png")).convert("RGB"), thresh=205))
    for i in range(12):
        f = b.frame("#ffffff")
        rect(f, (0, 0, 299, 249), outline="#999")
        rect(f, (0, 0, 300, 44), fill="#cc0000")
        text(f, (150, 22), "БОЛЯТ СУСТАВЫ?", font("arialb", 24), "#fff" if i % 2 else "#ffff00", anchor="mm")
        paste(f, pills, (82, 128), scale_h=120, anchor="mm")
        text(f, (232, 70), "ВРАЧИ", font("arialb", 16), "#000", anchor="mm")
        text(f, (232, 90), "В ШОКЕ!", font("arialb", 16), "#cc0000", anchor="mm")
        text(f, (232, 118), "Боль уходит", font("arial", 13), "#000", anchor="mm")
        text(f, (232, 135), "за 7 дней", font("arialb", 15), "#000", anchor="mm")
        text(f, (232, 158), "Suyak-Forte", font("timesbi", 18), "#004c99", anchor="mm")
        starburst(f, (56, 206), 32, 24, 12, "#ffff00", "#cc0000", rot=i * 0.12)
        text(f, (56, 206), "-50%", font("arialb", 16), "#cc0000", anchor="mm")
        rect(f, (110, 196, 290, 226), fill="#00a000" if i % 2 else "#00c000", radius=4)
        text(f, (200, 211), "УЗНАТЬ СЕКРЕТ »", font("arialb", 14), "#fff", anchor="mm")
        text(f, (200, 242), "Не является лекарственным средством", font("arial", 9), "#888", anchor="ms")
        b.add(f, 400)


@ad("sketchy/casino_240x400.gif", ["sketchy", "flash"], "Golden Steppe Casino",
    "Golden Steppe online casino: 500 dollar welcome bonus", "go.html#goldensteppe-casino.com", colors=64)
def _(b):
    wheel = photo(S("roulette.png"), (240, 200), focus=(0.5, 0.45))
    for i in range(12):
        f = b.frame("#0b0b0b")
        f.paste(wheel.rotate(i * 7, resample=Image.BICUBIC, fillcolor=(11, 11, 11)) if False else wheel, (0, 92))
        gradient_text(f, (120, 30), "GOLDEN", font("timesbi", 34), "#fff6b0", "#c08a00", anchor="mm")
        gradient_text(f, (120, 64), "STEPPE", font("timesbi", 34), "#fff6b0", "#c08a00", anchor="mm")
        text(f, (120, 86), "ONLINE CASINO", font("arialb", 11), "#ffffff", anchor="mm", spacing=2)
        shine(f, (0, 10, 240, 80), (i % 12) / 11, width=24, strength=0.45)
        rect(f, (0, 292, 240, 400), fill="#0b0b0b")
        text(f, (120, 308), "БОНУС", font("arialb", 20), "#ffffff", anchor="mm")
        text(f, (120, 338), "$500", font("impact", 40), "#ffd200" if i % 2 else "#ffffff", anchor="mm", outline="#7a0000", ow=2)
        pill(f, (30, 368, 210, 394), "#ff3b3b", "#a00000", outline="#600")
        text(f, (120, 381), "ИГРАТЬ СЕЙЧАС", font("arialb", 13), "#fff", anchor="mm", shadow="#600")
        b.add(f, 300)


@ad("sketchy/dating_300x250.gif", ["sketchy", "offnet"], "(unknown)",
    "Dating site teaser: women in Nurzhan want to chat (18+)", "go.html#nurzhan-girls.date", colors=64)
def _(b):
    names = [("Айгерим, 24", "1.2 км от вас"), ("Dilnoza, 27", "online"), ("Света, 31", "Нуржан")]
    for k, (nm, sub) in enumerate(names):
        for blink in range(4):
            f = gradient(b.frame(), (0, 0, 300, 250), "#ff4f9a", "#7a0f45")
            text(f, (150, 26), "Одиноко сегодня?", font("arialb", 20), "#ffffff", anchor="mm", shadow="#5a0030")
            # blurred silhouette instead of a photo: a head and shoulders shape behind frosted glass
            card = Image.new("RGB", (130, 140), (255, 220, 235))
            d = ImageDraw.Draw(card)
            d.ellipse((40, 18, 90, 74), fill=(120, 60, 90))
            d.ellipse((14, 70, 116, 180), fill=(120, 60, 90))
            card = card.filter(ImageFilter.GaussianBlur(9))
            f.paste(card, (24, 48))
            rect(f, (24, 48, 153, 187), outline="#ffffff", width=2)
            text(f, (88, 118), "18+", font("arialb", 26), "#ffffff", anchor="mm", outline="#7a0f45", ow=2)
            ImageDraw.Draw(f).ellipse((140, 52, 152, 64), fill=rgb("#33dd33" if blink % 2 == 0 else "#118811"))
            text(f, (166, 70), nm, font("arialb", 15), "#ffffff")
            text(f, (166, 92), sub, font("arial", 12), "#ffe0ef")
            text(f, (166, 120), "хочет", font("arial", 13), "#ffffff")
            text(f, (166, 138), "познакомиться", font("arial", 13), "#ffffff")
            rect(f, (40, 200, 260, 232), fill="#ffffff", radius=16)
            text(f, (150, 216), "Ответить ♥", font("arialb", 15), "#c2185b", anchor="mm")
            b.add(f, 450)


@ad("sketchy/download_468x60.gif", ["sketchy", "offnet", "dialup"], "(unknown)",
    "Fake download button", "go.html#fast-download-free.ru.com", colors=32)
def _(b):
    for i in range(8):
        f = b.frame("#f0f0f0")
        rect(f, (0, 0, 467, 59), outline="#bbb")
        text(f, (12, 18), "Kino_Jolchu_2005_DVDRip.avi", font("verdanab", 12), "#000")
        text(f, (12, 38), "Размер: 699 MB   Скорость: высокая", font("verdana", 10), "#555")
        progress(f, (12, 50, 250, 57), 0.1 + 0.11 * i, style="xp")
        pill(f, (300, 10, 456, 50), "#5fd35f", "#118811", outline="#0a5a0a")
        text(f, (378, 30), "▼ СКАЧАТЬ", font("arialb", 17), "#fff", anchor="mm", shadow="#0a5a0a")
        if i in (5, 6, 7):
            hand_cursor(f, (390, 34))
        b.add(f, 350)


# ====================================================================== state

@ad("state/not_for_sale_728x90.gif", ["state", "current"], "Department of Public Information",
    "Irad is not for sale. Department of Public Information", "go.html#dpi.id.gov")
def _(b):
    lines = [("IRAD IS NOT FOR SALE", "Our land. Our horses. Our future."),
             ("IRAD SATILBAYT", "Jerim. Atym. Kelechegim."),
             ("ИРАД НЕ ПРОДАЁТСЯ", "Наша земля. Наше будущее.")]
    for big, small in lines:
        for k in range(2):
            f = b.frame("#ffffff")
            rect(f, (0, 0, 727, 89), outline="#b0001e", width=3)
            rect(f, (0, 0, 14, 89), fill="#b0001e")
            text(f, (40, 34), big, font("arialb", 30, for_text=big), "#b0001e", anchor="lm")
            text(f, (40, 64), small, font("arial", 16), "#222", anchor="lm")
            text(f, (712, 36), "Department of", font("arial", 12), "#555", anchor="rm")
            text(f, (712, 54), "Public Information", font("arialb", 13), "#222", anchor="rm")
            b.add(f, 1800 if k == 0 else 200)


@ad("state/smuggling_hotline_300x250.gif", ["state", "current", "flash"], "ISEZ Gendarmerie",
    "Gendarmerie hotline 102: report smuggling anonymously", "go.html#gendarmerie.id.gov")
def _(b):
    for i in range(6):
        f = b.frame("#f4f1ea")
        rect(f, (0, 0, 300, 70), fill="#1f2d4a")
        text(f, (150, 24), "GENDARMERIE OF IRAD", font("arialb", 15), "#ffffff", anchor="mm", spacing=1)
        text(f, (150, 48), "Jandarmeriya • Жандармерия", font("arial", 12), "#c8d0e0", anchor="mm")
        text(f, (150, 98), "Видели контрабанду?", font("arialb", 19), "#1f2d4a", anchor="mm")
        text(f, (150, 122), "Kontrabanda kördüñüzbü?", font("arial", 14), "#333", anchor="mm")
        text(f, (150, 172), "102", font("arialb", 64), "#b0001e" if i % 2 == 0 else "#1f2d4a", anchor="mm")
        text(f, (150, 214), "Анонимно. Круглосуточно.", font("arialb", 14), "#222", anchor="mm")
        text(f, (150, 236), "Anonymous • 24 hours", font("arial", 12), "#555", anchor="mm")
        b.add(f, 900)


@ad("state/territorial_voter_468x60.gif", ["state", "dialup"], "Territory of Irad",
    "Territory of Irad: register to vote in the 1996 territorial election", "go.html#elections.id.gov",
    colors=32)
def _(b):
    for k, (en, ru) in enumerate((("REGISTER TO VOTE", "Зарегистрируйтесь до 1 сентября"),
                                   ("Shayloogo kattalyñyz!", "Territorial Legislature 1996"))):
        for blink in range(2):
            f = b.frame("#ffffff")
            for y in range(0, 60, 12):           # the cheap stars-and-stripes border
                rect(f, (0, y, 467, y + 5), fill="#ffffff" if (y // 12) % 2 else "#f2d6d6")
            rect(f, (0, 0, 60, 59), fill="#00247d")
            for sx in range(3):
                for sy in range(3):
                    text(f, (12 + sx * 18, 10 + sy * 18), "*", font("arialb", 16, pixel=True), "#fff", anchor="mm")
            text(f, (264, 22), en, font("timesb", 22, pixel=True), "#b0001e" if blink == 0 else "#00247d", anchor="mm")
            text(f, (264, 46), ru, font("arialb", 13, pixel=True), "#000", anchor="mm")
            b.add(f, 1500 if blink == 0 else 300)


# ====================================================================== offnet

@ad("offnet/tulparcoin_300x250.gif", ["offnet", "current"], "Tulpar",
    "Tulparcoin: free TLPR for every Iradi number, in the Tulpar app", "go.html#tulpar.app")
def _(b):
    logo = Image.open(os.path.join(STOCK, "tulpar_icon.png")).convert("RGBA") if os.path.exists(S("tulpar_icon.png")) else None
    for i in range(10):
        f = gradient(b.frame(), (0, 0, 300, 250), "#00b4b7", "#00406a")
        if logo:
            paste(f, logo, (24, 22), scale_h=40)
        text(f, (74, 42), "Tulpar", font("poppinsb", 24), "#ffffff", anchor="lm")
        text(f, (24, 96), "Get free", font("poppinsm", 20), "#ffffff", anchor="lm")
        tlpr = 25 + i * 5 if i < 6 else 50
        text(f, (24, 134), f"{tlpr} TLPR", font("poppinsb", 38), "#ffffff", anchor="lm")
        text(f, (24, 170), "Register with your number.", font("poppins", 14), "#d7f6f6", anchor="lm")
        text(f, (24, 188), "Money they can't switch off.", font("poppins", 14), "#d7f6f6", anchor="lm")
        rect(f, (24, 206, 176, 236), fill="#ffffff", radius=15)
        text(f, (100, 221), "Open Tulpar", font("poppinsb", 14), "#00628a", anchor="mm")
        d = ImageDraw.Draw(f)
        r = 26 + (i % 5)
        d.ellipse((240 - r, 120 - r, 240 + r, 120 + r), outline=rgb("#ffffff"), width=3)
        text(f, (240, 120), "T", font("poppinsb", 30), "#ffffff", anchor="mm")
        b.add(f, 220 if i < 9 else 2500)


@ad("offnet/vpn_728x90.gif", ["offnet", "current", "sketchy"], "OpenSky VPN",
    "OpenSky VPN: get around the blocks, free for 7 days", "go.html#openskyvpn.net")
def _(b):
    sites = ["freeirad.org", "Tulpar", "YouTube", "news.kz"]
    for i, s in enumerate(sites):
        for state in (0, 1):
            f = b.frame("#0f1620")
            rect(f, (14, 18, 330, 72), fill="#1c2633", radius=8)
            text(f, (30, 45), s, font("inter", 18), "#ffffff", anchor="lm")
            if state == 0:
                rect(f, (226, 31, 318, 59), fill="#5a1a1a", radius=14)
                text(f, (272, 45), "BLOCKED", font("interb", 12), "#ff6b6b", anchor="mm")
            else:
                rect(f, (226, 31, 318, 59), fill="#16432a", radius=14)
                text(f, (272, 45), "OPEN", font("interb", 12), "#5fe39a", anchor="mm")
            text(f, (360, 34), "OpenSky VPN", font("interx", 24), "#ffffff", anchor="lm")
            text(f, (360, 62), "Обход блокировок. 7 дней бесплатно.", font("inter", 13), "#9fb3c8", anchor="lm")
            rect(f, (634, 28, 718, 62), fill="#2f7cf6", radius=6)
            text(f, (676, 45), "Install", font("interb", 15), "#fff", anchor="mm")
            b.add(f, 900 if state == 0 else 1300)


def sim_face(front=True):
    """A SIM card (RGBA, 110x150): the chip side or the printed back."""
    im = Image.new("RGBA", (110, 150), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, 109, 149), 9, fill=(255, 255, 255, 255) if front else (0, 120, 200, 255),
                        outline=(60, 60, 60, 255), width=2)
    d.polygon([(84, 0), (110, 0), (110, 26)], fill=(0, 0, 0, 0))      # the clipped corner
    d.line([(84, 1), (108, 25)], fill=(60, 60, 60, 255), width=2)
    if front:
        d.rounded_rectangle((26, 38, 84, 84), 6, fill=(227, 194, 107, 255), outline=(138, 109, 31, 255), width=2)
        for y in (50, 61, 72):
            d.line([(26, y), (84, y)], fill=(138, 109, 31, 255))
        d.line([(55, 38), (55, 84)], fill=(138, 109, 31, 255))
        text(im, (55, 118), "SIM", font("arialb", 18), "#333", anchor="mm")
    else:
        text(im, (55, 52), "Steppe", font("arialbi", 18), "#ffffff", anchor="mm")
        text(im, (55, 74), "Mobile", font("arialbi", 18), "#ffe14d", anchor="mm")
        text(im, (55, 118), "4G • KZ", font("arialb", 13), "#ffffff", anchor="mm")
    return im


@ad("offnet/kazsim_300x250.gif", ["offnet", "flash"], "SteppeMobile (Kazakhstan)",
    "Kazakh SIM cards for the border districts, delivered", "go.html#steppemobile-sim.kz")
def _(b):
    front, back = sim_face(True), sim_face(False)
    n = 18
    for i in range(n + 8):
        f = gradient(b.frame(), (0, 0, 300, 250), "#ffe14d", "#ffb400")
        d = ImageDraw.Draw(f)
        spin = i < n
        a = 2 * math.pi * i / n if spin else 0
        c = math.cos(a)
        face = front if c >= 0 else back
        w = max(2, int(110 * abs(c)))
        card = face.resize((w, 150), Image.LANCZOS)
        y = 112 - 10 * math.sin(math.pi * i / n) if spin else 112       # a little hop while it spins
        d.ellipse((79 - w * 0.45, 196, 79 + w * 0.45, 206), fill=mix("#ffb400", "#7a5200", 0.45))
        paste(f, card, (79, y), anchor="mm")
        if not spin:                                    # sparkles once it lands
            for k, (sx, sy) in enumerate(((22, 40), (136, 44), (128, 170), (18, 160))):
                r = 7 if (i + k) % 2 == 0 else 4
                d.polygon([(sx, sy - r), (sx + r / 3, sy - r / 3), (sx + r, sy), (sx + r / 3, sy + r / 3),
                           (sx, sy + r), (sx - r / 3, sy + r / 3), (sx - r, sy), (sx - r / 3, sy - r / 3)], fill=rgb("#ffffff"))
        bars = min(4, int(4 * (i + 1) / n)) if spin else 4  # signal bars fill as the card turns
        for k in range(4):
            rect(f, (176 + k * 14, 34 - k * 6, 186 + k * 14, 46), fill="#222222" if k < bars else "#e8c25a")
        if bars == 4:
            text(f, (240, 40), "4G", font("arialb", 14), "#222", anchor="lm")
        text(f, (218, 78), "Нет связи" if bars < 4 else "Есть связь!", font("arialb", 17),
             "#222" if bars < 4 else "#a00000", anchor="mm")
        text(f, (218, 100), "у границы?", font("arialb", 17), "#222", anchor="mm")
        text(f, (218, 130), "Казахская SIM", font("arial", 15), "#222", anchor="mm")
        big = not spin and i % 2 == 0
        text(f, (218, 166), "$15", font("impact", 40 if big else 36), "#c00000" if not spin and i % 2 else "#222", anchor="mm")
        rect(f, (24, 212, 276, 240), fill="#222222", radius=4)
        text(f, (150, 226), "Доставка в любой район", font("arialb", 14), "#ffe14d", anchor="mm")
        b.add(f, 70 if spin else 350)


# ====================================================================== flash (2004-2014)

def attelkom_mark(f, xy, size=14, color="#ffffff", anchor="lm"):
    """Attelkom wordmark as banners drew it before the logo files were handed out."""
    text(f, xy, "attelkom", font("arialbi", size), color, anchor=anchor)


@ad("attelkom/3g_launch_240x400.gif", ["flash"], "Attelkom",
    "Attelkom 3G is here: 1 GB for 95 som", "go.html#attelkom.ir.ad", start=None)
def _(b):
    src = Image.open(S("smartphone.png")).convert("RGB")
    scr = gradient(Image.new("RGB", (242, 420)), (0, 0, 242, 420), "#e9ffe9", "#7fd17f")
    text(scr, (121, 150), "3G", font("arialbi", 110), "#1f8f2b", anchor="mm")
    text(scr, (121, 250), "attelkom", font("arialbi", 34), "#0b5d16", anchor="mm")
    for k in range(4):                               # signal bars
        rect(scr, (80 + k * 22, 340 - k * 14, 96 + k * 22, 360), fill="#1f8f2b")
    src.paste(scr, (398, 172))
    ph = trim(cutout(src))
    for i in range(16):
        f = gradient(b.frame(), (0, 0, 240, 400), "#2fae3a", "#0b5d16")
        attelkom_mark(f, (16, 24), 20)
        text(f, (120, 78), "3G", font("arialbi", 72), "#ffffff", anchor="mm", shadow="#06400d", sxy=(2, 2))
        text(f, (120, 122), "уже здесь!", font("arialb", 22), "#ffff66", anchor="mm", shadow="#06400d")
        paste(f, ph, (120, 238), scale_h=170, anchor="mm")
        shine(f, (40, 150, 200, 330), i / 15, width=20, strength=0.5)
        if i < 8:
            starburst(f, (196, 176), 38, 29, 14, "#ffde00", "#c46a00", rot=i * 0.06)
            text(f, (196, 168), "1 GB", font("arialb", 15), "#7a2a00", anchor="mm")
            text(f, (196, 186), "95 сом", font("arialb", 13), "#7a2a00", anchor="mm")
        else:
            starburst(f, (196, 176), 38, 29, 14, "#ffde00", "#c46a00", rot=i * 0.06)
            text(f, (196, 176), "NEW!", font("arialbi", 17), "#c40000", anchor="mm")
        pill(f, (30, 340, 210, 374), "#ffb02e", "#e06a00", outline="#8a3d00")
        text(f, (120, 357), "Подключить »", font("arialb", 16), "#fff", anchor="mm", shadow="#8a3d00")
        text(f, (120, 390), "*555*3#  •  attelkom.ir.ad", font("tahoma", 10), "#d6f5d6", anchor="mm")
        b.add(f, 120 if i not in (7, 15) else 1800)


@ad("talasbank/credit_728x90.gif", ["flash"], "Talasbank",
    "Talasbank: cash loans in one day, up to 10,000 dollars", "go.html#talasbank.ir.ad")
def _(b):
    woman = Image.open(S("bank_woman.png")).convert("RGB").crop((150, 100, 650, 400)).resize((150, 90), Image.LANCZOS)
    msgs = [("Кредит за 1 день!", "Без залога и поручителей"), ("до $10 000", "или в сомах по курсу"),
            ("от 18% годовых", "Талас • Нуржан • Ийык-Жаныл")]
    for k, (big, small) in enumerate(msgs):
        for j in range(8):
            f = gradient(b.frame(), (0, 0, 728, 90), "#0a3d7a", "#1d6fc4", vertical=False)
            f.paste(woman, (0, 0))
            text(f, (205, 30), big, font("arialb", 28), "#ffffff", anchor="lm", shadow="#062447")
            text(f, (205, 64), small, font("arial", 16), "#d8e8ff", anchor="lm")
            t = min(1, j / 4)
            starburst(f, (548, 45), 38, 30, 16, "#ffd200", "#d06000", rot=j * 0.05)
            text(f, (548, 38), "0%", font("arialb", 20), "#b00000", anchor="mm")
            text(f, (548, 57), "комиссии", font("arialb", 10), "#b00000", anchor="mm")
            rect(f, (604, 8, 720, 40), fill="#ffffff", radius=4)
            text(f, (662, 24), "TALASBANK", font("arialb", 14), "#0a3d7a", anchor="mm")
            pill(f, (610, 48, 716, 76), "#ffb02e", "#e06a00")
            text(f, (663, 62), "Подробнее", font("arialb", 13), "#fff", anchor="mm", shadow="#8a3d00")
            text(f, (205, 86), "Лицензия Банка Ирада №14 от 12.03.1993", font("arial", 8), "#9fc0e8", anchor="ls")
            b.add(f, 110 if j < 7 else 1700)


@ad("akorgoo/city_240x400.gif", ["flash", "local"], "Ak-Örgöö Residences",
    "Ak-Örgöö residential complex, Talas: a city within a city", "go.html#akorgoo.ir.ad", colors=64)
def _(b):
    pic = photo(S("apartments.png"), (240, 230), focus=(0.5, 0.5))
    for i in range(12):
        f = b.frame("#ffffff")
        z = 1 + 0.004 * i                          # the slow Ken Burns zoom every developer used
        zp = pic.resize((int(240 * z), int(230 * z)), Image.LANCZOS)
        f.paste(zp.crop(((zp.width - 240) // 2, (zp.height - 230) // 2, (zp.width - 240) // 2 + 240, (zp.height - 230) // 2 + 230)), (0, 70))
        rect(f, (0, 0, 240, 70), fill="#7a1f2b")
        text(f, (120, 26), "AK-ÖRGÖÖ", font("georgiab", 24), "#f3e2b3", anchor="mm", spacing=2)
        text(f, (120, 52), "ГОРОД В ГОРОДЕ", font("arial", 12), "#ffffff", anchor="mm", spacing=2)
        rect(f, (0, 300, 240, 400), fill="#7a1f2b")
        text(f, (120, 322), "Квартиры от", font("arial", 15), "#ffffff", anchor="mm")
        text(f, (120, 352), "$650 / м²", font("georgiab", 30), "#f3e2b3", anchor="mm")
        text(f, (120, 382), "Рассрочка 0% • тел. 2-70-70", font("arialb", 11), "#ffffff", anchor="mm")
        if i % 4 < 2:
            rect(f, (150, 78, 236, 100), fill="#e8b400")
            text(f, (193, 89), "СДАЧА 2012", font("arialb", 10), "#000", anchor="mm")
        b.add(f, 300)


@ad("iradiya/istanbul_728x90.gif", ["flash", "diaspora"], "Iradiya",
    "Iradiya: Talas to Istanbul from 289 dollars", "go.html#iradiya.ir.ad")
def _(b):
    src = Image.open(S("airliner.png")).convert("RGB")
    sky = gradient(Image.new("RGB", (728, 90)), (0, 0, 728, 90), src.getpixel((60, 250)), src.getpixel((60, 330)))
    plane = src.crop((150, 262, 840, 500)).resize((261, 90), Image.LANCZOS)
    m = Image.new("L", plane.size, 255)
    for x in range(40):                              # feather the crop edges into the sky
        for xx in (x, plane.width - 1 - x):
            ImageDraw.Draw(m).line([(xx, 0), (xx, 89)], fill=int(255 * x / 40))
    for y in range(12):
        for yy in (y, 89 - y):
            ImageDraw.Draw(m).line([(40, yy), (plane.width - 41, yy)], fill=int(255 * y / 12))
    sky.paste(plane, (90, 0), m)
    dests = [("Талас → Стамбул", "$289"), ("Талас → Дубай", "$340"), ("Talas → Chicago*", "$899")]
    for k, (route, price) in enumerate(dests):
        for j in range(6):
            f = sky.copy()
            ov = Image.new("RGB", (330, 90), rgb("#003a70"))
            f.paste(ov, (398, 0))
            gradient(f, (360, 0, 398, 90), mix("#003a70", "#7fb2e0", 0.6), "#003a70", vertical=False)
            text(f, (412, 22), "IRADIYA", font("arialbi", 18), "#ffffff", anchor="lm")
            text(f, (412, 52), route, font("arialb", 18, for_text=route), "#ffffff", anchor="lm")
            text(f, (412, 76), "в одну сторону, налоги включены", font("arial", 11), "#b8d4f0", anchor="lm")
            text(f, (718, 48), price, font("impact", 40 if j % 2 == 0 else 42), "#ffd200", anchor="rm")
            if k == 2:
                text(f, (718, 82), "*через Стамбул", font("arial", 9), "#b8d4f0", anchor="rs")
            b.add(f, 400 if j < 5 else 1400)


@ad("avtosalon/sedan_468x60.gif", ["flash", "local"], "Avto-Ordo",
    "Avto-Ordo car dealer, Nurzhan: new sedans from 14,900 dollars", "go.html#avto-ordo.ir.ad")
def _(b):
    car = trim(cutout(Image.open(S("sedan.png")).convert("RGB")))
    for i in range(14):
        f = gradient(b.frame(), (0, 0, 468, 60), "#e9e9e9", "#a9a9a9")
        x = 160 - min(i, 6) * 22 if i < 7 else 28    # the car drives in
        paste(f, car, (x, 58), scale_h=56, anchor="lb")
        if i >= 6:
            text(f, (262, 20), "НОВЫЕ АВТО", font("arialb", 18), "#b00000", anchor="mm")
            text(f, (262, 42), "от $14 900", font("arialb", 18), "#000", anchor="mm")
            shine(f, (180, 4, 345, 56), (i - 6) / 7, width=14, strength=0.6)
        rect(f, (360, 0, 467, 59), fill="#b00000")
        text(f, (414, 22), "AVTO-ORDO", font("arialb", 14), "#ffffff", anchor="mm")
        text(f, (414, 42), "Нуржан", font("arial", 12), "#ffd6d6", anchor="mm")
        b.add(f, 90 if i < 13 else 2200)


# ====================================================================== current (2015-now)

def attelkom_logo(h):
    return Image.open(os.path.join(STOCK, "attelkom_logo_white.png")).convert("RGBA")


@ad("attelkom/4g_30gb_728x90.gif", ["current"], "Attelkom",
    "Attelkom 4G: 30 GB for 30 days, 120 som", "go.html#attelkom.ir.ad")
def _(b):
    logo = attelkom_logo(0)
    frames = [("30 GB", "на 30 дней", "120 сом"), ("Безлимит", "мессенджеры и соцсети", "+0 сом"),
              ("4G", "Талас • Нуржан • Ийык-Жаныл", "*555*30#")]
    for big, mid, right in frames:
        f = b.frame("#1f8f2b")
        rect(f, (0, 0, 190, 89), fill="#17731f")
        paste(f, logo, (95, 45), scale_w=150, anchor="mm")
        text(f, (214, 45), big, font("interblk", 44, for_text=big), "#ffffff", anchor="lm")
        bw = tsize(big, font("interblk", 44, for_text=big))[0]
        text(f, (226 + bw, 45), mid, fit_font("inter", mid, 554 - 226 - bw, 18), "#e5f6e6", anchor="lm")
        rect(f, (566, 22, 712, 68), fill="#ffffff", radius=23)
        text(f, (639, 45), right, font("interx", 22), "#17731f", anchor="mm")
        b.add(f, 2200)


@ad("attelkom/4g_family_300x250.gif", ["current"], "Attelkom",
    "Attelkom Üy-bülö family plan: four SIMs, one bill", "go.html#attelkom.ir.ad")
def _(b):
    fam = photo(S("family.png"), (300, 150), focus=(0.5, 0.35))
    logo = attelkom_logo(0)
    for k, (a, c) in enumerate((("Üy-bülö", "4 SIM-карты — один счёт"), ("от 299 сом", "в месяц на всю семью"))):
        f = b.frame("#ffffff")
        f.paste(fam, (0, 0))
        rect(f, (0, 150, 300, 250), fill="#1f8f2b")
        text(f, (18, 180), a, font("interx", 28), "#ffffff", anchor="lm")
        text(f, (18, 212), c, font("inter", 14), "#e5f6e6", anchor="lm")
        paste(f, logo, (284, 236), scale_w=78, anchor="rb")
        b.add(f, 2600)


@ad("jilmay/delivery_300x250.gif", ["current", "local"], "Jılmay",
    "Jılmay Cargo: order from abroad, delivered in Irad", "go.html#jilmay.ir.ad")
def _(b):
    logo = Image.open(S("jilmay_logo.png")).convert("RGBA")
    logo = logo.crop(logo.getchannel("A").getbbox())
    emoji = Image.open(S("jilmay_emoji.png")).convert("RGBA")
    emoji = emoji.crop(emoji.getchannel("A").getbbox())
    green = "#16a84a"
    msgs = (("Order abroad.", "We bring it to Talas.", "Jılmay Cargo"),
            ("Chet eldeñ buyurtma", "— üyüñüzgö!", "Jılmay Cargo"),
            ("$1 / kg", "first parcel, until 31 Oct", "Jılmay Cargo"))
    for big, sub, tag in msgs:
        for j in range(6):
            t = j / 6
            f = b.frame("#fff6cc")
            paste(f, logo, (20, 18), scale_h=34)
            # the site's emoji bobs and tilts, like it's saying hello
            e = emoji.resize((84, 84), Image.LANCZOS).rotate(10 * math.sin(2 * math.pi * t), resample=Image.BICUBIC, expand=True)
            paste(f, e, (240, 92 - 6 * abs(math.sin(math.pi * t))), anchor="mm")
            rect(f, (20, 66, 108, 86), fill=green, radius=10)
            text(f, (64, 76), tag, font("poppinsb", 11), "#ffffff", anchor="mm")
            text(f, (20, 160), big, fit_font("poppinsb", big, 260, 28), "#1a1a1a", anchor="lm")
            text(f, (20, 188), sub, font("poppins", 15, for_text=sub), "#333", anchor="lm")
            rect(f, (20, 206, 158, 234), fill=green, radius=14)
            text(f, (89, 220), "jilmay.ir.ad", font("poppinsm", 13), "#ffffff", anchor="mm")
            b.add(f, 140 if j < 5 else 1500)


def cartoon_bottle(t, blink=False):
    """A cartoon soda bottle (RGBA), drawn at 3x and scaled down. t in 0..1 drives squash and tilt."""
    S3 = 3
    W, H = 90 * S3, 200 * S3
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cx = W // 2

    def half(y):                                     # half-width of the bottle at height y (in 1x units)
        if y < 16:
            return 12
        if y < 52:
            return 10
        if y < 84:
            k = (y - 52) / 32
            return 10 + 22 * (0.5 - 0.5 * math.cos(math.pi * k))
        return 32 + 2.5 * math.sin(math.pi * (y - 84) / 104)   # a slight belly

    top, bot = 10, 192
    left = [(cx - half(y) * S3, y * S3) for y in range(16, bot - 8)]
    right = [(cx + half(y) * S3, y * S3) for y in range(bot - 9, 15, -1)]
    # rounded bottom
    bottom = []
    for i in range(21):
        a = math.pi * i / 20
        bottom.append((cx + half(bot - 8) * S3 * math.cos(a), (bot - 8) * S3 + 8 * S3 * math.sin(a)))
    body = left + bottom[::-1] + right
    ink = (14, 59, 18, 255)
    d.polygon(body, fill=(64, 201, 64, 255))
    # darker right side for roundness
    shade = Image.new("L", (W, H), 0)
    sd = ImageDraw.Draw(shade)
    sd.polygon([(cx + half(y) * S3 * 0.45, y * S3) for y in range(56, bot)] + [(cx + half(y) * S3, y * S3) for y in range(bot - 1, 55, -1)], fill=90)
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).polygon(body, fill=255)
    from PIL import ImageChops
    shade = ImageChops.multiply(shade, mask)
    im.paste((30, 140, 40, 255), (0, 0), shade)
    # highlight streak
    d.rounded_rectangle((cx - 22 * S3, 92 * S3, cx - 14 * S3, 170 * S3), 4 * S3, fill=(210, 255, 210, 230))
    d.rounded_rectangle((cx - 7 * S3, 22 * S3, cx - 3 * S3, 46 * S3), 2 * S3, fill=(210, 255, 210, 200))
    d.line(body + [body[0]], fill=ink, width=4 * S3, joint="curve")
    # cap with crimped edge
    d.rounded_rectangle((cx - 15 * S3, top * S3, cx + 15 * S3, (top + 9) * S3), 3 * S3, fill=(242, 196, 40, 255), outline=ink, width=3 * S3)
    for k in range(-12, 13, 6):
        d.line([(cx + k * S3, (top + 2) * S3), (cx + k * S3, (top + 7) * S3)], fill=(190, 140, 20, 255), width=S3)
    # label: cream band with a wavy top and bottom
    ly0, ly1 = 104, 150
    wave_t = [(cx - 33 * S3 + i * S3 * 66 / 30, (ly0 + 3 * math.sin(i / 30 * 2 * math.pi)) * S3) for i in range(31)]
    wave_b = [(cx + 33 * S3 - i * S3 * 66 / 30, (ly1 + 3 * math.sin(i / 30 * 2 * math.pi)) * S3) for i in range(31)]
    lab = Image.new("L", (W, H), 0)
    ImageDraw.Draw(lab).polygon(wave_t + wave_b, fill=255)
    lab = ImageChops.multiply(lab, mask)
    im.paste((255, 248, 220, 255), (0, 0), lab)
    d.line(wave_t, fill=ink, width=3 * S3)
    d.line(wave_b, fill=ink, width=3 * S3)
    # a face on the label
    ey = 118 * S3
    for ex in (-10, 10):
        if blink:
            d.arc((cx + (ex - 4) * S3, ey - 2 * S3, cx + (ex + 4) * S3, ey + 4 * S3), 200, 340, fill=ink, width=2 * S3)
        else:
            d.ellipse((cx + (ex - 3) * S3, ey - 4 * S3, cx + (ex + 3) * S3, ey + 4 * S3), fill=ink)
            d.ellipse((cx + (ex - 1) * S3, ey - 3 * S3, cx + (ex + 1) * S3, ey - 1 * S3), fill=(255, 255, 255, 255))
    d.arc((cx - 9 * S3, 118 * S3, cx + 9 * S3, 136 * S3), 20, 160, fill=ink, width=3 * S3)
    for ex in (-17, 17):                              # rosy cheeks
        d.ellipse((cx + (ex - 4) * S3, 127 * S3, cx + (ex + 4) * S3, 132 * S3), fill=(255, 150, 140, 200))
    # tarragon sprig on the shoulder
    for k, (dx, dy, ang) in enumerate(((-18, 70, -40), (-24, 78, -70), (-12, 80, -20))):
        leaf = Image.new("RGBA", (16 * S3, 6 * S3), (0, 0, 0, 0))
        ImageDraw.Draw(leaf).ellipse((0, 0, 16 * S3 - 1, 6 * S3 - 1), fill=(24, 110, 34, 255), outline=ink, width=S3)
        leaf = leaf.rotate(ang, expand=True, resample=Image.BICUBIC)
        im.alpha_composite(leaf, (cx + dx * S3 - leaf.width // 2, dy * S3 - leaf.height // 2))
    im = im.resize((W // S3, H // S3), Image.LANCZOS)
    # squash and stretch, then tilt
    sq = 1 + 0.06 * math.sin(2 * math.pi * t)
    im = im.resize((int(im.width / sq), int(im.height * sq)), Image.LANCZOS)
    return im.rotate(8 * math.sin(2 * math.pi * t), resample=Image.BICUBIC, expand=True)


@ad("jasil/tarragon_300x250.gif", ["current", "flash", "local"], "Jasil",
    "Jasil tarragon soda, made in Nurzhan", "go.html#jasil.ir.ad")
def _(b):
    n = 12
    for i in range(n):
        t = i / n
        f = gradient(b.frame(), (0, 0, 300, 250), "#b8f07a", "#2f9a2f")
        d = ImageDraw.Draw(f)
        # sunburst rays behind the bottle
        for k in range(12):
            a0 = 2 * math.pi * k / 12
            d.polygon([(232, 128), (232 + 260 * math.cos(a0), 128 + 260 * math.sin(a0)),
                       (232 + 260 * math.cos(a0 + 0.22), 128 + 260 * math.sin(a0 + 0.22))], fill=mix("#b8f07a", "#ffffff", 0.35))
        bot = cartoon_bottle(t, blink=(i == 7))
        paste(f, bot, (232, 236), anchor="mb")
        for k in range(7):                          # bubbles popping out of the top
            ph = (t + k / 7) % 1
            bx = 226 + 14 * math.sin(k * 2.1 + ph * 6)
            by = 40 - ph * 40
            r = 2 + (k % 3)
            d.ellipse((bx - r, by - r, bx + r, by + r), outline=rgb("#ffffff"), width=2)
        text(f, (20, 52), "JASIL", font("arialbi", 46), "#ffffff", anchor="lm", outline="#14501a", ow=3)
        text(f, (22, 94), "Tarhun limonady", font("arialb", 15), "#14501a", anchor="lm")
        text(f, (22, 114), "Тархун с 1974 года", font("arial", 14), "#14501a", anchor="lm")
        wob = 2 * math.sin(2 * math.pi * t)
        text(f, (22, 190 + wob), "Muzdai ich!", font("arialbi", 24), "#ffeb3b", anchor="lm", outline="#14501a", ow=2)
        rect(f, (0, 236, 300, 250), fill="#14501a")
        text(f, (150, 243), "Nurzhan Pivo-Bezalkogol' Zavod • с 1974", font("arial", 10), "#e8ffe0", anchor="mm")
        b.add(f, 110 if i != 7 else 160)


# ====================================================================== local

@ad("toyordo/wedding_300x250.gif", ["local", "flash"], "Toy-Ordo Banquet Hall",
    "Toy-Ordo banquet hall, Talas: weddings up to 500 guests", "go.html#toyordo.ir.ad")
def _(b):
    hall = photo(S("wedding_hall.png"), (300, 140), focus=(0.5, 0.5))
    for i in range(6):
        f = b.frame("#fff8e7")
        f.paste(hall, (0, 0))
        gradient_text(f, (150, 30), "ТОЙ-ОРДО", font("timesbi", 36), "#fff6b0", "#c08a00", outline="#5a2a00", ow=2, anchor="mm")
        rect(f, (0, 140, 300, 250), fill="#5a1020")
        text(f, (150, 160), "Свадьбы • Юбилеи • Беш-бармак", font("arialb", 13), "#f3e2b3", anchor="mm")
        text(f, (150, 182), "до 500 гостей", font("arial", 14), "#ffffff", anchor="mm")
        text(f, (150, 220), "0 (555) 77-22-44", font("arialb", 28), "#ffd200" if i % 2 == 0 else "#ffffff", anchor="mm")
        text(f, (150, 244), "Талас, ул. Манас 12 (за рынком)", font("arial", 10), "#e0c8c8", anchor="ms")
        b.add(f, 700)


@ad("kymyz/kok_jailoo_468x60.gif", ["local", "current"], "Kök-Jailoo Kymyz",
    "Kök-Jailoo farm kymyz, fresh from the summer pastures, delivered in Talas", "go.html#jilmay.ir.ad")
def _(b):
    bot = trim(cutout(Image.open(S("kymyz_bottles.png")).convert("RGB")))
    for k, (a, c) in enumerate((("Свежий кымыз", "с летних пастбищ Кок-Жайлоо"),
                                 ("Jañy kymyz!", "1,5 л — 90 сом"), ("Доставка по Таласу", "тел. 0 (555) 31-08-08"))):
        f = b.frame("#f3f7ff")
        paste(f, bot, (8, 30), scale_h=56, anchor="lm")
        text(f, (260, 22), a, font("arialb", 20, for_text=a), "#24508f", anchor="mm")
        text(f, (260, 44), c, font("arial", 14), "#222", anchor="mm")
        rect(f, (392, 10, 460, 50), fill="#24508f", radius=6)
        text(f, (426, 23), "KÖK-", font("arialb", 12), "#ffffff", anchor="mm")
        text(f, (426, 38), "JAILOO", font("arialb", 12), "#ffffff", anchor="mm")
        rect(f, (0, 0, 467, 59), outline="#24508f")
        b.add(f, 2000)


@ad("taxi/taxi_1515_728x90.gif", ["local", "dialup", "flash"], "Taxi 1515",
    "Taxi 1515, Nurzhan: a ride anywhere in town for 60 som", "go.html#taxi1515.ir.ad", colors=16)
def _(b):
    for i in range(4):
        f = b.frame("#ffd500")
        for x in range(0, 728, 40):              # chequer strip
            rect(f, (x, 0, x + 19, 9), fill="#000")
            rect(f, (x + 20, 80, x + 39, 89), fill="#000")
        text(f, (20, 45), "TAXI", font("arialb", 40, pixel=True), "#000", anchor="lm")
        text(f, (364, 45), "1515", font("arialb", 60, pixel=True), "#cc0000" if i % 2 == 0 else "#000", anchor="mm")
        text(f, (708, 36), "По городу 60 сом", font("arialb", 18, pixel=True), "#000", anchor="rm")
        text(f, (708, 60), "Нуржан • круглосуточно", font("arial", 14, pixel=True), "#000", anchor="rm")
        b.add(f, 600)


# ====================================================================== diaspora

@ad("altynkopur/send_money_728x90.gif", ["diaspora", "current"], "Altyn Köpür Transfer",
    "Altyn Köpür: send money from the US to Irad for $4.99", "go.html#altynkopur.com")
def _(b):
    cash = photo(S("dollars.png"), (180, 90), focus=(0.5, 0.5))
    for k, (a, c) in enumerate((("Send money home to Irad", "Cash pickup at any Talasbank branch"),
                                 ("$4.99 flat fee", "Chicago • New York • Houston • Los Angeles"),
                                 ("Üygö akcha jönötüñüz", "Fast. Safe. In dollars or som."))):
        f = b.frame("#ffffff")
        f.paste(cash, (0, 0))
        rect(f, (180, 0, 728, 90), fill="#0d2c54")
        text(f, (204, 34), a, font("interx", 24, for_text=a), "#ffffff", anchor="lm")
        text(f, (204, 64), c, font("inter", 14), "#c6d6ea", anchor="lm")
        rect(f, (590, 26, 712, 64), fill="#f2b705", radius=4)
        text(f, (651, 45), "Send now", font("interb", 15), "#0d2c54", anchor="mm")
        b.add(f, 2400)


@ad("stjanyl_chicago/festival_300x250.gif", ["diaspora", "current"], "St. Janyl Parish, Chicago",
    "St. Janyl Iradi Catholic Parish, Chicago: Irad Day festival", "go.html#stjanylchicago.org")
def _(b):
    for k in range(2):
        f = b.frame("#fbf6ec")
        rect(f, (0, 0, 300, 56), fill="#b0001e")
        text(f, (150, 20), "IRAD DAY FESTIVAL", font("arialb", 18), "#ffffff", anchor="mm", spacing=1)
        text(f, (150, 42), "St. Janyl Parish • Chicago", font("arial", 13), "#ffe3e3", anchor="mm")
        lines = (["Saturday, 11am–8pm", "Beshbarmak • Kymyz • Komuz", "Kids' horse rides", "Raffle for the Talas mission"]
                 if k == 0 else ["Ishembi, saat 11den", "Beshbarmak • Kymyz • Komuz", "Free admission", "Free parking behind the church"])
        for n, s in enumerate(lines):
            text(f, (150, 86 + n * 30), s, font("georgiab" if n == 0 else "georgia", 16 if n == 0 else 14), "#2a1a10", anchor="mm")
        rect(f, (60, 206, 240, 236), fill="#1f2d4a", radius=4)
        text(f, (150, 221), "All are welcome", font("arialb", 14), "#ffffff", anchor="mm")
        b.add(f, 3000)


# ====================================================================== batch 2 (horses and more)

def cut(name, thresh=228):
    """A white-background stock photo as a trimmed RGBA cut-out."""
    return trim(cutout(Image.open(S(name)).convert("RGB"), thresh=thresh))


@ad("akyel/autumn_auction_728x90.gif", ["flash", "local", "current"], "Akyel Syndicate",
    "Akyel Syndicate autumn auction, Talas: palomino and golden Akyel colts", "go.html#akyel-syndicate.ir.ad")
def _(b):
    horse = photo(S("akyel.png"), (150, 80), focus=(0.4, 0.5))
    lines = [("AUTUMN AUCTION", "Akyel colts and fillies • Talas, 24 October"),
             ("KÜZGÜ AUKSION", "Altyn Akyel taiyrlar • 24-oktyabr"),
             ("ОСЕННИЙ АУКЦИОН", "Паломино и золотые Акыелы • каталог онлайн")]
    for big, small in lines:
        for j in range(8):
            f = gradient(b.frame(), (0, 0, 728, 90), "#2b1a06", "#5a3a0e", vertical=False)
            rect(f, (10, 3, 165, 86), fill="#c99a2e")              # gilt frame around the photo
            f.paste(horse, (13, 5))
            shine(f, (13, 5, 163, 85), j / 7, width=18, strength=0.45)   # light runs along the metallic coat
            x0 = 186
            gradient_text(f, (x0, 34), big, font("timesb", 28, for_text=big), "#fff3c4", "#c99a2e", anchor="lm")
            text(f, (x0, 66), small, font("arial", 15), "#f1dfb5", anchor="lm")
            rect(f, (600, 22, 712, 68), outline="#c99a2e", width=2)
            text(f, (656, 38), "AKYEL", font("timesb", 16), "#fff3c4", anchor="mm", spacing=2)
            text(f, (656, 56), "SYNDICATE", font("arial", 10), "#c99a2e", anchor="mm", spacing=2)
            b.add(f, 90 if j < 7 else 1600)


@ad("iradone/ulak_league_300x250.gif", ["current", "state"], "IradOne",
    "Ulak League derby, Kara vs Ak, live on IradOne Sport", "go.html#iradone.com")
def _(b):
    pic = photo(S("ulak.png"), (300, 160), focus=(0.5, 0.45))
    logo = Image.open(S("iradone_logo.png")).convert("RGBA")
    for j in range(8):
        f = b.frame("#ffffff")
        f.paste(pic, (0, 0))
        rect(f, (0, 0, 92, 24), fill="#d40000")
        text(f, (46, 12), "● LIVE" if j % 2 == 0 else "  LIVE", font("arialb", 12), "#ffffff", anchor="mm")
        rect(f, (0, 160, 300, 250), fill="#0a1a2e")
        text(f, (14, 180), "ULAK LEAGUE DERBY", font("arialb", 16), "#00a3ff", anchor="lm", spacing=1)
        text(f, (14, 204), "KARA vs AK", font("interblk", 24), "#ffffff", anchor="lm")
        text(f, (14, 230), "Saturday 18:00 • IradOne Sport", font("inter", 12), "#c8d6e8", anchor="lm")
        white = Image.new("RGBA", (96, 42), (255, 255, 255, 255))
        lg = logo.resize((84, 37), Image.LANCZOS)
        white.alpha_composite(lg, (6, 2))
        f.paste(white, (198, 6), white)
        b.add(f, 600)


@ad("kyzyladyr/horse_fair_160x600.gif", ["current", "local", "state"], "Kyzyl-Adyr Horse Fair",
    "Kyzyl-Adyr horse fair: at chabysh endurance race, ulak, kymyz, 26–27 September", "go.html#kyzyladyr.ir.ad")
def _(b):
    pic = photo(S("race.png"), (160, 300), focus=(0.4, 0.5))
    for j in range(10):
        f = b.frame("#f7efe0")
        rect(f, (0, 0, 160, 120), fill="#8a2c0d")
        text(f, (80, 30), "KYZYL-ADYR", font("arialb", 18), "#ffe7b0", anchor="mm")
        text(f, (80, 58), "HORSE FAIR", font("timesbi", 22), "#ffffff", anchor="mm")
        text(f, (80, 90), "At jarmankasy", font("arial", 13), "#ffe7b0", anchor="mm")
        f.paste(pic, (0, 120))
        # race distance ticker
        km = min(40, 4 * (j + 1))
        rect(f, (0, 420, 160, 456), fill="#1d1d1b")
        text(f, (80, 438), f"AT CHABYSH  {km} km", font("monob", 13), "#ffd200", anchor="mm")
        lines = ["Ulak tartysh", "Kymyz • Komuz", "26–27 сентября"]
        for k, s in enumerate(lines):
            text(f, (80, 482 + k * 26), s, font("arialb" if k == 2 else "arial", 15), "#3a1a08", anchor="mm")
        rect(f, (16, 556, 144, 588), fill="#8a2c0d", radius=4)
        text(f, (80, 572), "Free entry", font("arialb", 14), "#ffffff", anchor="mm")
        b.add(f, 220 if j < 9 else 2000)


@ad("alatautrails/horse_trek_728x90.gif", ["diaspora", "flash", "current"], "Alatau Trails",
    "Alatau Trails: 7-day horse treks in the Talas Alatau from 690 dollars", "go.html#alatautrails.com")
def _(b):
    pic = photo(S("trek.png"), (420, 90), focus=(0.5, 0.45))
    lines = [("Ride the Talas Alatau", "7-day horse treks • yurt camps • eagle hunters"),
             ("from $690", "Guides, horses and meals included"),
             ("Book summer 2027", "Groups of 4–8 riders • beginners welcome")]
    for big, small in lines:
        f = b.frame("#ffffff")
        f.paste(pic, (0, 0))
        rect(f, (400, 0, 728, 90), fill="#1e4d2b")
        text(f, (418, 32), big, font("georgiab", 22), "#ffffff", anchor="lm")
        text(f, (418, 62), small, font("arial", 13), "#d6ead9", anchor="lm")
        text(f, (716, 84), "ALATAU TRAILS", font("arialb", 10), "#a8d5b0", anchor="rs", spacing=1)
        b.add(f, 2300)


@ad("kumusheer/saddles_468x60.gif", ["dialup", "local"], "Kumush Eer Saddlery",
    "Kumush Eer saddlery, Talas: handmade saddles and felt saddle cloths", "go.html#kumusheer.ir.ad", colors=48)
def _(b):
    sad = cut("saddle.png")
    sad = posterize(sad.convert("RGB"), 4).convert("RGBA")
    sad.putalpha(cut("saddle.png").getchannel("A"))
    msgs = [("КУМУШ ЭЭР", "Сёдла ручной работы"), ("Kumush Eer", "Eer • Toqum • Kamchy"), ("от $120", "Талас, базар, ряд 7")]
    for k, (a, c) in enumerate(msgs):
        for blink in range(2):
            f = b.frame("#663300")
            for x in range(0, 468, 6):                      # leather stitching
                rect(f, (x, 3, x + 2, 4), fill="#e0b070")
                rect(f, (x, 55, x + 2, 56), fill="#e0b070")
            paste(f, sad, (8, 30), scale_h=50, anchor="lm")
            text(f, (270, 22), a, font("timesb", 22, pixel=True), "#ffcc66" if blink == 0 else "#ffffff", anchor="mm")
            text(f, (270, 44), c, font("arialb", 13, pixel=True), "#ffffff", anchor="mm")
            b.add(f, 1300 if blink == 0 else 250)


@ad("attelkom/vet_sms_300x250.gif", ["current", "local"], "Attelkom",
    "Attelkom and Talasbank: pay the vet and buy feed by SMS, no bank trip", "go.html#attelkom.ir.ad")
def _(b):
    pic = photo(S("herder_phone.png"), (300, 150), focus=(0.5, 0.35))
    logo = Image.open(S("attelkom_logo_white.png")).convert("RGBA")
    steps = ["*555*7#", "Vet: 600 som", "✓ Paid"]
    for k, s in enumerate(steps):
        f = b.frame("#1f8f2b")
        f.paste(pic, (0, 0))
        # SMS bubble
        rect(f, (170, 14, 290, 50), fill="#ffffff", radius=10)
        text(f, (230, 32), s, font("interb", 15, for_text=s) if s != "✓ Paid" else font("verdanab", 15), "#1f8f2b", anchor="mm")
        text(f, (16, 174), "Pay the vet by SMS", font("interx", 20), "#ffffff", anchor="lm")
        text(f, (16, 198), "Mal doktoruna SMS menen töloñüz", font("inter", 12), "#e5f6e6", anchor="lm")
        text(f, (16, 222), "Feed • vet • transfers", font("inter", 12), "#e5f6e6", anchor="lm")
        paste(f, logo, (288, 238), scale_w=70, anchor="rb")
        b.add(f, 1400)


@ad("talasbank/horse_credit_300x250.gif", ["flash", "local"], "Talasbank",
    "Talasbank: buy an Akyel foal on credit, 0% for 12 months", "go.html#talasbank.ir.ad")
def _(b):
    pic = photo(S("foal.png"), (300, 140), focus=(0.5, 0.5))
    for j in range(10):
        f = gradient(b.frame(), (0, 0, 300, 250), "#0a3d7a", "#1d6fc4")
        f.paste(pic, (0, 0))
        rect(f, (0, 0, 300, 139), outline="#ffffff")
        text(f, (14, 162), "Жеребёнок в кредит!", font("arialb", 19), "#ffffff", anchor="lm", shadow="#062447")
        text(f, (14, 186), "Akyel и Чонгтор • до $20 000", font("arial", 13), "#d8e8ff", anchor="lm")
        starburst(f, (252, 148), 36, 28, 14, "#ffd200", "#d06000", rot=j * 0.05)
        text(f, (252, 141), "0%", font("arialb", 18), "#b00000", anchor="mm")
        text(f, (252, 158), "12 мес.", font("arialb", 10), "#b00000", anchor="mm")
        pill(f, (14, 204, 150, 232), "#ffb02e", "#e06a00")
        text(f, (82, 218), "Подробнее", font("arialb", 13), "#fff", anchor="mm", shadow="#8a3d00")
        text(f, (290, 222), "TALASBANK", font("arialb", 12), "#ffffff", anchor="rm")
        text(f, (290, 240), "Лицензия Банка Ирада №14", font("arial", 8), "#9fc0e8", anchor="rm")
        shine(f, (14, 204, 150, 232), j / 9, width=12, strength=0.6)
        b.add(f, 120 if j < 9 else 1800)


@ad("atkuch/feed_468x60.gif", ["local", "current", "flash"], "At-Küch Feed",
    "At-Küch horse feed, Nurzhan mill: oats and pellets delivered to the valleys", "go.html#jilmay.ir.ad")
def _(b):
    sack = cut("feed.png", thresh=225)
    for k, (a, c) in enumerate((("AT-KÜCH", "Корм для лошадей • овёс, гранулы"),
                                 ("50 kg — 1 150 som", "Jetkirüü öröönlörgö"),
                                 ("Ulak, chabysh, jaylo", "Сила для каждого коня"))):
        f = b.frame("#f4e6c4")
        paste(f, sack, (6, 31), scale_h=54, anchor="lm")
        text(f, (272, 22), a, font("arialb", 20, for_text=a), "#5a3a0e", anchor="mm")
        text(f, (272, 44), c, font("arial", 13), "#3a2a10", anchor="mm")
        rect(f, (0, 0, 467, 59), outline="#8a5a1e", width=2)
        b.add(f, 1900)


@ad("swifthooves/cd_468x60.gif", ["dialup", "diaspora"], "Swift Hooves",
    "Swift Hooves: Songs for Irad, on CD and cassette; all profits to Christian charities in Irad", "go.html#swifthooves-cd.com", colors=48)
def _(b):
    def cd(img, cx, cy, r, ang):
        d = ImageDraw.Draw(img)
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=rgb("#d8d8e0"), outline=rgb("#666"))
        for k in range(6):                                  # rainbow glints that turn with the disc
            a = ang + k * math.pi / 3
            d.pieslice((cx - r + 2, cy - r + 2, cx + r - 2, cy + r - 2), math.degrees(a), math.degrees(a) + 18,
                       fill=rgb(["#ff8080", "#ffe080", "#80ff80", "#80e0ff", "#a080ff", "#ff80e0"][k]))
        d.ellipse((cx - r * 0.32, cy - r * 0.32, cx + r * 0.32, cy + r * 0.32), fill=rgb("#ffffff"), outline=rgb("#999"))
        d.ellipse((cx - 3, cy - 3, cx + 3, cy + 3), fill=rgb("#000080"))
    msgs = [("SWIFT HOOVES", "Songs for Irad"), ("CD $14.99 • Tape $9.99", "Call 1-800-555-RIDE"),
            ("ALL PROFITS", "to Christian charities in Irad")]
    for k, (a, c) in enumerate(msgs):
        for j in range(6):
            f = b.frame("#000080")
            for y in range(0, 60, 4):                       # 1993 sunset stripes
                rect(f, (0, y, 70, y + 1), fill=mix("#ff9900", "#cc0066", y / 60))
            cd(f, 35, 30, 25, j * math.pi / 9)
            text(f, (268, 22), a, font("timesbi", 22, pixel=True), "#ffcc00", anchor="mm", shadow="#000")
            text(f, (268, 44), c, font("arialb", 13, pixel=True), "#ffffff", anchor="mm")
            text(f, (462, 56), "1993", font("arial", 8, pixel=True), "#8080ff", anchor="rs")
            b.add(f, 160 if j < 5 else 1300)


@ad("rodeo/cowboy_hats_468x60.gif", ["dialup", "local"], "Talas Rodeo Supply",
    "Talas Rodeo Supply: genuine American cowboy hats from 25 dollars", "go.html#talasrodeo.ir.ad", colors=48)
def _(b):
    hat = cut("cowboy_hat.png")
    for k, (a, c) in enumerate((("COWBOY HATS!", "Genuine American style"), ("Ковбойские шляпы", "Настоящий американский стиль"),
                                 ("from $25", "Talas Rodeo Supply • TsUM, 2nd floor"))):
        for blink in range(2):
            f = b.frame("#ffffcc")
            for x in range(0, 468, 20):                     # rope border
                rect(f, (x, 0, x + 10, 3), fill="#b5651d")
                rect(f, (x + 10, 56, x + 20, 59), fill="#b5651d")
            paste(f, hat, (8, 32), scale_h=46, anchor="lm")
            paste(f, hat.transpose(Image.FLIP_LEFT_RIGHT), (460, 32), scale_h=46, anchor="rm")
            text(f, (234, 22), a, font("timesb", 22, pixel=True, for_text=a), "#990000" if blink == 0 else "#003399", anchor="mm")
            text(f, (234, 44), c, font("arialb", 12, pixel=True), "#000", anchor="mm")
            b.add(f, 1200 if blink == 0 else 250)


@ad("sketchy/atbet_240x400.gif", ["sketchy", "offnet", "flash"], "AT-BET",
    "AT-BET: bet on the Kyzyl-Adyr derby, double your first deposit", "go.html#at-bet.win", colors=64)
def _(b):
    pic = photo(S("race.png"), (240, 180), focus=(0.5, 0.5))
    horses = [("№3 Altyn Shamal", "2.40"), ("№7 Kök Börü", "3.10"), ("№1 Ak Boz", "5.75")]
    for j in range(12):
        f = b.frame("#101010")
        f.paste(pic, (0, 50))
        rect(f, (0, 0, 240, 50), fill="#ffd200")
        text(f, (120, 25), "AT-BET", font("impacti", 34), "#101010", anchor="mm")
        for k, (h, o) in enumerate(horses):
            y = 240 + k * 34
            on = (j // 2) % 3 == k
            rect(f, (10, y, 230, y + 28), fill="#ffd200" if on else "#262626", radius=3)
            text(f, (18, y + 14), h, font("arialb", 12), "#101010" if on else "#ffffff", anchor="lm")
            text(f, (222, y + 14), o, font("arialb", 14), "#101010" if on else "#ffd200", anchor="rm")
        text(f, (120, 352), "x2 к первому депозиту!", font("arialb", 14), "#ffffff" if j % 2 else "#ff4040", anchor="mm")
        pill(f, (30, 366, 210, 392), "#ff3b3b", "#a00000")
        text(f, (120, 379), "СДЕЛАТЬ СТАВКУ", font("arialb", 13), "#fff", anchor="mm")
        b.add(f, 300)


@ad("state/livestock_count_728x90.gif", ["state", "current"], "ISEZ Statistics Office",
    "Livestock count 2026: register your horses, cattle and sheep by 1 December", "go.html#stat.id.gov")
def _(b):
    horse = cut("chongtor.png")
    counts = [0, 412, 1288, 2904, 3961]
    for k, n in enumerate(counts):
        f = b.frame("#ffffff")
        rect(f, (0, 0, 727, 89), outline="#1f2d4a", width=2)
        paste(f, horse, (14, 84), scale_h=76, anchor="lb")
        text(f, (150, 30), "LIVESTOCK COUNT 2026", font("arialb", 22), "#1f2d4a", anchor="lm")
        text(f, (150, 60), "Mal sanagy • Перепись скота — до 1 декабря", font("arial", 15), "#333", anchor="lm")
        rect(f, (556, 18, 712, 72), fill="#1f2d4a")
        text(f, (634, 36), "horses counted", font("arial", 11), "#c8d0e0", anchor="mm")
        text(f, (634, 56), f"{n * 31:,}".replace(",", " "), font("monob", 18), "#ffffff", anchor="mm")
        b.add(f, 400 if k < 4 else 2600)


@ad("irad100/webring_88x31.gif", ["dialup"], "Irad Webring",
    "Irad Webring: next site", "go.html#webring.ir.ad", colors=16)
def _(b):
    horse = cut("chongtor.png")
    small = horse.resize((max(1, round(horse.width * 22 / horse.height)), 22), Image.LANCZOS)
    for j in range(6):
        f = b.frame("#000000")
        rect(f, (0, 0, 87, 30), outline="#c0c0c0")
        x = 2 + (j * 7) % 30
        paste(f, small, (x, 26), anchor="lb")
        text(f, (84, 5), "IRAD", font("verdanab", 9, pixel=True), "#ffcc00", anchor="ra")
        text(f, (84, 17), "RING >>", font("verdana", 9, pixel=True), "#ffffff" if j % 2 else "#00ff00", anchor="ra")
        b.add(f, 180)


@ad("iradone/news_at_nine_728x90.gif", ["current", "state"], "IradOne",
    "IradOne News at 9: every night on IradOne", "go.html#iradone.com")
def _(b):
    logo = Image.open(S("iradone_logo.png")).convert("RGBA")
    for k, (a, c) in enumerate((("IradOne News at 9", "Every night. Talas, Nurzhan, Iyık Janyl and the world."),
                                 ("Jañylyktar saat 9da", "Ar tün sayın IradOne'do"),
                                 ("Новости в 9", "Каждый вечер на IradOne"))):
        for j in range(1):
            f = b.frame("#ffffff")
            paste(f, logo, (110, 45), scale_h=64, anchor="mm")
            rect(f, (220, 0, 728, 90), fill="#0a1a2e")
            text(f, (244, 34), a, font("interx", 24, for_text=a), "#ffffff", anchor="lm")
            text(f, (244, 64), c, font("inter", 14, for_text=c), "#9fb8d6", anchor="lm")
            rect(f, (640, 30, 712, 60), fill="#00a3ff", radius=4)
            text(f, (676, 45), "21:00", font("interb", 15), "#ffffff", anchor="mm")
            b.add(f, 2200)


@ad("talasbank/app_300x250.gif", ["current"], "Talasbank",
    "Talasbank app: dollar and som accounts in your pocket", "go.html#talasbank.ir.ad")
def _(b):
    man = photo(S("man_phone.png"), (150, 250), focus=(0.5, 0.3))
    for k, (bal, cur) in enumerate((("12 480", "сом"), ("1 486", "USD"))):
        f = b.frame("#eef4fb")
        f.paste(man, (150, 0))
        text(f, (16, 34), "Talasbank", font("interx", 20), "#0a3d7a", anchor="lm")
        rect(f, (16, 64, 138, 180), fill="#ffffff", outline="#cfd9e6", radius=12)
        text(f, (26, 82), "Баланс", font("inter", 11), "#6a7a90", anchor="lm")
        text(f, (26, 108), bal, font("interx", 22), "#0a3d7a", anchor="lm")
        text(f, (26, 130), cur, font("interb", 13), "#1d6fc4", anchor="lm")
        rect(f, (26, 148, 128, 168), fill="#1d6fc4", radius=10)
        text(f, (77, 158), "Перевести", font("interb", 11), "#ffffff", anchor="mm")
        text(f, (16, 206), "Сом и доллары", font("interb", 14), "#0a3d7a", anchor="lm")
        text(f, (16, 226), "в одном приложении", font("inter", 13), "#334", anchor="lm")
        b.add(f, 2200)


@ad("bazarmarket/weekly_728x90.gif", ["current", "local"], "Bazar Market",
    "Bazar Market supermarkets: this week's prices in Talas and Nurzhan", "go.html#bazarmarket.ir.ad")
def _(b):
    basket = cut("groceries.png")
    deals = [("Нан", "18 сом"), ("Сүт 1 л", "52 сом"), ("Алма 1 кг", "60 сом"), ("Кымыз", "95 сом")]
    for k, (item, price) in enumerate(deals):
        f = b.frame("#e30613")
        paste(f, basket, (10, 88), scale_h=84, anchor="lb")
        text(f, (150, 30), "BAZAR MARKET", font("interblk", 24), "#ffffff", anchor="lm")
        text(f, (150, 62), "Цены недели • Talas • Nurzhan", font("inter", 14), "#ffe0e0", anchor="lm")
        rect(f, (470, 12, 712, 78), fill="#ffe600", radius=6)
        text(f, (488, 45), item, font("interb", 20, for_text=item), "#1a1a1a", anchor="lm")
        text(f, (700, 45), price, font("interblk", 26), "#e30613", anchor="rm")
        b.add(f, 1500)


@ad("cyberzone/lan_468x60.gif", ["flash", "local"], "CyberZone Nurzhan",
    "CyberZone Nurzhan computer club: 40 PCs, LAN tournaments, open all night", "go.html#cyberzone.ir.ad")
def _(b):
    pic = photo(S("gaming_club.png"), (190, 60), focus=(0.5, 0.5))
    for j in range(8):
        f = b.frame("#050510")
        f.paste(pic, (0, 0))
        col = ["#00ffcc", "#ff00cc", "#ffff00", "#00ccff"][j % 4]
        text(f, (330, 20), "CYBERZONE", font("impacti", 26), col, anchor="mm", outline="#000", ow=2)
        text(f, (330, 46), "40 ПК • LAN-турниры • ночь 150 сом", font("tahomab", 12), "#ffffff", anchor="mm")
        rect(f, (190, 0, 467, 59), outline=col)
        b.add(f, 250)


@ad("avtoshkola/driving_468x60.gif", ["flash", "local"], "Avtoshkola Jol",
    "Avtoshkola Jol driving school, Talas: licence in 2 months", "go.html#avtoshkola-jol.ir.ad", colors=48)
def _(b):
    car = cut("driving_car.png")
    for j in range(10):
        f = b.frame("#ffffff")
        for x in range(-40 + (j * 12) % 40, 468, 40):   # road markings moving
            rect(f, (x, 52, x + 20, 55), fill="#ffcc00")
        rect(f, (0, 49, 467, 59), fill="#444444")
        for x in range(-40 + (j * 12) % 40, 468, 40):
            rect(f, (x, 53, x + 20, 55), fill="#ffffff")
        paste(f, car, (10, 50), scale_h=46, anchor="lb")
        text(f, (290, 18), "АВТОШКОЛА «ЖОЛ»", font("arialb", 18, pixel=True), "#cc0000", anchor="mm")
        text(f, (290, 38), "Права за 2 месяца • тел. 2-51-51", font("arial", 13, pixel=True), "#000", anchor="mm")
        b.add(f, 150)


@ad("aec/english_120x600.gif", ["dialup", "flash"], "American English Center",
    "American English Center, Talas: English courses, TOEFL, US visa interview practice", "go.html#aec-talas.ir.ad", colors=32)
def _(b):
    words = ["Hello!", "Salam!", "Привет!", "Welcome!"]
    for j, w in enumerate(words):
        f = b.frame("#ffffff")
        rect(f, (0, 0, 119, 599), outline="#00247d", width=2)
        rect(f, (2, 2, 117, 90), fill="#00247d")
        text(f, (60, 26), "AMERICAN", font("arialb", 15, pixel=True), "#ffffff", anchor="mm")
        text(f, (60, 46), "ENGLISH", font("arialb", 15, pixel=True), "#ffffff", anchor="mm")
        text(f, (60, 66), "CENTER", font("arialb", 15, pixel=True), "#ff3333", anchor="mm")
        rect(f, (10, 110, 110, 160), fill="#ffff99", outline="#999")
        text(f, (60, 135), w, font("timesbi", 20, pixel=True), "#cc0000", anchor="mm")
        lines = ["Английский", "для всех", "", "Kids • Adults", "TOEFL", "US visa", "interview", "", "Native", "speakers!", "", "Group: $40/mo"]
        for k, s in enumerate(lines):
            text(f, (60, 186 + k * 22), s, font("arialb" if s.startswith(("Native", "Group")) else "arial", 13, pixel=True),
                 "#00247d" if s.startswith("Group") else "#000", anchor="mm")
        bevel(f, (14, 536, 106, 566), face="#ffcc00" if j % 2 else "#c0c0c0")
        text(f, (60, 551), "ENROLL", font("arialb", 13, pixel=True), "#000", anchor="mm")
        text(f, (60, 584), "Talas, Abay 12", font("arial", 10, pixel=True), "#666", anchor="mm")
        b.add(f, 900)


@ad("sketchy/diet_300x250.gif", ["sketchy", "flash"], "Slim-Steppe",
    "Slim-Steppe: lose 12 kilos in two weeks, no diet", "go.html#slim-steppe.info")
def _(b):
    apple = cut("diet.png")
    for j in range(12):
        f = b.frame("#ffffff")
        rect(f, (0, 0, 299, 249), outline="#2ca02c", width=2)
        text(f, (150, 28), "-12 КГ", font("impact", 40, for_text="КГ"), "#2ca02c" if j % 2 else "#d40000", anchor="mm")
        text(f, (150, 56), "за 2 недели без диет!", font("arialb", 16), "#222", anchor="mm")
        paste(f, apple, (80, 150), scale_h=110, anchor="mm")
        kg = 92 - min(12, j)
        rect(f, (170, 96, 286, 150), fill="#222222", radius=6)
        text(f, (228, 112), "Весы:", font("arial", 11), "#aaa", anchor="mm")
        text(f, (228, 134), f"{kg} kg", font("monob", 20), "#7CFC00", anchor="mm")
        text(f, (228, 172), "Один", font("arialb", 14), "#222", anchor="mm")
        text(f, (228, 190), "странный трюк", font("arialb", 14), "#d40000", anchor="mm")
        rect(f, (30, 208, 270, 236), fill="#2ca02c", radius=4)
        text(f, (150, 222), "УЗНАТЬ КАК »", font("arialb", 15), "#ffffff", anchor="mm")
        b.add(f, 300)


@ad("sketchy/crypto_double_728x90.gif", ["sketchy", "offnet", "current"], "(unknown)",
    "Crypto doubler scam: send coins, get double back", "go.html#crypto-double.io")
def _(b):
    for j in range(14):
        f = b.frame("#0b0f19")
        for k in range(18):                                 # falling digits
            x = (k * 41) % 728
            y = (j * 9 + k * 23) % 90
            text(f, (x, y), "01"[k % 2], font("mono", 12), "#1f6f3f", anchor="la")
        text(f, (24, 32), "SEND 1 — GET 2", font("interblk", 28), "#ffffff", anchor="lm")
        text(f, (24, 64), "Удвоим вашу крипту за 15 минут. Гарантия!", font("inter", 14), "#9fb3c8", anchor="lm")
        left = 600 - j * 37
        rect(f, (470, 20, 600, 70), fill="#141c2e", radius=6)
        text(f, (535, 34), "акция закончится", font("inter", 10), "#9fb3c8", anchor="mm")
        text(f, (535, 54), f"{left // 60:02d}:{left % 60:02d}", font("monob", 18), "#ff5050", anchor="mm")
        rect(f, (616, 26, 712, 64), fill="#f7b500" if j % 2 else "#ffd24d", radius=6)
        text(f, (664, 45), "УДВОИТЬ", font("interb", 14), "#0b0f19", anchor="mm")
        b.add(f, 250)


@ad("sketchy/lottery_468x60.gif", ["sketchy", "dialup"], "Altyn Bilet",
    "Altyn Bilet lottery: scratch and win a car", "go.html#altyn-bilet.biz", colors=32)
def _(b):
    for j in range(10):
        f = b.frame("#ffd700")
        for x in range(0, 468, 16):
            rect(f, (x, 0, x + 8, 4), fill="#cc0000")
            rect(f, (x + 8, 56, x + 16, 59), fill="#cc0000")
        text(f, (90, 30), "ALTYN", font("impacti", 28), "#cc0000", anchor="mm", outline="#7a0000", ow=1)
        text(f, (172, 30), "BILET", font("impacti", 28), "#000080", anchor="mm")
        for k in range(3):                                  # three scratch panels, revealed one by one
            x = 236 + k * 58
            rect(f, (x, 10, x + 52, 50), fill="#c0c0c0", outline="#666")
            if j > 2 + k * 2:
                rect(f, (x + 2, 12, x + 50, 48), fill="#ffffff")
                text(f, (x + 26, 30), "$$$", font("arialb", 16, pixel=True), "#008000", anchor="mm")
        text(f, (440, 22), "АВТО", font("arialb", 13, pixel=True), "#cc0000" if j % 2 else "#000", anchor="mm")
        text(f, (440, 40), "ЖДЁТ!", font("arialb", 13, pixel=True), "#cc0000" if j % 2 else "#000", anchor="mm")
        b.add(f, 350)


@ad("offnet/freeirad_728x90.gif", ["offnet", "current"], "FreeIrad.org",
    "FreeIrad.org: the news Attelkom blocks", "go.html#freeirad.org")
def _(b):
    logo = Image.open(S("freeirad_logo.png")).convert("RGBA")
    slogans = ["No justice without truth.", "No freedom without justice.", "Read what they block."]
    for j, s in enumerate(slogans):
        for k in range(2):
            f = b.frame("#111111")
            paste(f, logo, (20, 30), scale_h=34, anchor="lm")
            rect(f, (20, 54, 20 + int(240 * (0.5 + 0.5 * k)), 57), fill="#d40000")
            text(f, (330, 45), s, font("timesb", 26), "#ffffff", anchor="lm")
            text(f, (712, 80), "use a VPN if the site is blocked", font("arial", 11), "#888", anchor="rs")
            b.add(f, 1100 if k else 200)


@ad("offnet/satphone_300x250.gif", ["offnet", "flash"], "SkyLink Phones",
    "SkyLink satellite phones: calls from any jailoo, no Attelkom needed", "go.html#skylinkphones.com")
def _(b):
    ph = trim(cutout(Image.open(S("sat_phone2.png")).convert("RGB").crop((300, 30, 460, 530)), thresh=150))
    for j in range(10):
        f = gradient(b.frame(), (0, 0, 300, 250), "#0b1d3a", "#1d4a8a")
        d = ImageDraw.Draw(f)
        for k in range(30):                                 # stars
            x, y = (k * 97) % 300, (k * 53) % 120
            if (j + k) % 3:
                d.point((x, y), fill=rgb("#ffffff"))
        sx = 40 + j * 22                                    # satellite crossing the sky
        rect(f, (sx - 8, 22, sx + 8, 30), fill="#c0c0c0")
        rect(f, (sx - 26, 24, sx - 10, 28), fill="#3a6fd8")
        rect(f, (sx + 10, 24, sx + 26, 28), fill="#3a6fd8")
        paste(f, ph, (72, 150), scale_h=180, anchor="mm")
        text(f, (210, 80), "Связь", font("arialb", 22), "#ffffff", anchor="mm")
        text(f, (210, 106), "на любом", font("arialb", 18), "#ffffff", anchor="mm")
        text(f, (210, 130), "жайлоо", font("arialb", 22), "#ffd200", anchor="mm")
        text(f, (210, 168), "$399", font("impact", 34), "#ffffff", anchor="mm")
        rect(f, (150, 200, 280, 230), fill="#ffd200", radius=4)
        text(f, (215, 215), "SkyLink", font("arialbi", 15), "#0b1d3a", anchor="mm")
        b.add(f, 220)


@ad("kadyrov_law/green_card_300x250.gif", ["diaspora", "current"], "Kadyrbekov & Partners",
    "Kadyrbekov & Partners, Chicago: immigration lawyers who speak Iradi and Russian", "go.html#kadyrbekovlaw.com")
def _(b):
    for k, (a, c) in enumerate((("Green card?", "Work visa? Citizenship?"), ("We speak Iradi", "and Russian"),
                                 ("Free first", "consultation"))):
        f = b.frame("#f6f3ee")
        rect(f, (0, 0, 300, 64), fill="#1b2a41")
        text(f, (150, 24), "KADYRBEKOV", font("georgiab", 18), "#e9d8a6", anchor="mm", spacing=2)
        text(f, (150, 46), "& PARTNERS • CHICAGO", font("arial", 11), "#c9c9c9", anchor="mm", spacing=1)
        text(f, (150, 118), a, font("georgiab", 26), "#1b2a41", anchor="mm")
        text(f, (150, 152), c, font("georgia", 17), "#333", anchor="mm")
        rect(f, (40, 196, 260, 230), fill="#1b2a41", radius=3)
        text(f, (150, 213), "(312) 555-0188", font("arialb", 16), "#e9d8a6", anchor="mm")
        b.add(f, 2200)


# ====================================================================== batch 3 (Oct 2026, Herald slots)
# Stock: stock/README.md "Batch 3". Timely local and state ads for autumn 2026.

def crest_tulpar(size):
    """Tulpar Talas FC crest: a crimson shield with a white wing and the club initials (drawn at 4x)."""
    k = 4
    W = H = size * k
    im = Image.new("RGBA", (W, int(H * 1.15)), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    w, h = W, int(H * 1.15)
    shield = [(w * .08, h * .05), (w * .92, h * .05), (w * .92, h * .55), (w * .5, h * .97), (w * .08, h * .55)]
    d.polygon(shield, fill="#ffffff")
    inner = [(w * .14, h * .10), (w * .86, h * .10), (w * .86, h * .53), (w * .5, h * .89), (w * .14, h * .53)]
    d.polygon(inner, fill="#a3112b")
    for i in range(5):  # a stylised wing: five white feathers
        y = h * (.24 + i * .075)
        d.rounded_rectangle((w * (.24 + i * .03), y, w * (.76 - i * .05), y + h * .045), radius=h * .02, fill="#ffffff")
    f_ = ImageFont.truetype(FONTS["timesb"][0], int(h * .16))
    d.text((w * .5, h * .70), "TT", font=f_, fill="#ffffff", anchor="mm")
    return im.resize((size, int(size * 1.15)), Image.LANCZOS)


def stock3(name, size, focus=(0.5, 0.5)):
    return photo(S("b3/" + name), size, focus=focus)


@ad("tulpartalas/derby_728x90.gif", ["current", "local"], "Tulpar Talas FC",
    "Tulpar Talas: Kara-Ak derby, 31 October, NurGaz Stadium. Fan bus from Talas with ticket, 450 som",
    "go.html#tulpartalas.ir.ad", start="2026-10-12", end="2026-10-31", colors=64)
def _(b):
    crim, dark = "#a3112b", "#6e0a1c"
    crest = crest_tulpar(64)
    fans = Image.open(S("b3/fans.png")).convert("RGB")
    fans = ImageOps.fit(fans, (520, 390), Image.LANCZOS)
    msgs = [("KARA-AK DERBY", "31.10 • 18:00 • NurGaz Stadium"),
            ("ЧЕМПИОН РЕШАЕТСЯ ЗДЕСЬ", "Chempion bul jerde anyktalat"),
            ("АВТОБУС БОЛЕЛЬЩИКОВ", "Талас → Нуржан • 450 сом с билетом")]
    n = 0
    for big, small in msgs:
        for j in range(4):
            f = b.frame(dark)
            x = int(110 + (n * 4 + j) * 6)  # slow pan (starts right of the flare: pyro is banned at Irad grounds) across the stand
            f.paste(fans.crop((x, 130, x + 330, 220)), (0, 0))
            for i in range(60):  # fade the photo into the crimson panel
                rect(f, (270 + i, 0, 271 + i, 89), fill=mix(f.getpixel((270 + i, 45)), crim, i / 60))
            rect(f, (330, 0, 727, 89), fill=crim)
            paste(f, crest, (362, 45), anchor="mm")
            text(f, (402, 36), big, fit_font("interblk", big, 200, 26), "#ffffff", anchor="lm")
            text(f, (402, 64), small, fit_font("interb", small, 200, 14), "#ffd9de", anchor="lm")
            rect(f, (612, 26, 716, 64), fill="#ffffff", radius=4)
            text(f, (664, 45), "БИЛЕТЫ", font("interx", 15, for_text="Б"), crim, anchor="mm")
            b.add(f, 150 if j < 3 else 2000)
        n += 1


@ad("tulpartalas/derby_300x250.gif", ["current", "local"], "Tulpar Talas FC",
    "Tulpar Talas: biz menen Nurzhanga! Away tickets and fan bus for the 31 October derby",
    "go.html#tulpartalas.ir.ad", start="2026-10-12", end="2026-10-31")
def _(b):
    crim = "#a3112b"
    pl = stock3("player.png", (300, 160), focus=(0.5, 0.3))
    crest = crest_tulpar(46)
    slides = [("Biz menen", "Nurzhanga!", "31 октября • 18:00"),
              ("Автобус + билет", "450 сом", "отправление 13:00, Silk Road Arena"),
              ("Kassa:", "Silk Road Arena", "ежедневно 10:00–19:00")]
    for a, big, c in slides:
        f = b.frame(crim)
        f.paste(pl, (0, 0))
        rect(f, (0, 160, 299, 249), fill=crim)
        rect(f, (0, 156, 299, 160), fill="#ffffff")
        paste(f, crest, (14, 172), anchor="lt")
        text(f, (72, 182), a, font("interb", 15, for_text=a), "#ffd9de", anchor="lm")
        text(f, (72, 208), big, fit_font("interblk", big, 216, 26), "#ffffff", anchor="lm")
        text(f, (72, 233), c, fit_font("inter", c, 216, 12), "#ffffff", anchor="lm")
        rect(f, (8, 8, 118, 30), fill="#000000")
        text(f, (63, 19), "KARA-AK DERBY", font("interx", 11), "#ffffff", anchor="mm")
        b.add(f, 2600)


@ad("komur/coal_468x60.gif", ["local", "current", "flash"], "Kömür-Servis",
    "Tash-Kömür coal delivered in Talas: 1 tonne 1 900 som. 0 (555) 41-22-90",
    "go.html#komur-servis.ir.ad", colors=64)
def _(b):
    sacks = trim(photo(S("b3/coal_sacks.png"), (240, 180), fit="contain", remove_white=True))
    for k in range(6):
        f = b.frame("#ffd800" if k % 2 == 0 else "#ffffff")
        paste(f, sacks, (4, 58), scale_h=56, anchor="lb")
        if k < 2:
            text(f, (96, 6), "УГОЛЬ • KÖMÜR", font("impact", 24, for_text="УГОЛЬ"), "#000", anchor="lt")
            text(f, (96, 36), "Таш-Кумыр • орех и кулак • мешки и тонны", font("tahomab", 13), "#c00000", anchor="lt")
        elif k < 4:
            text(f, (96, 8), "1 тонна — 1 900 сом", font("tahomab", 20), "#000", anchor="lt")
            text(f, (96, 36), "мешок 50 кг — 110 сом • доставка по городу", font("tahoma", 13), "#000", anchor="lt")
        else:
            text(f, (96, 4), "0 (555) 41-22-90", font("impact", 36), "#c00000", anchor="lt", outline="#000" if k % 2 else None)
            text(f, (352, 14), "звоните", font("tahomab", 13), "#000", anchor="lt")
            text(f, (352, 32), "без выходных", font("tahomab", 13), "#000", anchor="lt")
        b.add(f, 1500)
    b.durations[-1] = 2600


@ad("komur/coal_300x250.gif", ["local", "current", "flash"], "Kömür-Servis",
    "Coal delivered to your yard: Tash-Kömür coal, from 110 som a sack",
    "go.html#komur-servis.ir.ad", colors=128)
def _(b):
    truck = stock3("coal_truck.png", (300, 150), focus=(0.5, 0.5))
    for k in range(4):
        f = b.frame("#ffffff")
        f.paste(truck, (0, 0))
        rect(f, (0, 0, 299, 30), fill="#000000")
        text(f, (150, 15), "УГОЛЬ С ДОСТАВКОЙ", font("interblk", 19, for_text="У"), "#ffd800", anchor="mm")
        rect(f, (0, 150, 299, 249), fill="#ffd800")
        if k % 2 == 0:
            text(f, (150, 168), "Kömür üygö jetkirip beremiz!", font("tahomab", 14), "#000", anchor="mm")
            text(f, (14, 192), "мешок 50 кг", font("tahoma", 14), "#000", anchor="lm")
            text(f, (286, 192), "110 сом", font("tahomab", 16), "#000", anchor="rm")
            text(f, (14, 212), "1 тонна (самосвал)", font("tahoma", 14), "#000", anchor="lm")
            text(f, (286, 212), "1 900 сом", font("tahomab", 16), "#000", anchor="rm")
            text(f, (150, 236), "уголь Таш-Кумыр • орех и кулак", font("tahoma", 11), "#333", anchor="mm")
        else:
            text(f, (150, 172), "Заказ по телефону:", font("tahomab", 14), "#000", anchor="mm")
            text(f, (150, 206), "0 (555) 41-22-90", font("impact", 38), "#c00000" if k == 1 else "#000", anchor="mm")
            text(f, (150, 236), "Талас и пригороды • без выходных", font("tahoma", 12), "#000", anchor="mm")
        b.add(f, 2600)


@ad("nurgaz/heating_728x90.gif", ["current", "state", "local"], "NurGaz",
    "NurGaz: the heating season has begun. Pay for gas by the 25th at any Talasbank branch or in the Talasbank app",
    "go.html#nurgaz.ir.ad", start="2026-10-01", end="2027-03-31")
def _(b):
    blue, deep = "#0b5aa6", "#073c70"
    flame = stock3("gas_flame.png", (230, 90), focus=(0.45, 0.55))
    rad = stock3("radiator.png", (230, 90), focus=(0.5, 0.5))
    def logo(f, x, y):
        d = ImageDraw.Draw(f)
        d.ellipse((x, y, x + 34, y + 34), fill="#ffffff")
        d.polygon([(x + 17, y + 5), (x + 26, y + 20), (x + 17, y + 29), (x + 8, y + 20)], fill="#f28c00")
        d.polygon([(x + 17, y + 14), (x + 21, y + 22), (x + 17, y + 27), (x + 13, y + 22)], fill="#0b5aa6")
        text(f, (x + 42, y + 17), "NurGaz", font("interx", 22), "#ffffff", anchor="lm")
    frames = [(flame, "Отопительный сезон начался", "Isytuu mezgili bashtaldy — gazdy ubaktyluu tölöñüz"),
              (rad, "Оплатите газ до 25 числа", "Talasbank • приложение Talasbank • кассы NurGaz"),
              (flame, "Утечка газа? Звоните 104", "круглосуточно, бесплатно")]
    for img, a, c in frames:
        f = b.frame(blue)
        f.paste(img, (0, 0))
        for i in range(40):
            rect(f, (190 + i, 0, 191 + i, 89), fill=mix(f.getpixel((190 + i, 45)), blue, i / 40))
        logo(f, 244, 8)
        text(f, (244, 56), a, fit_font("interb", a, 340, 22), "#ffffff", anchor="lm")
        text(f, (244, 78), c, fit_font("inter", c, 470, 13), "#cfe3f7", anchor="lm")
        rect(f, (600, 18, 716, 46), fill="#f28c00", radius=3)
        text(f, (658, 32), "Оплатить", font("interb", 14, for_text="О"), "#ffffff", anchor="mm")
        b.add(f, 2800)


@ad("kartoshka/storage_468x60.gif", ["local", "current", "flash"], "Talas North Cold Store",
    "Store your potatoes until spring: cellars at Talas North, 2 som per kg a month",
    "go.html#talas-sklad.ir.ad", start="2026-09-20", end="2026-12-15", colors=96)
def _(b):
    cel = stock3("cellar.png", (150, 60), focus=(0.5, 0.6))
    pot = trim(photo(S("b3/potatoes.png"), (200, 150), fit="contain", remove_white=True))
    msgs = [("Овощехранилище «Талас-Север»", "картофель • лук • морковь • яблоки"),
            ("2 сом за кг в месяц", "храните урожай до весенних цен!"),
            ("Kartoshkañyzdy jazga cheyin saktañyz", "тел. 0 (555) 62-18-05 • весы на месте")]
    for a, c in msgs:
        f = b.frame("#2e5e1e")
        f.paste(cel, (0, 0))
        paste(f, pot, (184, 60), scale_h=42, anchor="mb")
        text(f, (218, 20), a, fit_font("tahomab", a, 244, 16), "#ffffff", anchor="lm")
        text(f, (218, 42), c, fit_font("tahoma", c, 244, 12), "#ffe680", anchor="lm")
        b.add(f, 2400)


@ad("attelkom/home100_468x60.gif", ["current"], "Attelkom",
    "Attelkom home internet up to 100 Mbit/s* (*central district of Talas)", "go.html#attelkom.ir.ad")
def _(b):
    logo = Image.open(S("attelkom_logo_color.png")).convert("RGBA")
    r = Image.open(S("b3/router.png")).convert("RGB").crop((240, 40, 900, 730))
    r = ImageOps.autocontrast(r, cutoff=(0, 3))  # lift the grey studio sweep to white
    m = Image.new("L", r.size, 0)
    ImageDraw.Draw(m).ellipse((30, 30, r.width - 30, r.height - 30), fill=255)
    router = r.convert("RGBA")
    router.putalpha(m.filter(ImageFilter.GaussianBlur(40)))
    msgs = [("до 100 Мбит/с*", "Домашний интернет Attelkom"), ("от 890 сом/мес", "подключение 0 сом до 30.11"),
            ("Üy internet", "*в центральном районе г. Талас. Скорость не гарантируется")]
    for big, small in msgs:
        f = b.frame("#ffffff")
        paste(f, logo, (8, 30), scale_h=40, anchor="lm")
        paste(f, router, (190, 30), scale_h=58, anchor="mm")
        text(f, (232, 22), big, fit_font("interblk", big, 224, 24), "#1f8a2b", anchor="lm")
        text(f, (232, 46), small, fit_font("inter", small, 228, 12), "#555", anchor="lm")
        rect(f, (0, 0, 467, 59), outline="#1f8a2b")
        b.add(f, 2300)


@ad("attelkom/home100_300x250.gif", ["current"], "Attelkom",
    "Attelkom home internet: up to 100 Mbit/s*, connection free until 30 November", "go.html#attelkom.ir.ad")
def _(b):
    fam = stock3("family_laptop.png", (300, 150), focus=(0.5, 0.4))
    logo = attelkom_logo(0)
    for k, (a, c) in enumerate((("до 100 Мбит/с*", "Домашний интернет для всей семьи"),
                                ("0 сом", "подключение до 30 ноября"))):
        f = b.frame("#ffffff")
        f.paste(fam, (0, 0))
        rect(f, (0, 150, 300, 250), fill="#1f8a2b")
        rect(f, (196, 8, 292, 30), fill="#ff8a00", radius=11)
        text(f, (244, 19), "АКЦИЯ", font("interx", 12, for_text="А"), "#ffffff", anchor="mm")
        text(f, (16, 176), a, fit_font("interx", a, 270, 28), "#ffffff", anchor="lm")
        text(f, (16, 204), c, font("inter", 14, for_text=c), "#e5f6e6", anchor="lm")
        text(f, (16, 238), "*центральный район г. Талас", font("inter", 9, for_text="ц"), "#bfe5c4", anchor="lm")
        paste(f, logo, (288, 242), scale_w=70, anchor="rb")
        b.add(f, 2600)


def tsu_seal(size):
    k = 4
    s = size * k
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse((0, 0, s - 1, s - 1), fill="#ffffff")
    d.ellipse((s * .06, s * .06, s * .94, s * .94), fill="#13306b")
    d.ellipse((s * .12, s * .12, s * .88, s * .88), outline="#d4a72c", width=k * 2)
    book = [(s * .28, s * .38), (s * .5, s * .44), (s * .72, s * .38), (s * .72, s * .62), (s * .5, s * .68), (s * .28, s * .62)]
    d.polygon(book, fill="#ffffff")
    d.line((s * .5, s * .44, s * .5, s * .68), fill="#13306b", width=k * 2)
    f_ = ImageFont.truetype(FONTS["timesb"][0], int(s * .14))
    d.text((s * .5, s * .27), "TSU", font=f_, fill="#d4a72c", anchor="mm")
    d.text((s * .5, s * .79), "1932", font=ImageFont.truetype(FONTS["timesb"][0], int(s * .1)), fill="#d4a72c", anchor="mm")
    return im.resize((size, size), Image.LANCZOS)


@ad("tsu/evening_468x60.gif", ["current", "local", "state"], "Talas State University",
    "Talas State University evening courses: accounting, English, computer literacy. Enrolment until 1 November",
    "go.html#tsu.ir.ad", start="2026-10-01", end="2026-11-01")
def _(b):
    seal = tsu_seal(48)
    msgs = [("Вечерние курсы ТГУ", "Talas State University • Talas mamlekettik universiteti"),
            ("Бухгалтерия • English • Компьютер", "3 месяца • занятия 18:30–20:30 • сертификат"),
            ("Приём до 1 ноября", "ул. Университетская, 12, корпус 3 • тел. 2-31-40-17")]
    for a, c in msgs:
        f = b.frame("#13306b")
        paste(f, seal, (6, 30), anchor="lm")
        text(f, (64, 20), a, fit_font("georgiab", a, 396, 18), "#ffffff", anchor="lm")
        text(f, (64, 43), c, fit_font("tahoma", c, 396, 12), "#d4c48c", anchor="lm")
        rect(f, (0, 56, 467, 59), fill="#d4a72c")
        b.add(f, 2400)


@ad("tsu/evening_300x250.gif", ["current", "local", "state"], "Talas State University",
    "Talas State University evening courses for adults. Enrolment until 1 November",
    "go.html#tsu.ir.ad", start="2026-10-01", end="2026-11-01")
def _(b):
    cls = stock3("class.png", (300, 140), focus=(0.5, 0.5))
    seal = tsu_seal(44)
    for k in range(2):
        f = b.frame("#13306b")
        f.paste(cls, (0, 54))
        paste(f, seal, (8, 5), anchor="lt")
        text(f, (60, 16), "Talas State University", font("georgiab", 15), "#ffffff", anchor="lm")
        text(f, (60, 36), "Вечерние курсы для взрослых", font("tahoma", 12), "#d4c48c", anchor="lm")
        if k == 0:
            items = ["Бухгалтерия и налоги", "English (A1–B2)", "Компьютерная грамотность"]
            rect(f, (0, 194, 299, 249), fill="#13306b")
            text(f, (14, 207), "• " + items[0] + "   • " + items[1], font("tahomab", 12), "#ffffff", anchor="lm")
            text(f, (14, 226), "• " + items[2] + "   • 3 месяца", font("tahomab", 12), "#ffffff", anchor="lm")
            text(f, (14, 243), "сертификат государственного образца", font("tahoma", 10), "#d4c48c", anchor="lm")
        else:
            rect(f, (0, 194, 299, 249), fill="#d4a72c")
            text(f, (150, 212), "ПРИЁМ ДО 1 НОЯБРЯ", font("interblk", 20, for_text="П"), "#13306b", anchor="mm")
            text(f, (150, 236), "корпус 3, каб. 104 • тел. 2-31-40-17", font("tahomab", 12), "#13306b", anchor="mm")
        b.add(f, 3000)


@ad("state/flu_vaccine_300x250.gif", ["state", "current"], "ISEZ Health Department",
    "Free seasonal flu vaccination at your district polyclinic until 30 November",
    "go.html#health.isez.ir.ad", start="2026-10-01", end="2026-11-30")
def _(b):
    vac = stock3("vaccine.png", (300, 140), focus=(0.5, 0.4))
    crim = "#a5121e"
    for k, (a, c) in enumerate((("Tumoogo karshy emdöö", "Вакцинация от гриппа"),
                                ("БЕСПЛАТНО", "в поликлинике по месту жительства до 30 ноября"))):
        f = b.frame("#ffffff")
        rect(f, (0, 0, 299, 34), fill=crim)
        text(f, (12, 17), "ISEZ • Департамент здравоохранения", font("interb", 12, for_text="Д"), "#ffffff", anchor="lm")
        f.paste(vac, (0, 34))
        text(f, (150, 196), a, fit_font("interx", a, 280, 24), crim, anchor="mm")
        text(f, (150, 224), c, fit_font("inter", c, 284, 13), "#222", anchor="mm")
        rect(f, (0, 243, 299, 249), fill=crim)
        b.add(f, 3200)


@ad("herald/delivery_468x60.gif", ["current", "local"], "The Talas Herald",
    "The Talas Herald delivered to your door before 7am: print and digital, 90 som a month",
    "https://talasherald.com/subscribe.html")
def _(b):
    paper = stock3("newspaper.png", (120, 60), focus=(0.5, 0.55))
    msgs = [("The Talas Herald", "on your doormat before 7am"),
            ("90 som a month", "home delivery + every story online"),
            ("Subscribe today", "+996-39-2-44-10-97 • talasherald.com")]
    for a, c in msgs:
        f = b.frame("#faf8f3")
        f.paste(paper, (0, 0))
        text(f, (136, 22), a, fit_font("timesb", a, 230, 24), "#111", anchor="lm")
        text(f, (136, 44), c, fit_font("georgia", c, 230, 12), "#555", anchor="lm")
        rect(f, (376, 18, 460, 42), fill="#8c1d18")
        text(f, (418, 30), "SUBSCRIBE", font("arialb", 11), "#ffffff", anchor="mm")
        rect(f, (0, 0, 467, 59), outline="#8c1d18")
        b.add(f, 2400)


# ====================================================================== build

def main(only=None):
    camp_path = os.path.join(ROOT, "campaigns.json")
    camp = json.load(open(camp_path)) if os.path.exists(camp_path) else {"ads": []}
    by_file = {a["file"]: a for a in camp.get("ads", [])}
    for a in ADS:
        if only and only not in a["file"]:
            continue
        w, h = size_of(a["file"])
        b = Banner(w, h)
        a["fn"](b)
        out = os.path.join(ROOT, a["file"])
        b.save(out, colors=a["colors"], dither=a["dither"])
        kb = os.path.getsize(out) / 1024
        print(f"{a['file']:48s} {len(b.frames):3d} frames {sum(b.durations)/1000:5.1f}s {kb:6.1f} KB")
        entry = by_file.get(a["file"], {})
        entry.update({k: a[k] for k in ("advertiser", "file") if a.get(k)})
        entry["size"] = f"{w}x{h}"
        entry["themes"] = a["themes"]
        entry["link"] = a["link"]
        entry["alt"] = a["alt"]
        for k in ("start", "end"):
            if a.get(k):
                entry[k] = a[k]
        entry.setdefault("active", True)
        by_file[a["file"]] = entry
    camp["ads"] = sorted(by_file.values(), key=lambda e: e["file"])
    with open(camp_path, "w") as fh:
        json.dump(camp, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
