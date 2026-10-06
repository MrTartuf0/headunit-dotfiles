#!/bin/bash

# Definiamo i flag globali in una variabile di bash
FLAGS="--disk-cache-dir=/tmp/chromium-cache --disk-cache-size=104857600 --enable-features=UseOzonePlatform --ozone-platform=wayland --ignore-gpu-blocklist --enable-gpu-rasterization --enable-zero-copy --disable-features=OverscrollHistoryNavigation,Translate --disable-pinch --overscroll-history-navigation=0 --disable-background-networking --disable-ipc-flooding-protection --js-flags=--max-old-space-size=512"

# Avvia il server backend della Dashboard
pkill -f dashboard.py
python3 /home/vit/.config/sway/dashboard.py &

# 1. Avvia la Dashboard (T=0)
chromium $FLAGS --app=http://localhost:8080 &

# Auto launch disabilitati come richiesto dall'utente:
#
# 2. Avvia Spotify (T=4 secondi)
# sleep 4
# chromium $FLAGS --app=https://open.spotify.com &
#
# 3. Avvia YouTube Mobile (T=8 secondi)
# sleep 4
# chromium $FLAGS --user-agent="Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36" --app=https://m.youtube.com &
