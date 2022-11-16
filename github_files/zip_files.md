# Zip archives

You can read about what a zip archive is here: [Wikipedia](https://en.wikipedia.org/wiki/ZIP_(file_format))

Python has a `zipfile` module from the standard library to handle zip archives - [see doc](https://docs.python.org/3/library/zipfile.html)


# Basic usage

 - module import: `import zipfile`
 - archive content view: 
 ```python
with zipfile.ZipFile('archive_path.zip') as fz:
    fz.printdir()
 ```

 - get a list of files from the archive:
 ```python
with zipfile.ZipFile('archive_path.zip') as fz:
    file_list = fz.namelist()
 ```

 - reading data from a csv file without unpacking the archive:
 ```python
 import pandas as pd

 with zipfile.ZipFile('archive_path.zip') as fz:
    # for example, the first file in the file list
    file_name = file_list[0]
    csv_file = fz.open(file_name)
    df = pd.read_csv(csv_file)
```

 - extract the selected file from the archive:
```python
with zipfile.ZipFile('archive_path.zip') as fz:
    file_name = file_list[0]
    fz.extract(file_name, path='destination_dir')
```

 - extract all files with `extractall()` method.


# Coding trouble

Sometimes a different character encoding was used to save the data than on our computer.
It is possible to use python to recognize the encoding:

- module [chardet](https://chardet.readthedocs.io/en/latest/index.html)
- module installation: `conda install -c conda-forge chardet`
- using the module by reading data in binary mode:
 ```python
 import chardet

 coding_list = []

 with open('file_path','rb') as f:
    for l in f:
        info = chardet.detect(l) # this is dict
        coding_list.append(info['encoding'])

 coding_list = list(set(coding_list))
 ```

 - the `coding_list` contains the names of the encodings detected in the file, which can be used 
   to read the file by specifying the `encoding = coding_name` argument, e.g. `open(file_path, 
   encoding = coding_name)`.
