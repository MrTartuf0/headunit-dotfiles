#!/bin/bash

STATE_FILE="/tmp/wvkbd_visible"

# Show the keyboard using SIGUSR2
pkill -USR2 wvkbd
# Mark it as visible
touch "$STATE_FILE"
