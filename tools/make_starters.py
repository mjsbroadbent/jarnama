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


@ad("offnet/kazsim_300x250.gif", ["offnet", "flash"], "SteppeMobile (Kazakhstan)",
    "Kazakh SIM cards for the border districts, delivered", "go.html#steppemobile-sim.kz")
def _(b):
    for i in range(8):
        f = gradient(b.frame(), (0, 0, 300, 250), "#ffe14d", "#ffb400")
        # SIM card drawn flat
        rect(f, (24, 40, 134, 180), fill="#ffffff", outline="#555", radius=8)
        rect(f, (50, 78, 108, 124), fill="#e3c26b", outline="#8a6d1f", radius=5)
        for y in (90, 101, 112):
            ImageDraw.Draw(f).line([(50, y), (108, y)], fill=rgb("#8a6d1f"))
        text(f, (79, 154), "SIM", font("arialb", 18), "#333", anchor="mm")
        text(f, (210, 62), "Нет связи", font("arialb", 17), "#222", anchor="mm")
        text(f, (210, 84), "у границы?", font("arialb", 17), "#222", anchor="mm")
        text(f, (210, 120), "Казахская", font("arial", 15), "#222", anchor="mm")
        text(f, (210, 138), "SIM-карта", font("arial", 15), "#222", anchor="mm")
        text(f, (210, 164), "$15", font("impact", 34), "#c00000" if i % 2 else "#222", anchor="mm")
        rect(f, (24, 198, 276, 232), fill="#222222", radius=4)
        text(f, (150, 215), "Доставка в любой район", font("arialb", 14), "#ffe14d", anchor="mm")
        b.add(f, 500)


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
    for k, (top, big, sub) in enumerate((("Jılmay Cargo", "Order abroad.", "We bring it to Talas."),
                                         ("Jılmay Cargo", "Chet eldeñ", "buyurtma — üyüñüzgö"),
                                         ("Jılmay", "$1 / kg", "first parcel, until 31 Oct"))):
        f = b.frame("#fff5c2")
        ImageDraw.Draw(f).ellipse((214, 18, 282, 86), fill=rgb("#fdd835"), outline=rgb("#e0a800"), width=2)
        d = ImageDraw.Draw(f)
        d.ellipse((234, 40, 241, 47), fill=rgb("#4a3000"))
        d.ellipse((255, 40, 262, 47), fill=rgb("#4a3000"))
        d.arc((230, 46, 266, 74), 20, 160, fill=rgb("#4a3000"), width=3)
        text(f, (20, 40), top, font("poppinsb", 22), "#3a2a00", anchor="lm")
        text(f, (20, 130), big, font("poppinsb", 30, for_text=big), "#1a1a1a", anchor="lm")
        text(f, (20, 166), sub, font("poppins", 16, for_text=sub), "#333", anchor="lm")
        rect(f, (20, 198, 160, 230), fill="#1a1a1a", radius=16)
        text(f, (90, 214), "jilmay.ir.ad", font("poppinsm", 13), "#fdd835", anchor="mm")
        b.add(f, 2200)


@ad("jasil/tarragon_300x250.gif", ["current", "flash", "local"], "Jasil",
    "Jasil tarragon soda, made in Nurzhan", "go.html#jasil.ir.ad")
def _(b):
    for i in range(10):
        f = gradient(b.frame(), (0, 0, 300, 250), "#9be15d", "#2f8f2f")
        # bottle drawn flat: green glass, white label
        x = 200
        rect(f, (x + 14, 26, x + 34, 60), fill="#1f6b1f")
        rect(f, (x + 12, 20, x + 36, 30), fill="#d4af37")
        d = ImageDraw.Draw(f)
        d.rounded_rectangle((x, 56, x + 48, 226), 14, fill=rgb("#36c236"), outline=rgb("#1f6b1f"), width=2)
        rect(f, (x + 2, 110, x + 46, 170), fill="#ffffff")
        text(f, (x + 24, 140), "JASIL", font("arialbi", 13), "#1f8f2b", anchor="mm")
        for k in range(6):                       # bubbles rising
            by = 220 - ((i * 14 + k * 37) % 150)
            d.ellipse((x + 10 + (k * 7) % 28, by, x + 15 + (k * 7) % 28, by + 5), outline=rgb("#d8ffd8"))
        text(f, (22, 60), "JASIL", font("arialbi", 44), "#ffffff", anchor="lm", shadow="#1f5f1f", sxy=(2, 2))
        text(f, (22, 100), "Tarhun limonady", font("arialb", 15), "#ffffff", anchor="lm")
        text(f, (22, 122), "Тархун с 1974 года", font("arial", 14), "#f0ffe0", anchor="lm")
        text(f, (22, 196), "Muzdai ich!", font("arialbi", 22), "#ffff66", anchor="lm", shadow="#1f5f1f")
        text(f, (22, 222), "Nurzhan Pivo-Bezalkogol' Zavod", font("arial", 10), "#e0ffe0", anchor="lm")
        b.add(f, 160)


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
