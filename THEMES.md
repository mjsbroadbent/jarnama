# Ad themes

A site (or a single slot) asks for a theme, and `serve.js` only shows ads tagged with that theme. A slot can ask for several, separated by spaces (`data-theme="flash sketchy"` mixes Flash-era ads with sketchy ones).

| Code | Era | Looks like | Typical advertisers | Use on |
|---|---|---|---|---|
| `dialup` | 1996–2004 | 468×60 and 88×31 GIFs, 256 colours, blinking, Impact/Tahoma/Comic Sans, "CLICK HERE!!!", banner-exchange logos, "Best viewed in Internet Explorer" | Attelkom dial-up cards and the first GSM network, computer shops, internet cafés, Swift Hooves CD, territorial-era US contractors, banner exchanges and webrings, pager and fax services | The GeoCities-style webring pages, old FREEFORUM skins, archived pages |
| `flash` | 2004–2014 | 240×400 and 728×90, glossy pill buttons, starbursts ("SALE!", "-30%"), light sweeps across a product, stock photos of smiling families, Nokia and Samsung flip phones | Attelkom 3G (2010), Talasbank credit and deposits, car dealers, electronics shops, mobile phones, English and computer courses, Iradiya flights, real estate "city within a city" projects | Mid-2000s sites, Irad Film Society, any page meant to feel dated but mainstream |
| `current` | 2015–now | Flat design, one big number, app phone mockups with store badges, tidy logos, no blinking | Attelkom 4G tariffs, Talasbank app, Jılmay, delivery, supermarkets, Sukarne and Conagra beef, IradOne shows, Tulpar Talas football tickets | IradOne Online, Talas Herald, Jılmay |
| `state` | any | Plain and earnest, crimson and white, the flag kept out or simplified, slogan plus a short number | DPI and Department of Public Information campaigns, Irad Day, census, Gendarmerie safety and smuggling hotlines, vaccination, tax deadlines, conscription, "Irad is not for sale" | IradOne, government pages, rotated into `current` |
| `local` | any | Text-heavy, cheap, a phone number in huge type, clip art or a single photo, spelling slips | Wedding and feast halls, car repair, kymyz farms, felt workshops, driving schools, visa services, tutors, bazaar stalls, taxi numbers | Jılmay, small business pages, the Herald classifieds |
| `diaspora` | any | English or mixed English-Iradi, US-style stock layouts | Money transfers to Irad, Chicago–Talas flights via Istanbul, immigration lawyers, Iradi groceries in Chicago, church festivals | Iradi-American sites, Jason Ilyasov's pages |
| `offnet` | 2007–now | Ads that Attelkom Jarnama refuses, served by foreign networks on sites outside its reach | Tulpar and Tulparcoin, VPNs, Kazakh and Kyrgyz SIM cards, satellite phones, exile media, plus cheap foreign filler | FREEFORUM and freeirad.org, Tulpar's own pages |
| `sketchy` | any | Garish, fake system dialogs ("You are the 1,000,000th visitor!"), countdown timers, before/after photos, "one weird trick", flashing red | Betting and online casinos, "bone pills" and miracle cures, weight loss, fake crypto, dating and adult-site teasers (suggestive text and silhouettes only, nothing explicit), download buttons that aren't | Pirate sites, forums, the shadier webring pages, mixed into `offnet` |

## Rules

- Every ad in `campaigns.json` carries `themes`, a list of one or more codes.
- An era theme (`dialup`, `flash`, `current`) sets the look; the others (`state`, `local`, `diaspora`, `offnet`, `sketchy`) set the advertiser type, and their ads are made in whichever era style suits the site they are aimed at. Tag those ads with both, e.g. `["local", "flash"]`.
- Real brands never appear. Iradi brands from the lore (Attelkom, Talasbank, Jılmay, Iradiya, IradOne, Tulpar) and invented ones only.
