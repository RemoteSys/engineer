import csv
from collections import Counter
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


def read_csv(path: str, n: int = 5) -> list:
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
            
            
