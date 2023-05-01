# round_robin.py
from flask import Flask, request, jsonify
import requests
from queue import Queue
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Read the configuration file
with open('config.json', 'r') as f:
    config = json.load(f)

# Get the Application API instances from the configuration
application_api_instances = config['application_api_instances']

instance_queue = Queue()
for instance in application_api_instances:
    instance_queue.put(instance)

def get_next_application_api_instance():
    for _ in range(len(application_api_instances)):
        instance = instance_queue.get()
        instance_queue.put(instance)
        if is_instance_healthy(instance):
            return instance
    return None

def is_instance_healthy(instance):
    try:
        response = requests.get(f"{instance}/health_check", timeout=5)
        if response.status_code == 200 and response.json().get("status") == "healthy":
            return True
    except requests.exceptions.RequestException:
       logger.error("Application API instance is not healthy: %s", instance)
    return False


@app.route("/echo-api", methods=["POST"])
def round_robin_api():
    data = request.get_json()
    application_api_instance = get_next_application_api_instance()

    if application_api_instance:
        try:
            response = requests.post(f"{application_api_instance}/echo_api", json=data, timeout=5)
            response.raise_for_status()
            json_response = response.json()
            if response.status_code == 200:
                logger.info("Application API instance responded successfully: %s", application_api_instance)
                return jsonify(json_response)
        except requests.exceptions.RequestException:
            # Log or handle the exception as needed
            logger.error("Application API instance did not respond: %s", application_api_instance)
    return "All application API instances are unavailable or not responding.", 500

if __name__ == "__main__":
    logger.info("Starting Round Robin API")
    app.run(port=4000)
