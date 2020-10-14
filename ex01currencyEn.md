# Task 1

Write a script giving current currency and gold rates downloaded from the website. Functionality of the script:

  - displays the entire table of currency rates
  - displays the rate of a single currency
  - displays the current price of gold

Banking service providing data [NBP](http://api.nbp.pl/)

# Scope of the task

  1. Importing modules
  2. module [urllib.request](#module_urllib.request )
  3. [File formats](#json_csv) `json` and `csv`
  2. [Scripts](#scripts)



# 1. Importing modules

Ways to import modules:

### 1.1. Importing the whole module
Import (sample) module from standard library `sys`:

```python
import sys
```

> ,,This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available''

(from *https://docs.python.org/3/library/sys.html*)

In this case, you can access the module objects by entering the name of the imported module, dot sign and function/class name, e.g:

```python
sys.path[0]
```


### 1.2. Importing all module functionalities

Import all mathematical functions from the module `math`:

```python
from math import *
```

> ,,This module provides access to the mathematical functions defined by the C standard.''

(from *https://docs.python.org/3/library/math.html*)



### 1.3. Importing selected module functionalities

Import the cosine function from the module`math`:
```python
from math import cos
```

Using the imported function comes down to calling it with an appropriate argument:
```python
cos(3.14)
```



### 1.4. Import with name change - alias

Import the `numpy` module with an alias `np`: 
```python
import numpy as np
```

> ,,NumPy (Numerical Python) is an open source Python library that’s used in almost every field of science and engineering.''

(from *https://numpy.org/doc/stable/user/absolute_beginners.html*)


#### 1.5. Importing custom modules

A simple way to import your own modules, which do not have to be permanently available, is to add their directory address to the temporary search path. Example:

  - a directory has been created for the temporary modules `c:/myTmpModule`.
  - a temporary module (file) `foo.py` was created in the directory `c:/myTmpModule`.
  - import:

```python
#adds the search directory address
sys.path.append('c:/myTmpModule')

# import
import foo

```

#### 1.6.Re-loading the module

While working with the program code, changes are made. For the changes to be "noticed" in the system, it is necessary to reload the module in which the changes were made. The function `reload()` from the module `importlib` is used for this task:

```python
# import of functions
from importlib import reload

#using a function on a fictional 'myMod' module
reload(myMod)

```
Information about the module `importlb`: *https://docs.python.org/3/library/importlib.html*



# 2.  Module urllib.request 

>,,The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.''

(from *https://docs.python.org/3/library/urllib.request.html#module-urllib.request*)

Basic use of the module:

  - `urllib.request.urlopen()` - wysyłanie zapytania  
  - `.read()` - metoda obiektu `urllib.request.urlopen()` wczytująca otrzymane dane
  - `.decode()` - metoda konwertująca typ danych `bajt` na `str`


# 3. JSON CSV

About `json`:
>,,JavaScript Object Notation (JSON, pronounced /ˈdʒeɪsən/; also /ˈdʒeɪˌsɒn/[note 1]) is an open standard file format, and data interchange format, that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and array data types (or any other serializable value). It is a very common data format, with a diverse range of applications, such as serving as a replacement for XML in AJAX systems.''

(from *https://en.wikipedia.org/wiki/JSON*)


About `csv`
>,,A comma-separated values (CSV) file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format. A CSV file typically stores tabular data (numbers and text) in plain text, in which case each line will have the same number of fields.''

(from *https://en.wikipedia.org/wiki/Comma-separated_values*)


#### 3.1. Modules

  - `json` - json encoder and decoder. Moduł biblioteki standardowej, wymaga zaimportowania:  `import json`
  - `csv` - csv file reading and writing. Moduł biblioteki standardowej,  wymaga zaimportowania:  `import csv`




# Scripts

Basic information about creating scripts can be found in the  [GitHub](https://github.com/RemoteSys/entry/blob/master/scriptsInfo.md).

An example of a simple script can be found in the file at [GitHub](https://github.com/RemoteSys/entry/blob/master/testScript.py).

