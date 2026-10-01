---
name: carpc-designer
description: >-
  Designs, builds and reviews in-car head-unit and Car PC interfaces for Android tablets and low-RAM devices (launcher / "now playing" / OBD gauges / status bar), applying automotive UX norms (Google Design for Driving and NHTSA glance limits) instead of phone-app rules. Use this skill whenever the user mentions a Car PC, head unit, car tablet, in-car launcher, dashboard for a car, infotainment, OBD2 gauges screen, "Music Box", Nexus 7 in a car, day/night mode for a car screen, or asks to review or improve a car UI screenshot, even if they only say "make it readable while driving". Также: автомобильный интерфейс, автомагнитола на Android, планшет в машине, лаунчер для авто, приборная панель на экране, ночной режим для авто, проверить дизайн под требования автоконцернов.
---

# CarPC designer

Design and review interfaces that people read in 1-2 second glances while driving, on small, old, memory-starved Android hardware. This skill comes from building a real launcher ("Music Box") for a Nexus 7 2012 (Android 7.1.2, 1 GB RAM, 1280x800) in a Lada Granta; everything marked *measured* below was checked on that device.

## Why this is not ordinary mobile design

Phone and web design skills assume a hand-held screen at 40 cm: 44-48 px buttons, 16 px text. A dashboard screen is 60-90 cm away, touched with a gloved or shaking hand, and looked at between glances at the road. So: bigger type, bigger targets, fewer things per screen, no gestures as the only way to act, and a night palette that does not blind. When a phone-design checklist and an automotive number disagree, the automotive number wins. Read `references/automotive-rules.md` for the numbers and their sources before judging any layout.

## Workflow

1. **Pin the screen facts first.** Resolution, dpi, orientation, safe areas (status/nav bars), RAM, Android version. Convert norms from dp to px with `scripts/dp_px.py` (px = dp x dpi / 160; at 213 dpi, 76 dp is about 101 px and 24 dp about 32 px). Everything else depends on this; a design done in "px of a mockup" silently breaks the norms on the real screen.
2. **Choose a layout archetype** from `references/layouts.md` (six proven ones: Graphite, Dial, Cover-flow, Rail, Bento, Sport). Offer 2-3 to the user rather than inventing a seventh; they differ in what is primary (gauges, music, navigation shortcuts).
3. **Build on a reference grid.** Design on one fixed grid (the project used 1280x736) and scale to the real screen, so spacing stays even. Use one accent colour, day/night as palettes rather than separate layouts, and the same status bar on every layout.
4. **Handle data honestly.** No adapter or no signal shows "--" and a visible state label ("нет адаптера", "ЭБУ спит"), never plausible fake numbers. A demo mode is allowed only if it is off by default and labelled on screen.
5. **Run the review pass** in `references/review-checklist.md` on real screenshots (not mockups): contrast with `scripts/contrast.py`, text sizes, target sizes, spacing, empty and off states, day and night.
6. **Fix everything the checklist finds in one batch**, then re-screenshot. Say what was fixed and what was left (with the reason) so the user can decide.
7. **Check it on the device.** A change that looks right in code can be invisible or broken on screen (see the wallpaper-veil lesson below). Take a screenshot via `adb shell screencap -p`, look at it, and restore the device state you changed (mode, brightness, active app).

## Rules that repeatedly mattered

- **Show state changes visibly.** If a control changes something, the change must be visible at the setting you ship. In the project, wallpaper swatches seemed to do nothing because a "background dimming" slider sat at 90% and hid them. Default the slider to a value where every option is visible and label what the slider does.
- **Off and disabled states need a shape, not only a colour.** Wi-Fi/Bluetooth/VPN off = the same glyph with a slash, plus lower contrast. A VPN key that is crossed out when off matches what Android and VPN apps show.
- **Spacing is a feature.** Status-bar icons need equal gaps and consistent sizes; uneven spacing was the first thing the user noticed.
- **Every swipe has a button.** Carousels get visible arrows; swipe is an accelerator, not the only path.
- **Long text scrolls, then stops.** Marquee a few passes (the project used 5) and rest, otherwise it competes for the driver's attention.
- **Night is near-black with light text, one warm option.** A warm "Night+" palette with lower contrast and dimmer icons exists for dark roads; keep text still >= 4.5:1.
- **Light theme needs its own veil.** Over wallpapers use a veil whose strength follows the user's dim slider in both themes (night = dark veil, day = white veil), or the wallpaper will either vanish or make text unreadable.
- **No video, no text entry while moving.** Route searching and typing to the parked state.

## Low-RAM and device pitfalls (measured)

Read `references/low-ram-android.md` before shipping anything that starts at boot. Key facts: heavy initialisation at boot starves the UI (an "Application not responding" appeared when a 100 MB voice model loaded during start-up; delaying it 60 s and lowering thread priority fixed it); autostart order matters (maps cold start 14.6 s alone, 28 s with a music app, 40 s with three apps); a launcher installed as a privileged system app can force-stop other players; keep-screen-on while powered is a window flag, not a system setting.

## Voice and steering-wheel control

For hands-free control read `references/voice-and-controls.md`: offline Vosk with a grammar of "wake word + command" worked on synthetic speech; real in-car noise is untested, and it explains why a Bluetooth media remote is the dependable fallback.

## Output when reviewing

Give a short table: finding, where, rule violated (with number), fix. Then say which items you changed and which you did not, and attach the before/after screenshot. Do not invent measurements; if something was not measured on the device, say so.

## Bundled files

- `references/automotive-rules.md`: sizes, contrast, glance limits, sources, dp to px table.
- `references/layouts.md`: the six layout archetypes with grid geometry and when to use each.
- `references/review-checklist.md`: the automotive and accessibility pass, with the findings that came up in practice.
- `references/low-ram-android.md`: memory, boot, autostart, priv-app, adb automation traps.
- `references/voice-and-controls.md`: voice control design and Bluetooth remote notes.
- `scripts/contrast.py`: WCAG contrast ratio checker for colour pairs or a JSON palette.
- `scripts/dp_px.py`: dp/px converter and the automotive minimums in px for a given dpi.
