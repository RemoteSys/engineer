import xmltodict
from collections import defaultdict

# local imports
from functions import my_flat_dict
# ---

def xml_to_dict(path: str) -> dict:
    with open(path, "r") as f:
        data = xmltodict.parse(f.read(),dict_constructor=dict)

    data = my_flat_dict(data)
    return data
