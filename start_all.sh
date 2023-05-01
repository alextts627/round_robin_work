#!/bin/bash

# Replace 'your_app_api_script.py' with the actual name of your Application API script
# Start Application API instances
python3 app_api.py 5001 &
python3 app_api.py 5002 &
python3 app_api.py 5003 &

# Start the Round Robin API
python3 round_robin.py
