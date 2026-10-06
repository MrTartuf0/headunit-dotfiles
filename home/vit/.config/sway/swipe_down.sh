#!/bin/bash

# We use this file to track whether the keyboard is visible
STATE_FILE="/tmp/wvkbd_visible"

if [ -f "$STATE_FILE" ]; then
    # Keyboard is visible, so hide it
    pkill -USR1 wvkbd
    rm -f "$STATE_FILE"
else
    # Keyboard is NOT visible, go to workspace 2 (Custom Webapp)
    swaymsg workspace 2
fi
