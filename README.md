# Attelkom Jarnama

The ad network of the Irad worldbuilding project. In the world of Irad, **Attelkom Jarnama** (*jarnama*, "advertisement") is the advertising department of Attelkom, the national telecom. It sells and serves the banner ads seen on Iradi websites: IradOne Online, the Talas Herald, the Attelkom-hosted personal pages of the webring, and so on.

Out of world, this repo holds every fake banner ad for those sites in one place, plus a small script that each site includes to show them.

## Layout

| Path | What it is |
|---|---|
| `ads/<advertiser>/` | The banners for one advertiser: GIFs, PNGs or self-contained HTML5 banners, named by size (`728x90.gif`, `300x250.html`) |
| `campaigns.json` | Every ad: advertiser, file, size, themes, link, start and end dates, active flag |
| `THEMES.md` | The ad themes (era looks and advertiser types) a site asks for |
| `serve.js` | Included by each site. Fills `<div class="jarnama" data-size="728x90"></div>` slots with a random ad of the page's (or slot's) theme |
| `research/` | Notes on real Central Asian advertising (style, sizes, offers, languages) and the house style guide for Iradi ads |
| `tools/` | Scripts that build the animated GIFs |

## Sizes

The standard IAB sizes of the late 1990s and 2000s: 468×60 full banner, 728×90 leaderboard, 300×250 medium rectangle, 120×600 and 160×600 skyscrapers, 88×31 buttons for the webring.
