#!/bin/sh

ports="5000 5001 5002 5003"

for port in $ports; do
    pid=$(lsof -ti :$port)
    if [ -n "$pid" ]; then
        echo "Stopping instance on port $port"
        kill $pid
    else
        echo "No instance found on port $port"
    fi
done
