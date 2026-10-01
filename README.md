# carpc-designer

A Claude skill for designing and reviewing in-car head-unit / Car PC interfaces on Android tablets and low-RAM devices: launcher, "now playing", OBD2 gauges, status bar, day/night themes. It applies automotive norms (Google Design for Driving, NHTSA glance limits) instead of phone-app rules.

Навык Claude для проектирования и проверки интерфейса автомобильного планшета (Car PC): лаунчер, «сейчас играет», приборы OBD2, строка состояния, день/ночь. Опирается на автомобильные нормы, а не на правила мобильных приложений.

Built from a real project: a Nexus 7 2012 (Android 7.1.2, 1 GB RAM) in a Lada Granta. Everything marked "measured" in the references was checked on that device; untested items are labelled as such.

## What is inside

```
carpc-designer/
  SKILL.md                      workflow, rules, triggers (EN, with RU trigger words)
  references/
    automotive-rules.md         sizes, contrast, glance limits, sources, dp to px
    layouts.md                  six layout archetypes, palettes, modes
    review-checklist.md         review pass for real screenshots
    low-ram-android.md          memory, boot/autostart, priv-app, adb traps
    voice-and-controls.md       offline voice (Vosk) and BT remote notes
  scripts/
    contrast.py                 WCAG contrast checker (pairs or JSON palette)
    dp_px.py                    dp/px converter and automotive minimums
```

## Install

Claude Code: copy the `carpc-designer` folder to `~/.claude/skills/` (or `.claude/skills/` in a project). Claude.ai / Cowork: zip the `carpc-designer` folder as `carpc-designer.skill` and upload it in Settings, Skills.

## Use

Ask in plain words, for example: "review this car-screen screenshot against automotive rules", "design a night mode for my Car PC launcher", "почему на планшете в машине неудобно читать скорость". Run the helpers directly:

```
python3 carpc-designer/scripts/dp_px.py 213
python3 carpc-designer/scripts/contrast.py "#c9d2e0" "#0b0f17"
```

## Sources and honesty notes

Numbers (32/24 dp text, 76 dp targets, 4.5:1 contrast, night polarity) were re-fetched from Google Design for Driving on 2026-10-01. The 23 dp target gap is a working value that could not be re-confirmed. NHTSA limits are quoted from the project's notes. Steering-wheel Bluetooth remotes and in-car voice accuracy were not tested. The reference project (a Music Box launcher for the tablet) is a separate, private repository.

License: MIT.
