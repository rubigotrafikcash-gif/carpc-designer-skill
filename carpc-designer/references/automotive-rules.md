# Automotive UI rules (with sources)

Collected in September 2026; on 2026-10-01 the text-size, contrast, touch-target and night-polarity numbers were re-fetched from the two Google pages cited below and matched. The gap value is marked where it could not be re-confirmed. Re-check sources before quoting them in a deliverable; guidelines change.

## Sizes (Google Design for Driving)

| Element | Minimum | Notes |
|---|---|---|
| Primary text | 32 dp | Google: "should be 32dp" (song titles, contact names, info needed for decisions) |
| Secondary text | 24 dp | Google: "should be 24dp" (artist name, supporting info); treat as a floor |
| Touch targets | 76 x 76 dp | Google: minimum touch-target size in Android for Cars; applies to prev/next and slider hit areas |
| Gap between targets | 23 dp | from the project's earlier notes; NOT re-confirmed on the sizing page, treat as a working value |
| Contrast | 4.5 : 1 | Google: for icons, text and other images; apply to hints too |

Night: Google requires negative polarity at night (light content on a dark background); day may be either. One accent colour and a gentle day/night transition are the project's own conclusions from the same material.

Sources:
- https://developers.google.com/cars/design/design-foundations/visual-principles
- https://developers.google.com/cars/design/automotive-os/design-system/sizing

## Driver distraction (NHTSA visual-manual guidelines)

- A single glance away from the road <= 2 s; total glance time for a task <= 12 s.
- Block video playback, text entry and long text while the vehicle moves.
- Operation should be possible with one hand.

Source: https://www.nhtsa.gov/document/visual-manual-nhtsa-driver-distraction-guidelines-vehicle-electronic-devices-0

## Structure ideas from OEMs

- BMW iDrive: flat structure ("zero layer"), configurable widgets, driver instruments in front of the driver (BMW press release T0410078EN).
- Mercedes MBUX: no confirmed source was found in the project, so nothing is claimed.

## dp to px

px = dp x dpi / 160. Use `scripts/dp_px.py <dpi>` to print the table. For the Nexus 7 2012 (213 dpi, factor 1.33): 24 dp = 32 px, 32 dp = 43 px, 76 dp = 101 px, 23 dp = 31 px.

Trap: a design grid in "reference px" (the project used 1280x736 scaled to the screen) is not dp. A 76-unit button on that grid is about 57 dp on the 213 dpi screen, below the 76 dp minimum (the project's prev/next buttons are 72-96 units, about 54-72 dp). Convert before declaring a target compliant.

## Phone-design skills: what transfers and what does not

Three open-source mobile design skills were run over the mockups (awesome-skills/mobile-app-design, ceorkm/mobile-app-ui-design, nextlevelbuilder/ui-ux-pro-max-skill). What transferred: contrast checking, "no emoji as icons", "swipe-only carousel is bad", scrim under the status bar over bright wallpapers. What did not: button sizes of 44/48 and 16 px text (phone norms, too small for a car), and the web-oriented design-system generator, which returned an unrelated landing-page pattern for "car infotainment". Useful from it: "Dark Mode (OLED)" and the warning about poor audio players.
