#!/bin/bash
COMMAND=$1
for player in $(dbus-send --print-reply --dest=org.freedesktop.DBus /org/freedesktop/DBus org.freedesktop.DBus.ListNames | awk '/org.mpris.MediaPlayer2./ { print $2 }' | tr -d '"'); do
    dbus-send --print-reply --dest=$player /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.$COMMAND
done
