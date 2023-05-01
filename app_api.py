# app_api.py
from flask import Flask, request, jsonify
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/echo_api", methods=["POST"])
def echo_api():
    data = request.json
    logger.info("Received request: %s", data)
    return jsonify(data)

@app.route("/health_check", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000

    logger.info("Starting Application API on port %d", port)
    app.run(port=port)
