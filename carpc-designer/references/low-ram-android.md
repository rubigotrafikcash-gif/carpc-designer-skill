# Low-RAM Android in a car: what was measured

Device: Nexus 7 2012 3G (tilapia), Android 7.1.2, armeabi-v7a, about 1 GB RAM, 1280x800, 213 dpi. Numbers below were measured on it in September-October 2026. They are not universal; re-measure on other hardware (`dumpsys meminfo`, `free`, `logcat`).

## Memory and speed

- Typical working set after boot with maps + music + VPN: about 40 MB free, about 330 MB cache, swap in use. Largest processes: maps about 178 MB, music about 111 MB.
- Draw with custom Canvas views and build only the selected layout; avoid heavyweight UI libraries.
- Ahead-of-time compile slow apps: `cmd package compile -m speed-profile -f <package>` (undo: `cmd package compile --reset <package>`). It fixed a music app that started slowly because it was interpret-only. Repeat after an app update.
- Developer option "background process limit = 1" freed memory (free 114 to 379 MB) but kills cached processes of maps/music/VPN and resets on reboot; the project decided not to rely on it. Instead the launcher stops other players when one starts and leaves background services (VPN) alone.
- Cold start of the maps app: 14.6 s alone, 28.2 s with another player running, 40.5 s with three apps running. Design the autostart order around that.

## Boot and autostart

- Make the launcher the HOME app (`cmd package set-home-activity <component>`); a custom launcher then starts at boot and can run the sequence once per boot (guard with `SystemClock.elapsedRealtime()` stored in prefs, and only in the first 10 minutes of uptime).
- Verified order (two reboots): maps at +15 s, then music about 26 s later (play command sent to that player's MediaSession, retried), then maps brought back to the front. Music keeps playing while maps is on top.
- Do not send `KEYCODE_MEDIA_PLAY` to start music: Android hands it to the last media-button receiver (after reboot that was VLC, which grabbed audio focus). Use `MediaController.getTransportControls().play()` for the specific package (needs notification-listener access).
- After a reboot the tablet shows a swipe lock screen; apps already run under it. Disabling the lock is a security decision for the owner; offer it, do not do it silently.
- Heavy initialisation at boot (a 100 MB speech model) made the launcher show "Application not responding" while the load average was above 4. Fixes that worked: start it 60 s after the launcher, give the loading thread background priority, keep it in a separate process.

## Privileged install for process control

A normal app cannot reliably stop a music player that runs a foreground service. Installing the launcher as a privileged system app (`/system/priv-app/<app>/`, requires remounting /system, so the owner decides) lets it hold `FORCE_STOP_PACKAGES`. Verified: force-stop of the music player worked. Installing a newer build as a normal update on top kept the privilege.

## Screen on 24/7

Use `FLAG_KEEP_SCREEN_ON` on the launcher window; the system setting `stay_on_while_plugged_in=3` was already on. Verified through the wake lock (`SCREEN_BRIGHT_WAKE_LOCK`) held by the window.

## adb and automation traps

- `am start --ei layout N` does not rebuild an already-running activity; force-stop first.
- Injecting `input tap` while the app is still starting causes an ANR ("no window has focus"); wait until the window is up.
- Swipe to unlock: `input swipe 640 700 640 150 300`. `input text` needs `%s` for spaces.
- Screenshot-driving scripts change device state (they cycled the day/night mode and once started a video). Read the prefs before and after, and restore.
- Toasts disappear before a screenshot; verify them through logcat or by their code path.
- On the Windows host: adb may not be on PATH; PowerShell `-Command` inline strips `$`, so put scripts in `.ps1` files; scripts that contain Cyrillic must be saved with a BOM or read the text from a UTF-8 file with `Get-Content -Encoding UTF8`, otherwise PowerShell 5 reads it as ANSI and mangles it.
- Build without Gradle: aapt2 link, javac `--release 8`, d8 (`--min-api 24`), zipalign, apksigner. Native libraries go into `lib/armeabi-v7a/` of the APK.
