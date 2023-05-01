# Round Robin API

This project demonstrates a simple implementation of a Round Robin API in Python using Flask. The Round Robin API receives HTTP POST requests and routes them to one of a list of Application APIs.

## Project Structure

.
├── app_api.py
├── round_robin.py
├── start_all.sh
└── stop_all.sh

- `app_api.py`: Simple Application API with one endpoint that accepts an HTTP POST with any JSON payload and responds with the same payload.
- `round_robin.py`: Round Robin API that receives HTTP POST requests and forwards them to one of the Application API instances on a round-robin basis.
- `start_all.sh`: Shell script to start multiple instances of the Application API and the Round Robin API.
- `stop_all.sh`: Shell script to stop all instances of the Application API and the Round Robin API.

## Requirements

- Python 3.6 or later
- Flask
- Requests

## Installation

1. Clone this repository:

2. Create a virtual environment and activate it:
    > python3 -m venv venv
    > source venv/bin/activate

3. Install the required packages:
    > pip install -r requirements.txt


## Usage

1. Start multiple instances of the Application API and the Round Robin API using the `start_all.sh` script:
> `./start_all.sh`

2. Send an HTTP POST request to the Round Robin API with a JSON payload:
> `curl -X POST -H "Content-Type: application/json" -d '{"game":"Mobile Legends", "gamerID":"GYUTDTE", "points":20}' http://localhost:4000/echo_api`

- The Round Robin API will forward the request to one of the Application API instances and return the response.

3. To stop all instances of the Application API and the Round Robin API, use the `stop_all.sh` script:
> `./stop_all.sh`