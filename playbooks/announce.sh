#!/bin/bash

# Check if host is online
ping -c 1 google.com > /dev/null

if [ $? -eq 0 ]; then
    # Host is online, send message to provisioning server
    curl -X POST -d "`hostname` is online" http:/ip:8000
else
    # Host is offline, do nothing
    exit 0
fi
