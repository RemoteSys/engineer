import xmltodict
import csv
import json
from collections import defaultdict
from pathlib import Path

# local imports

import csv_functions as csv_fn
import xml_functions as xml_fn
import json_functions as js_fn
# ---


def my_flat_dict(dc: dict, flat_dc=None) -> dict:
    """Converts a nested dictionary into a flat dictionary of type
    table: {key1: [...], key2: [...]}, where:
      - `keys` are column headings
      - lists [...] are column values."""
    if flat_dc is None:
        flat_dc = defaultdict(list)
        
    for key, val in dc.items():
        if not isinstance(val, (dict, list)):
            if key[0] in ('@', '#'):
                key = key[1:]
            flat_dc[key].append(val)
        elif isinstance(val, dict):
            my_flat_dict(val, flat_dc)
        elif isinstance(val, list):
            for item in val:
                if isinstance(item, dict):
                    my_flat_dict(item, flat_dc)
                else:
                    flat_dc[key].append(item)
    return dict(flat_dc)
# ---
    

def data_type_recognition(path: str):
    suffix = Path(path).suffix
    if suffix == '.xml':
        return from_xml
    elif suffix == '.csv':
        return from_csv
    elif suffix == '.json':
        return from_json
    else:
        return None
# ---


def from_xml(path: str) -> dict:
    data = xml_fn.xml_to_dict(path)
    return data
# ---


def from_csv(path: str) -> dict:
    data = csv_fn.read_csv(path)
    data = csv_fn.csv_to_dict(data)
    name = f"{Path(path).stem}_res.json"
    path = str(Path(path).with_name(name))
    js_fn.save_as_json(data, path) 
    # return data
# ---


def from_json(path: str):
    data = js_fn.read_json(path)
    name = f"{Path(path).stem}_res.csv"
    path = str(Path(path).with_name(name))
    csv_fn.save_as_csv(data, path)
# ---
