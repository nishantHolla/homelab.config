#!/bin/sh

CONFIG_FILE="/etc/sysctl.d/99-syncthing.conf"

sudo tee "$CONFIG_FILE" >/dev/null <<'EOF'
fs.inotify.max_user_watches=1048576
fs.inotify.max_user_instances=8192
fs.inotify.max_queued_events=65536
EOF

sudo /usr/sbin/sysctl --system
