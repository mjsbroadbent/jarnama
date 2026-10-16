# Attelkom Jarnama

**Publisher guide and full ad inventory:** https://ads.attelkom.net/

The ad network of the Irad worldbuilding project. In the world of Irad, **Attelkom Jarnama** (*jarnama*, "advertisement") is the advertising department of Attelkom, the national telecom. It sells and serves the banner ads seen on Iradi websites: IradOne Online, the Talas Herald, the Attelkom-hosted personal pages of the webring, and so on.

Out of world, this repo holds every fake banner ad for those sites in one place, plus a small script that each site includes to show them.

## Layout

| Path | What it is |
|---|---|
| `ads/<advertiser>/` | The banners for one advertiser: GIFs, PNGs or self-contained HTML5 banners, named by size (`728x90.gif`, `300x250.html`) |
| `campaigns.json` | Every ad: advertiser, file, size, themes, link, start and end dates, active flag |
| `THEMES.md` | The ad themes (era looks and advertiser types) a site asks for |
| `go.html` | Where every ad click lands: opens the advertiser's site when it is live (`sites.json`), Attelkom's restricted-resources notice when it is blocked, and "site unavailable" otherwise. `sites.json` is copied from the irad-persona skill's site registry by `python3 tools/sync_sites.py`. |
| `serve.js` | Included by each site. Fills `<div class="jarnama" data-size="728x90"></div>` slots with a random ad of the page's (or slot's) theme |
| `research/` | Notes on real Central Asian advertising (style, sizes, offers, languages) and the house style guide for Iradi ads |
| `tools/` | Scripts that build the animated GIFs |

## Sizes

The standard IAB sizes of the late 1990s and 2000s: 468×60 full banner, 728×90 leaderboard, 300×250 medium rectangle, 120×600 and 160×600 skyscrapers, 88×31 buttons for the webring.

## Making ads

- `tools/banner.py` is a small PIL toolkit for era-styled animated GIFs: frames and timing, a shared palette, unantialiased "pixel" text, outlines and drop shadows, WordArt-style gradient text, starbursts, glossy pill buttons, Windows 98 / XP dialogs, buttons and progress bars, cursors, light sweeps, and cut-outs of white-background photos.
- `tools/make_starters.py` builds every ad in `ads/` (one function per ad) and writes its entry into `campaigns.json`. Run `python3 tools/make_starters.py` for all, or pass part of a file name to rebuild one.
- `stock/` holds the AI product photos the ads use (see `stock/README.md`).
- `index.html` is the in-world landing page of ads.attelkom.net (Attelkom site style) with a partner login that fills itself in (demo_partner) and goes to `gallery.html`, the publisher guide, code builder and ad gallery. Images in `img/` (logo from attelkom-new, AI hero image).
- `preview.html` shows the whole inventory with a theme filter.
- Ad links point to `go.html#domain`, an in-universe "advertiser's site cannot be reached" page, so no ad ever sends a reader to a real domain.
- Fonts: the Windows fonts real banners used are not available here. Liberation Sans/Serif stand in for Arial/Times, DejaVu Sans (Condensed) for Verdana/Tahoma, TeX Gyre Heros Cn Bold for Impact (Latin only; Cyrillic falls back to DejaVu).
- Keep files small the way real networks did: about 150 KB at most, fewer frames for photo ads.

## Sites using Jarnama

| Site | How | Themes |
|---|---|---|
| IradOne Online | its own `site.js` reads `campaigns.json` for its `.ad-slot` boxes (leaderboard = 728×90, box = 300×250), mixed with IradOne's house ads | `current state` |
| Talas Herald | `serve.js` in the page template; slots on the front page, section pages and under every story | `current local state` |
| Jarysh | `serve.js` in the page template; a 728×90 slot above the footer, next to Jarysh's own house ads | `current local sketchy` |
| Kartalar (Attelkom Maps) | `serve.js`; a 300×250 slot at the foot of every place panel, filled by `window.jarnamaFill()` when the panel opens | `current local state` |
