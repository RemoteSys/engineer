import csv
from collections import Counter, defaultdict
from pathlib import Path

            
def scan_csv(path: str, n: int):
    with open(path) as f:
        txt = [f.readline() for _ in range(n)]
    
    txt = ''.join(txt)
    counts = Counter(txt)
    separators = ['.', ',', ';', '\t']
    count_sep = [(s, counts.get(s, 0)) for s in separators]
    sep = max(count_sep, key = lambda item: item[-1])
    count_sep.remove(sep)
    decimal = max(count_sep, key = lambda item: item[-1])
    return sep[0], decimal[0]
    

def convert2numeric(x: str):
    if x.isdigit():
        return(int(x))
    else:
        try:
            return float(x)
        except:
            return x


def read_csv(path: str, n: int = 5) -> list[list]:
    sep, decimal = scan_csv(path, n=n)
    with open(path) as f:
        reader = csv.reader(f, delimiter=sep)
        # reader = csv.DictReader(f, delimiter=delimiter)
        data = []
        for line in reader:
            if decimal != '.':
                line = [l.replace(decimal, '.') for l in line]
            line = [convert2numeric(l) for l in line]
            data.append(line)
        return data
            
            
def csv_to_dict(data: list[list]) -> dict:
    """Converts a list of data of type:
      - [[headers], [values], values],...]
    to a dictionary of columns:
      - {head: [...], head: [...], ...}"""
    data = data[:]
    data_dict = defaultdict(list)
    headers = data.pop(0)
      
    for row in data:
        for key, val in zip(headers, row):
            data_dict[key].append(val)

    return dict(data_dict)
# ---


def save_as_csv(data: dict, path):
    headers = data.keys()
    data = zip(*data.values())

    with open(path, mode='w', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(data)
