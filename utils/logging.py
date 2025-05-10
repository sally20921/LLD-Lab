import os
import json
from datetime import datetime

# LOG_DIR = "data/logs"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "data", "logs")
LOG_DIR = os.path.abspath(LOG_DIR)


def log_run(result_dict):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    path = os.path.join(LOG_DIR, f"{timestamp}.json")
    with open(path, "w") as f:
        json.dump(result_dict, f, indent=2)
    return path

def list_logs():
    return sorted(os.listdir(LOG_DIR))

def read_log(filename):
    path = os.path.join(LOG_DIR, filename)
    with open(path) as f:
        return json.load(f)

