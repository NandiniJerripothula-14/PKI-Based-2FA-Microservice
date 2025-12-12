#!/usr/bin/env bash
set -e
# Ensure UTC timezone
export TZ=UTC
ln -sf /usr/share/zoneinfo/UTC /etc/localtime || true

# Start cron
cron || true

# Ensure /cron exists
mkdir -p /cron /data

# Run uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port 8080
