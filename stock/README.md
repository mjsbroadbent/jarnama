# Stock photos

FLUX.1 Krea Dev renders (no LoRA, 1024×768, euler/simple, 24 steps, guidance 3.5) made on the owner's PC for the starter ads. All are AI-generated; badges and stray lettering were blurred out. `attelkom_logo_white.png` comes from the wiki's `images/`, `tulpar_icon.png` is the wiki's Tulpar icon rasterized.

| File | Seed | Prompt (abridged) |
|---|---|---|
| flip_phone.png | 9101 | silver mid-2000s mobile phone, blank glowing blue screen, white background |
| family.png | 9102 | cheesy 2008 stock photo, Central Asian family of four on a white sofa |
| sedan.png | 9103 | generic silver 2010 sedan, three-quarter view, white background (badge blurred) |
| apartments.png | 9104 | 3D rendering, three cream and terracotta 12-storey towers, fountain, blue sky |
| smartphone.png | 9105 | hand holding a black smartphone with a blank white screen |
| bank_woman.png | 9106 | smiling young Central Asian businesswoman holding a blank bank card |
| dollars.png | 9107 | fanned stack of US dollar banknotes |
| roulette.png | 9108 | red and gold roulette wheel with chips, black background |
| pills.png | 9109 | unlabeled white pill bottle, blue capsules spilling out |
| wedding_hall.png | 9110 | banquet hall set for a Central Asian wedding, chandeliers, red and gold drapes |
| airliner.png | 9111 | white airliner taking off, no livery (fuselage lettering blurred) |
| old_pc.png | 9112 | beige late-1990s desktop PC with CRT monitor |
| kymyz_bottles.png | 9113 | three glass bottles of milky fermented mare's milk, wooden bowl |

Rejected: a satellite phone (seed 9114 came out as a router).

## Batch 2 (2026-10-15)

| File | Seed | Prompt (abridged) |
|---|---|---|
| akyel.png | 9201 | slender golden palomino horse with a metallic coat, white background |
| chongtor.png | 9202 | small stocky dark bay mountain horse with a shaggy mane |
| ulak.png | 9203 | ulak tartysh scrum, numbered jerseys and helmets, dusty field |
| race.png | 9204 | adult riders galloping across golden steppe in an endurance race |
| trek.png | 9205 | tourists on a horse trek in an alpine valley, guide in a cowboy hat |
| saddle.png | 9206 | handmade leather saddle with brass studs and a felt saddle cloth |
| herder_phone.png | 9207 | smiling herder in a baseball cap with his horse, looking at his phone |
| cowboy_hat.png | 9208 | brown felt cowboy hat, white background |
| groceries.png | 9209 | wicker basket of unlabeled groceries |
| man_phone.png | 9210 | cheerful young man looking at his smartphone |
| gaming_club.png | 9211 | 2005 computer club, CRT monitors (posters blurred) |
| driving_car.png | 9212 | white hatchback with a yellow roof sign (badge blurred) |
| diet.png | 9213 | tape measure around a green apple |
| foal.png | 9214 | bay foal running beside its palomino mother at a stud farm |
| feed.png | 9215 | burlap sack of horse feed with oats spilling out |
| sat_phone2.png | 9216 | rugged handheld satellite phone (label blurred) |

Also `iradone_logo.png`, `freeirad_logo.png`, `jilmay_logo.png` and `jilmay_emoji.png`, rasterized from the wiki's logo files.

## Batch 3 (2026-10-15), in `b3/`

Same settings. For the autumn 2026 Herald slots. Logos and lettering the model invented were smudged out (the player's shirt maker's mark and badge, the truck door decal, the router's name).

| File | Prompt (abridged) |
|---|---|
| fans.png | supporters in white and crimson knitted scarves, stand at dusk (the ad crops out the flare: pyro is banned at Irad grounds) |
| player.png | footballer celebrating in a plain white shirt with crimson sleeves |
| coal_truck.png | old blue Soviet-era dump truck with coal in a village yard, autumn poplars |
| coal_sacks.png | white sacks of coal, white background |
| gas_flame.png | blue gas flame on an enamel stove, aluminium kettle |
| radiator.png | cast-iron radiator under a frosted window, knitted socks |
| cellar.png | burlap sacks of potatoes in a stone cellar, bare bulb |
| potatoes.png | potatoes spilling from a burlap sack, white background |
| router.png | plain white home wifi router, two antennas |
| family_laptop.png | Central Asian family on a sofa round a laptop, carpet on the wall |
| class.png | adult evening students in a university computer room |
| vaccine.png | polyclinic nurse giving an elderly man a flu jab |
| newspaper.png | folded newspaper on a doormat with a glass of tea |

`attelkom_logo_color.png` is the green logo from attelkom-new, rasterized.

`logos/` holds the finished brand logos (trimmed PNGs) of Talasbank, Bank of Irad, Bereke, Irad Pochtasy, Torgoy, Iradenergo and Talas Süt, used through `brand()` in `tools/make_starters.py`. Talas Süt's is the company's own logo from talas-sut.com, unchanged.
