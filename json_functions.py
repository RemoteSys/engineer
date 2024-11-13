# coding: utf-8
import json

# ---


def save_as_json(data: dict, path: str, indent=2):
    keys = data.keys()
    rows = zip(*data.values())
    data = [dict(zip(keys, val)) for val in rows]
    with open(path, 'w') as f:
        data_json = json.dump(data, f, indent=indent)
# ---


def read_json(path: str) -> dict:
    with open(path) as f:
        data = json.load(f)
    return data
# ---
