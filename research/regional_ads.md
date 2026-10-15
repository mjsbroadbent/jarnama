# Regional Banner Ads: Style Guide (KG / KZ / UZ / Runet, c. 2000 to now)

Purpose: make fake banner ads for a fictional Central Asian country look like they belong on its web.
Labels used below: **[src]** = backed by a source in section 1. **[gk]** = general knowledge of the period, not checked against a source this session. **[guess]** = an informed guess.

> **Method caveat.** This environment blocked web.archive.org and archive.ph, so I could not open archived homepages or read old banner `<img>`/`<object>` markup or filenames. Today's portals (akipress, gazeta.uz, diesel) load their ads through JavaScript, so plain fetches of them show no banner tags either. What follows comes from rate cards, trade press, news reports and Habr histories. To check details yourself, browse Wayback from your own machine. The best targets are akipress.org (2005–2010), diesel.elcat.kg (2007–2012) and nur.kz / krisha.kz (2010–2014).

---

## 1. Sources examined

| Source | What it showed |
|---|---|
| [kaktus.media, 16 Sep 2015](https://kaktus.media/doc/324621_v_kyrgyzstane_perestali_rabotat_reklamnye_bannery_na_popyliarnyh_saytah.html) | A new Chrome release stopped Flash banners auto-playing. The article says **~90% of banners on Kyrgyz sites were Flash**. 24.kg and ts.kg quickly switched to GIFs and statics. Names the Rubicon agency (vb.kg) and Namba Media. |
| [kapital.kz, 20 Feb 2012](https://kapital.kz/economic/3965/skol-ko-stoit-bannernaya-reklama-v-kaznete.html) | Kaznet rate card: tengrinews **980x100**, satu.kz **728x90 & 240x350**, krisha.kz **240x400** plus a "VIP" **4000x90** strip, kolesa.kz **250x190**, kiwi.kz 300x250. Prices 35–2,500 ₸ per 1,000 impressions. |
| [alfa.kz rate card](https://alfa.kz/node/11) (current) | Modern KZ sizes: top **980x200**, side **240x400** (3 slots), bottom 720x90, central 512x230, text tile **155x155** (headline ≤20 chars). **Branding = two 450x940 side panels** that fade to white. Mobile fullscreen 600x1200. Limits: ≤150 KB static, ≤200 KB GIF/HTML5, ≤30% text. |
| [24.kg, May 2020](https://24.kg/biznes_info/153366_spetsialnyie_skidki_nanbspreklamu_dlya_malogo_inbspsrednego_biznesa/) | Banner sold as a bundle with Facebook/Instagram posts. Sales contact is a WhatsApp/Telegram mobile number. |
| [economist.kg rate card 2026](https://economist.kg/advertisement) | Banners sold as slots "A/B/C" at about 1M views a month in 3 rotations. Paid "articles" and Instagram posts now sit alongside banners. Political ads cost +100%. |
| akipress.org homepage (live fetch) | Ad slots are named in tracking parameters (`place=rightpresscban`, `doskatopleftbot`, `reklamtizing`). A "Новости компаний" (company news) block carries PR for Optima Bank, MEGA/AKNET tariffs, O! Market cashback, ABank and Kompanion. The site runs its own classifieds (doska.kg) with flats priced in som. |
| diesel.elcat.kg (live fetch) | No banners at all today. The "Коммерция и Реклама" forum section (Куплю-Продам, Услуги, Аренда, АнтиРеклама) shows that classifieds lived in forums. |
| [Habr, 31 Aug 2025 (Kholmogorov)](https://habr.com/en/articles/938914) | Runet banner exchanges: Sputnik 1996, RLE 1997, RotaBanner, TX3 (1999). Sizes: 468/480x60, **88x31 buttons**, 120x240, 125x125, 234x60. Sites were designed for 640x480 / 800x600 screens. Pages full of Rambler Top100-style counters. Blinking "ЖМИ СЮДА!!!" ("CLICK HERE!!!"). GIFs made in Ulead GIF Animator. |
| [vc.ru Runet ad history](https://vc.ru/91803-kak-kovali-runet-istoriya-internet-reklamy) | Early favourites were **100x100** and the full banner. Later 336x336 and 728x90 took over. Holodilnik.ru was a big advertiser. Affiliate banners such as amf.ru flowers were everywhere. |
| [oborot.ru, Mar 2008](https://oborot.ru/articles/obzor-sistem-medijnogo-konteksta-starye-bannery-na-novyj-lad-i34343.html) | 468x60 on Runet by 1998. Rambler/Begun/RORER **240x400**, Yandex 200x300, Begun 600x90. Rules banned "frequent intense blinking", sound and fake OS controls; RORER also banned typos. |
| [Habr, Jun 2007](https://habr.com/en/articles/11121) | The Ukrainian Banner Network added 240x400 and 728x90 in June 2007 to standardise Russian/Ukrainian formats. 240x350 was a local variant. |
| [sostav.ru, Oct 2010](https://www.sostav.ru/blogs/21132/4286) | Early clichés: fake Windows buttons and scrollbars, fake progress bars, photos of women with "Познакомимся?" ("Shall we get acquainted?"). GIFs limited to 256 colours. Flash was "an order of magnitude better" but cost more. |
| [fl.ru brief, Mar 2015](https://www.fl.ru/projects/2265591/nujno-sdelat-flesh-ili-gif-banner-po-trebovaniyam.html) | Mail.ru 240x400 Flash: ≤60 KB, AS2/3, needs a static fallback, CPU ≤35% on a Celeron 1.5 GHz. Yandex 200x300: ≤35 KB. |
| [Habr, Apr 2012](https://habr.com/en/articles/142714) | Teaser networks TeaserNet, BodyClick, MarketGid. CTR roughly 0.03–0.2%, with lots of fake traffic. |
| [mobile-review, Oct 2024](https://mobile-review.com/all/articles/operator/a-kak-u-nih-n3-4g-v-kyrgyzstan/) | Beeline KG names tariffs by data volume: «Это 70 ГБ» 500 som, «Это 250 ГБ» 1,500 som, unlimited 850 som. O! sells week and 4-week packs. The author notes KG tariffs don't get flashy marketing names. |
| [economist.kg, Oct 2025](https://economist.kg/novosti-kompanii/2025/10/27/bolshie-intiernieta-i-vozmozhnostiei-v-novom-tarifie-beeline-eto-80-gb/) | «Это 80 GB» — "80 ГБ интернета… всего за 540 сомов на 30 дней", activate with **\*555\*5401#**. |
| [24.kg, Apr 2023](https://24.kg/biznes_info/263886_17let_MEGAinnovatsiy_skorosti_isvobodyi_obscheniya/) | MegaCom launched 28 Apr 2006 and rebranded to MEGA in Dec 2022. Tariff «Элдики» ("of the people"). Prize draw with Tesla cars as prizes («Собери машину», "Build the car"). |
| [economist.kg DemirBank, May 2024](https://economist.kg/novosti-kompanii/2024/05/23/poluchi-onlain-kriedit-ot-demirbank-po-nizkoi-protsientnoi-stavkie-25.md) | "Получи онлайн-кредит… 25%" (get an online loan at 25%), "до 200 000 сомов" (up to 200,000 som), "Без залога, поручителей и справок" (no collateral, guarantors or paperwork). Short number **2222**. |
| [economist.kg real estate, Oct 2024](https://economist.kg/novosti-kompanii/2024/10/14/ekskliuzivnoie-priedlozhieniie-kvartiry-v-iuzhnoi-chasti-bishkieka-s-udobnoi-rassrochkoi/) | «Кочмон Сити — город в городе» ("a city within a city"). Priced at **$650/m²**, 15% down, **instalments over 60 months**, a gift for 50% down. |
| [forbes.kz, Nov 2019](https://forbes.kz/articles/kto_dvigaet_prodaji_v_chernuyu_pyatnitsu_na_kazahstanskom_ryinke) | Sulpak: discounts "до 70%" (up to 70%), "рассрочка на 24 месяца без процентов, переплат и предварительных взносов" (24 months, no interest, no overpayment, no down payment). |
| [kapital.kz Kaspi Red, 2016](https://kapital.kz/business/52995/shoping-s-kaspi-red.html) | "Без процентов. Без комиссий. Без переплаты." (No interest. No fees. No overpayment.) 3-month instalments, 1–5% bonus. Red terminal and stickers in shop windows. |
| [alataucitybank.kz (KZ ad law)](https://alataucitybank.kz/business/osim/articles/zakon-o-reklame-chto-nuzhno-znat-predprinimatelyam-kazakhstana) | Ads in Kazakh; Russian optional. Kazakh goes **left or top**, Russian right or bottom, same font and letter size. **Prices must be in tenge.** Online casinos banned; alcohol banned except wine. |
| [kun.uz, Sep 2022 (UZ ad law)](https://kun.uz/en/news/2022/09/09/law-on-advertising-comes-into-force-basic-rules-and-restrictions-announced) | From 9 Sep 2022 ads must be in Uzbek. A translation may sit below it, ≤40% of the area, in smaller type. Prices in foreign currency are banned. |
| [kaktus.media, May 2024](https://kaktus.media/doc/501411_depytat_predlagaet_zapretit_reklamy_tovarov_s_ykazaniem_ih_stoimosti_v_inostrannoy_valute.html) / [Aug 2025](https://kaktus.media/doc/529267_reklama_na_kyrgyzskom_iazyke_doljna_byt_soglasovana._podpisan_zakon.html) | KG: a bill to ban foreign-currency prices in ads, because property, cars and tours are priced in foreign currency. From 2025, Kyrgyz-language ad text must be approved by local government. |
| [sostav.ru, Mar 2024](https://www.sostav.ru/blogs/239662/44759) | Banner blindness: the 1998 study, where 42% missed the boxed link. Top-right is the most-ignored placement. |
| [spot.uz, Jun 2020](https://www.spot.uz/ru/2020/06/16/ads/) | UZ ad market about $48M, roughly 70% TV, with digital third. Telegram is central but can't be targeted. |

---

## 2. Sizes and placements by era

**c. 2000–2005: banner exchanges and counters**
- **468x60** (or 480x60) full banner at the top or bottom. **100x100** squares in side columns. **88x31** buttons and counters in a row at the page footer [src: Habr 2025, vc.ru].
- Footer counter row [gk]: LiveInternet, Rambler Top100, Mail.ru, SpyLog, and for KG the national rating **top.kg** (some ran their own counters, e.g. 'Net.kg'). Each counter showed hits and visitors in tiny pixel digits.
- Also seen: 120x60, 120x240, 125x125, 234x60 [src].
- Layouts were fixed width for 800x600, built in tables, with ads in their own cells.

**c. 2005–2012: Flash era**
- **240x400** becomes the standard Runet side banner (240x350 is a local variant) [src].
- **728x90**, plus wide top strips: tengrinews **980x100**, others 990x90 and 1000x90 [src: kapital.kz]. **100%x90 stretch** strips ("растяжка"/"перетяжка") between content blocks [gk].
- Classifieds and verticals use odd sizes: kolesa **250x190**, krisha's "VIP 4000x90" (presumably full-bleed and centred) [src].
- **Branding / background takeover** of the whole page background around a centred 1000px site; usually a bank, operator or car brand [gk; the format is confirmed later by alfa.kz].
- Format: SWF with a GIF fallback, ~30–60 KB [src: fl.ru]. In KG about 90% Flash until 2015 [src].

**c. 2012–2018: GIF comeback and teasers**
- After Chrome's 2015 Flash change, Kyrgyz sites switched to **animated GIF and static JPG** [src].
- **Teaser blocks**: grids of ~100x100 to 200x150 thumbnails with a yellow-press headline, at the bottom of articles [src: Habr 2012 for the networks; look is gk].
- **300x250** spreads through Google and Yandex networks.

**c. 2018–now: mobile-first and native**
- Desktop: **980x200** or 1000x120 top, **240x400** side, 2 or 3 rotations per slot [src: alfa.kz].
- Mobile: **320x50/100**, **320x250**, fullscreen interstitials of 600x1200 with a "Закрыть" (close) timer [src].
- Branding: two **450x940** side panels [src].
- Much of the budget has moved to **sponsored articles** ("Новости компаний", PR labels), Instagram stories and Telegram posts [src: akipress, economist.kg].

---

## 3. Typical advertisers and offers

| Era | Advertisers | Offer formats (translated) |
|---|---|---|
| 2000–05 | ISPs and dial-up cards (in KG: Elcat, AsiaInfo, Aknet [gk]); computer shops; banner exchanges; dating; flower/gift affiliates; web studios ("Создание сайтов", website design) | "Интернет-карты от 100 сом" (internet cards from 100 som) [guess]; "Знакомства" (dating); "ЖМИ СЮДА!!!" (click here!!!) |
| 2005–12 | **Mobile operators** (KG: MegaCom from 2006, Beeline, Fonex, O!; KZ: Kcell/Activ, Beeline; UZ: Beeline, Ucell, UMS/MTS) [src/gk]; banks (consumer credit, deposits, Western Union-style transfers); car dealers (Toyota, Hyundai, Lada); electronics shops; English courses; tours (Turkey, UAE, Issyk-Kul); visa and study abroad | "Звони по 1 сому!" (call for 1 som); "Кредит за 15 минут" (credit in 15 minutes); "Депозит до 18% годовых" (deposit up to 18% a year); "Скидки до 50%" (discounts up to 50%); "Хит сезона" (hit of the season) [gk] |
| 2012–18 | Same as above, plus real-estate developers ("элитки", new-build flats), microcredit, furniture, taxis, online shops; teaser offers (weight loss, "secret of"…) | "Квартиры в рассрочку" (flats on instalments); "Без справок" (no paperwork); "0-0-12" (0% interest, 0 down, 12 months; Kaspi-style in KZ) [gk] |
| 2018–now | Bank apps and fintech (Kaspi, Halyk, Optima/MBank, Demir, O!Bank), marketplaces (Kaspi, O! Market, Uzum), operators (tariffs named by GB), developers, education and IT courses; **betting** grey/illegal in places, where banned it shows up in Telegram [guess] | «Это 80 GB… всего за 540 сомов на 30 дней» (80 GB for just 540 som per 30 days); "Онлайн-кредит до 200 000 сомов, без залога" (online loan up to 200,000 som, no collateral); "рассрочка 60 месяцев, взнос 15%" (60 months, 15% down); "кэшбэк до 5%" (cashback up to 5%) [src] |

Real offer patterns worth copying:
- Telecom: **big number of GB + price + period + USSD code** (`*555*5401#`) [src].
- Banks: **rate % + "до" (up to) amount + "без X, Y и Z"** (no X, Y or Z) + short number (2222) [src].
- Retail: **"до 70%"** (up to 70%) + **"рассрочка 24 мес. без % и первого взноса"** (24 months, no interest, no down payment) [src].
- Real estate: **name in guillemets + tagline ("город в городе", a city within a city) + price per m² in $ + months of instalments** [src]. Dollar pricing is normal in KG property and cars, banned in UZ, and tenge-only in KZ [src].

---

## 4. Visual conventions by era

**2000–05 [gk unless marked]**
- Default fonts: Arial, Verdana, Tahoma, **Impact**, Times; Comic Sans for "fun".
- Pure web colours: #FF0000 red, #0000FF blue, yellow on black.
- GIFs of 2 to 6 frames with 256-colour dithering and hard-blinking text, often looping without end [src: sostav for 256 colours].
- Cheap tricks: fake Windows buttons, fake "OK" dialogs, fake progress bars [src].
- Small files (~10–15 KB), so photos were heavily JPEG-compressed or reduced to clip-art.
- Bevelled 1px borders.

**2005–12 (Flash) [gk]**
- Smooth motion: text flies in, light glints sweep across the product, logos zoom in.
- Glossy "Web 2.0" pill buttons ("Подробнее" = more, "Узнать больше" = learn more, "Подключить" = connect).
- Gradient backgrounds, reflections under products, **red/yellow starbursts** reading "АКЦИЯ!" (promotion!), "-30%", "ХИТ!" (hit!), "NEW".
- Loops of about 8–15 s, usually 3–4 "scenes": hook, product, price, logo and phone number.
- Stock photos of smiling Slavic or European-looking models alongside local faces; family-in-new-car or family-with-keys shots for real estate.
- Operator brand colours carry the ad: Beeline yellow/black, MegaCom green, O! pink/magenta, Kcell purple, Kaspi red, Halyk green [gk].

**2012–18**
- Flat design and Helvetica-like or Roboto/Open Sans type.
- In KG, GIFs again after 2015, with 3–5 frames carrying the old Flash scene structure [src for the switch].
- Teasers: close-up "shock" thumbnails (bellies, faces, pills) with clickbait text [gk].

**2018–now**
- Clean flat brand colours, big bold numbers ("80 ГБ", "0%", "25%"), app phone mockups, App Store / Google Play badges, QR codes.
- Instagram-style 1:1 and 9:16 creatives reused as banners [guess].

**Constants across eras**
- **Phone numbers big and prominent**: KG `0 (312) 90 90 60`, `0555 xx xx xx`, `+996 …`; KZ `8 (727) …`, `+7 701 …`; UZ `+998 71 …`. Short numbers: 2222, 9999, `*xxx#` [src/gk].
- **Price large, currency small**: "540 сом", "от 2 990 ₸" (₸ sign since 2007), "199 000 сўм / so'm" [gk]. The Kyrgyz som sign ⃀ exists (2017) but is rarely used; "сом" spelled out is the norm [gk].
- **Languages**:
  - Russian dominates in KG and the older KZ/UZ web.
  - Kazakh is required first in KZ ads [src]; Uzbek is required in UZ from 2022 [src], written in Latin script (O'zbek, so'm), though Cyrillic lingers.
  - Kyrgyz shows up in slogans and tariff names («Элдики»).
  - English for brand words ("Black Friday", "SALE", "NEW", "Online").
  - Mixed Russian + national-language lines are common [gk].
  - 2000s fonts often lacked ң ө ү ә қ ғ і, so expect substitutes or missing letters in older Kazakh/Kyrgyz text [gk].
- Fine print such as "*Подробности на сайте" (*details on the site) and licence numbers under bank ads ("Лицензия НБКР №…" = National Bank licence no.) [gk].

---

## 5. Clichés worth copying, and what feels too Western

**Copy these**
- Exclamation marks and caps: "АКЦИЯ!", "СКИДКИ!", "ТОЛЬКО ДО 31 МАЯ!" (until 31 May only), "ЖМИ!" (click!), "Успей!" (hurry!) [src/gk].
- The word **"до"** (up to) before the discount and **"от"** (from) before the price.
- Instalment formulas: "0-0-12", "без переплат" (no overpayment), "без первого взноса" (no down payment).
- "Без залога и справок" (no collateral or paperwork). "Кредит за 15 минут" (credit in 15 minutes).
- USSD codes and short numbers as the call to action instead of a URL.
- A starburst sticker with the percentage. A red price over a crossed-out old price.
- A slightly crowded layout: logo, offer, phone number and URL all in a 240x400.
- Gift hooks: "Подарок каждому!" (a gift for everyone!), "Розыгрыш автомобиля" (car prize draw; cf. MEGA's Tesla draw [src]).
- Classifieds and forum culture: "Куплю-Продам" (buy-sell), "Срочно!" (urgent!).
- Seasonal hooks: Nooruz (Navruz), 8 Марта (8 March), Новый год (New Year), Курман/Орозо айт (Eid holidays), back to school ("1 сентября").
- A footer row of 88x31 counters on 2000s pages.
- Dollar prices for flats and cars (KG). Tenge only (KZ). Sum only after 2022 (UZ).

**Feels off or too Western**
- Witty understatement and minimal "Think different" copy with no price. Regional ads lead with **numbers**.
- US-style "Sign up free" calls to action, or "$9.99/mo" pricing.
- Perfectly kerned premium typography on a 2006 banner. Real ones used system fonts and Impact.
- Diverse US stock models; use local or generic Slavic/Central Asian faces.
- Thanksgiving or Super Bowl tie-ins.
- Credit scores or "APR" wording; locally it is "% годовых" (% a year), "ГЭСВ" (effective annual rate, KZ).
- Gambling or alcohol banners on mainstream KZ/UZ news sites (restricted there) [src].
- Prices without a currency word, or with "€".

---

## 6. Ad concept templates (generic, for a fictional country)

Use your own currency word (shown here as **[CUR]**), operator names and USSD codes.

1. **Telecom tariff GIF, 240x400, 3 frames**: (1) huge "50 ГБ" on the brand colour → (2) "всего 450 [CUR] / 30 дней" (just 450 [CUR] for 30 days) → (3) "Подключи: \*505\*450#" (connect via the code) plus the logo. Loops; each frame about 1.5 s.
2. **Operator per-minute offer, 2007-style 468x60 Flash look**: "Звони по 1 [CUR]!" (call for 1 [CUR]!) slides in from the right, a glint sweeps across, then a starburst "АКЦИЯ!" and the short number.
3. **Bank consumer loan, 728x90**: "Кредит до 300 000 [CUR] · от 19% годовых · без залога и справок" (loan up to 300,000 [CUR], from 19% a year, no collateral or paperwork), then a big short number "7777", then fine print "*Лицензия НБ №…" (National Bank licence no.).
4. **Bank app, modern 320x250**: phone mockup, "Переводы без комиссии" (fee-free transfers), App Store and Google Play badges, QR code.
5. **Deposit, Flash era 240x400**: gold coins with a reflection, "Депозит «Байлык» до 16% годовых" (Baylyk deposit up to 16% a year; *байлык* = wealth), glossy "Подробнее" (more) button.
6. **Electronics chain sale, 980x100 top strip**: red background, "СКИДКИ ДО 70%" (discounts up to 70%) in Impact or heavy sans, crossed-out old price, "рассрочка 0-0-24" (0%, 0 down, 24 months), dates "только 25–30 ноября" (25–30 November only).
7. **Real-estate developer, 240x400 or branding takeover**: render of a tower block at sunset, «Ак-Суу Сити — город в городе» ("Ak-Suu City: a city within a city"), "от $690/м²" (from $690/m²), "рассрочка 60 мес., взнос 15%" (60 months, 15% down), sales phone in big type.
8. **Car dealer, 728x90 Flash**: car slides in, "Новая Corolla от 1 990 000 [CUR]" (new Corolla from 1,990,000 [CUR]), "Trade-in · Кредит" (trade-in, credit), showroom address.
9. **English or IT courses, 2000s GIF 100x100**: flag of the UK or US, then "IELTS 7.0" or "Курсы английского — 1-е занятие бесплатно!" (English courses, first lesson free!), then the phone number. 3 frames, blinking.
10. **Study or work abroad and visas, 468x60**: "Учёба в Корее / Работа в Европе / Визы" (study in Korea / work in Europe / visas), photo of passport and plane, "Звоните: 0 (XXX) …" (call).
11. **Tour operator, 240x400**: beach photo, "Турция всё включено от $499" (Turkey all-inclusive from $499), "Раннее бронирование −20%" (early booking −20%), plus a domestic lake-resort variant in summer.
12. **ISP, 2003-style 88x31 or 468x60**: "Безлимитный ADSL — 990 [CUR]/мес" (unlimited ADSL, 990 [CUR] a month) or "Интернет-карты везде" (internet cards everywhere), pixel font, 2-frame blink.
13. **Teaser tile, 200x150, 2014 style**: tight-crop "shock" photo and the headline "Местные врачи в шоке: этот способ…" (local doctors are shocked: this method…). Below articles, in a grid of six.
14. **Marketplace or holiday mega-sale, mobile 320x100**: "Nooruz Sale · кешбэк до 10%" (cashback up to 10%), the state-language line first with Russian below, per the regional legal pattern.
15. **Counter and button footer row (2000s page dressing)**: four or five 88x31s for a fictional national rating ("TOP.XX"), a LiveInternet-style hit counter, and "Сделано в … studio" (made in … studio).

Animation rules of thumb [gk/guess]:
- GIF: 2–5 frames, 0.8–2 s each, infinite loop, hard cuts or one blinking element.
- Flash look: 3–4 scenes over 8–15 s, fly-ins, glints, a pulsing call-to-action button.
- 2015+: 3–5 flat frames.
- Modern: mostly static, or a subtle 2–3 frame HTML5 sequence.
