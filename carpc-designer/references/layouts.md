# Six layout archetypes (reference grid 1280 x 736)

All six share one status bar (clock left, data-source label, then Wi-Fi / Bluetooth / VPN / battery icons, then mode and settings) and the same now-playing parts (cover, title, artist, progress, prev / play / next, volume slider). Day/night are palettes, not layouts. Only the selected layout is built, which saves memory.

Offer two or three of these to the user; they differ in what they put first.

| Name | Primary content | Geometry (grid units) | Use when |
|---|---|---|---|
| Graphite | balanced: gauges left, player centre, app tiles right | speed ring card 330x216, RPM bar card 330x128, four 158x100 chips; player card 520x600; 2x3 tiles 162x186 | default, the user wants everything visible |
| Dial (Циферблат) | a big two-ring dial (speed outer, RPM inner) in the middle | rings 500x500 and 412x412 at the centre; four 300x100 chips on the left; title and artist under the dial | the car data is the point |
| Cover-flow | music first: horizontal cover carousel with a row of six 190x100 chips on top | swipe left/right moves the carousel, tap a side card to go to it, tap the centre to launch; keep arrow buttons | music and app switching dominate |
| Rail (Рейка) | navigation first: a 120-wide icon rail on the left and a large "Navigation" card | rail card 120x676 with six 88x88 icons; navigation card 672x616 with 48-unit title | the user lives in the maps app |
| Bento | wallpaper background with glass cards | speed card 300x300, now-playing card 560x300 with 150 cover, app card 336x300 | the user wants a pretty screen; needs the wallpaper veil |
| Sport | tachometer as the hero | tach 560x560 (needle starts at 55% of the radius, no hub dot), speed 96-unit digits inside; four 288x100 chips; player card 590x204; six 190x98 tiles | enthusiast look, fewer widgets |

Common sizes that worked: card radius 28, outer margin 28, tile icon 100, chip value 40-44 units, chip label 32-36 units, title 48 (32 in narrow cards), slider track thickness 0.36 x height with a stronger track colour on light theme.

Per-layout checks: each of the six needs prev/next and volume reachable; the tile that is playing is highlighted; the Sport layout needs its lower tile row filled (empty space reads as a bug).

## Palettes (hex, as used)

| Palette | bg | text / secondary / hint | accent | notes |
|---|---|---|---|---|
| Night | #0b0f17 to black | #c9d2e0 / #95a1b5 / #7f8ba0 | #3f78d8 | icons at 0.7 brightness, wallpaper scrim 0.6 |
| Night+ (warm) | #0b0806 to black | #d9bfa9 / #b89b86 / #a08571 | #c27a3a | icons at 0.55, scrim 0.78, lowest blue light |
| Day | #f3f5f9 to #d5dbe6 | dark text on light cards | blue | contrast >= 4.5:1, white veil 0.45 + 0.45 x dim over wallpapers |

Verify any new palette with `scripts/contrast.py`; the Night hint colour started at 3.19:1 and had to be lightened.

## Modes

Auto / Day / Night / Night+. Auto follows the ambient light sensor when the device has one (the Nexus 7 reported 0 lx during one check, so test Auto with real sensor readings in both light and dark). Brightness is set separately for day and night.
