import json
import os
from app.config import RESULTS_PATH

def load_results():
    if not os.path.exists(RESULTS_PATH):
        return []

    with open(RESULTS_PATH, "r") as f:
        return json.load(f)


def save_result(data):
    results = load_results()
    results.append(data)

    with open(RESULTS_PATH, "w") as f:
        json.dump(results, f, indent=4)

    return {"message": "Stored successfully"}