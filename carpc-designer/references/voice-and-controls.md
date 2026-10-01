# Hands-free control

## Offline voice (Vosk) - what was built and measured

Engine: Vosk 0.3.47 (Android AAR + JNA 5.13.0), Russian small model `vosk-model-small-ru-0.22` (46 MB zip, about 90 MB unpacked). Runs in its own process as a foreground service so the UI stays light.

Design:
- Use a **grammar**: only the phrases "wake word + command" plus `[unk]`. Anything else (radio, chatter) becomes `[unk]` and is dropped. In free dictation the model heard the made-up wake word "Nexus" as "ник соус", but inside a grammar it worked; the plain word "компьютер" was recognised reliably. Keep two wake words.
- Validate the wake word yourself. A first version split the result and took the second word as the command without checking the first; the phrase "на играть" triggered Play. Always require the exact wake word.
- Require a per-word confidence (>= 0.55 was used) and ignore repeats for 1.5 s.
- Confirm with a short tone and an on-screen toast.
- Commands: next / previous / pause / play, volume up / down (via AudioManager), maps, music (starts the last player and sends play to its MediaSession), home.
- Load the model with low thread priority, start the service about 60 s after the launcher, and offer a settings toggle.
- Media actions go through MediaController of the playing session (the app already has notification-listener access for "now playing"); do not send media keys.

Measured on the Nexus 7: model load 7-14 s, process memory about 130-170 MB. With clean synthetic speech (Windows SAPI voice Irina, 16 kHz mono PCM fed to the service) 6 of 6 commands were recognised and phrases without the wake word were ignored; volume and VLC pause/play/next were verified. **Not verified:** real voices, engine noise at speed, the single weak tablet microphone, and memory behaviour with maps + two players running. If accuracy is poor in the car, an external USB or Bluetooth microphone near the mirror is the next step.

Test harness idea: add a debug intent extra that feeds a raw 16 kHz mono 16-bit PCM file to the recogniser instead of the microphone, generate phrases with a TTS voice, and read the results from logcat. Watch text encoding in the generator script (see low-ram-android.md).

## Bluetooth steering-wheel media remote (not tested)

Typical clip-on wheel remotes send standard media keys (play/pause, next/previous, volume) over Bluetooth (AVRCP or HID). Android delivers media keys to the active media session, so the music apps should react without any code in the launcher. This is general Android behaviour, **not tested in this project**. Before buying, check the profile (classic HID/AVRCP vs BLE-only) against the device's Bluetooth support, and prefer a seller with returns. Volume buttons may change Bluetooth volume rather than the system music volume; test with the actual device.
