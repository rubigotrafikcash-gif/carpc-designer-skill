# Review checklist for a car UI (run on real screenshots)

Do the pass on screenshots from the device (`adb shell screencap -p`), not on mockups: scaling, anti-aliasing and real data change the result. Check day and night, and every layout.

## 1. Legibility
- [ ] Primary text >= 32 dp, secondary >= 24 dp (convert from px with `scripts/dp_px.py`). Nothing smaller, including chip labels, app-tile labels and toasts. In the project, labels were raised from small sizes to 32-36 units.
- [ ] Contrast >= 4.5:1 for every text/background pair, including hints, disabled text and toasts. Use `scripts/contrast.py`. A toast was too faint until it got an opaque dark rounded background with a light stroke.
- [ ] Text over wallpapers: a veil or scrim guarantees contrast; a scrim under the status bar on bright wallpapers.
- [ ] Slider tracks are visible on both themes (light theme: a stronger track colour than the dark theme's translucent white).

## 2. Targets and spacing
- [ ] Every control >= 76 dp with >= 23 dp gaps. Known gap in the project: prev/next buttons are 72-96 px, about 54-72 dp on the real screen, so some are under the minimum. Record gaps you do not fix.
- [ ] Whole slider track is tappable, not only the knob (verify instead of assuming; an earlier wrong assumption in the project was corrected after a test).
- [ ] Equal gaps and equal icon sizes in the status bar.
- [ ] Even inner padding in cards; content centred in its card.

## 3. State and data honesty
- [ ] Every status icon has an off state that differs by shape (slash) and not only by colour.
- [ ] No data shows "--" plus a state label; no fake numbers. Demo mode is off by default and labelled.
- [ ] Battery shows percent with a charging bolt; if there is no battery, show a plug glyph.
- [ ] VPN uses the key glyph (crossed-out when off).

## 4. Interaction
- [ ] No gesture-only actions; carousels have arrows.
- [ ] No text entry, video or long text reachable while driving.
- [ ] Settings overlay is opaque (a translucent settings panel showed the main screen through it and looked broken).
- [ ] Each setting visibly changes something at the shipped default value.

## 5. Visual details that looked wrong in practice
- Tachometer needle with a hub dot overlapping the speed digits: start the needle at ~55% of the radius and drop the hub.
- Glyph artefacts (a music-note icon drew a stray shape); check every icon at screenshot scale.
- Empty areas on dense layouts (Sport) read as a bug; fill or rebalance.
- Icons of apps with adaptive/vector launcher icons cannot always be rasterised; use the real PNG when available, otherwise a clearly approximate glyph and say so.

## 6. Reporting
Table: finding | screen | rule | fix. Mark each finding fixed / not fixed (with reason). Never claim something is verified unless you looked at the screenshot after the change.
