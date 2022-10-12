# Zadanie 1

Napisać skrypt podający bieżące kursy walut pobrane z serwisu internetowego. Funkcjonalność skryptu:

  - wyświetla kurs pojedynczej waluty
  - wyświetla całą tabelę kursów walut

 

Serwis bankowy udostępniający dane: [NBP](http://api.nbp.pl/)

# Zakres ćwiczenia

  1. Importowanie modułów
  2. Moduł [requests](#moduł_requests)
  3. Formaty [plików](#json_csv) `json` i `csv`
  2. [Skrypty](#skrypty)



# 1. Importowanie modułów

Sposoby importowania modułów:

### 1.1. Import całego modułu
Importuj (przykładowy) moduł z biblioteki standardowej `sys`:

```python
import sys
```

> ,,This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available''

(from *https://docs.python.org/3/library/sys.html*)


W tym przypadku dostęp do funkcji/klas/podmodułów dokonuje się poprzez podanie nazwy zaimportowanego modułu, znaku kropki i nazwy funkcji/klasy np.:

```python
sys.path[0]
```


### 1.2. Importowanie wszystkich funkcjonalności modułu

Zaimportuj wszystkie funkcje matematyczne z modułu `math`:

```python
from math import *
```

> ,,This module provides access to the mathematical functions defined by the C standard.''

(from *https://docs.python.org/3/library/math.html*)



### 1.3. Importowanie wybranych funkcjonalności modułu

Zaimportuj funkcję cosinus z modułu `math`:
```python
from math import cos
```

Użycie zaimportowanej funkcji sprowadza się do jej wywołania z odpowiednim argumentem:

```python
cos(3.14)
```



### 1.4. Importowanie ze zmianą nazwy - aliasem

Zaimportuj moduł `numpy` z aliasem `np`: 
```python
import numpy as np
```

> ,,NumPy (Numerical Python) is an open source Python library that’s used in almost every field of science and engineering.''

(from *https://numpy.org/doc/stable/user/absolute_beginners.html*)


#### 1.5. Importowanie modułów własnych

Prostym sposobem importu własnych modułów, które nie muszą być na stałe dostępne jest dodanie do tymczasowej ścieżki wyszukiwania adresu ich katalogu. Przykład:  

  - utworzono katalog na tymczasowe moduły `c:/myTmpModule`
  - utworzono tymczasowy moduł(plik) `foo.py` w katalogu `c:/myTmpModule`
  - importowanie:

```python
#dodaje adres katalogu wyszukiwania
sys.path.append('c:/myTmpModule')

# import
import foo

```

#### 1.6. Przeładowanie modułu

Podczas pracy z kodem programu, dokonywane są zmiany. Aby zmiany zostały "zauważone" w systemie konieczne jest ponowne załadowanie modułu, w którym dokonano zmian. Do tego zadania używana jest funkcja `reload()` z modułu `importlib`:

```python
# import funkcji
from importlib import reload

#użycie funkcji na fikcyjnym module 'myMod'
reload(myMod)

```
Informacje o module `importlb`: *https://docs.python.org/3/library/importlib.html*



# 2.  Moduł urllib.request 

>,,The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.''

(from *https://docs.python.org/3/library/urllib.request.html#module-urllib.request*)

Podstawowe wykorzystanie modułu:

  - `urllib.request.urlopen()` - wysyłanie zapytania  
  - `.read()` - metoda obiektu `urllib.request.urlopen()` wczytująca otrzymane dane
  - `.decode()` - metoda konwertująca typ danych `bajt` na `str`


# 3. JSON CSV

O formacie `json`:
>,,JavaScript Object Notation (JSON, pronounced /ˈdʒeɪsən/; also /ˈdʒeɪˌsɒn/[note 1]) is an open standard file format, and data interchange format, that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and array data types (or any other serializable value). It is a very common data format, with a diverse range of applications, such as serving as a replacement for XML in AJAX systems.''

(from *https://en.wikipedia.org/wiki/JSON*)


O formacie `csv`
>,,A comma-separated values (CSV) file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format. A CSV file typically stores tabular data (numbers and text) in plain text, in which case each line will have the same number of fields.''

(from *https://en.wikipedia.org/wiki/Comma-separated_values*)


#### 3.1. Moduły

  - `json` - json encoder and decoder. Moduł biblioteki standardowej, wymaga zaimportowania:  `import json`
  - `csv` - csv file reading and writing. Moduł biblioteki standardowej,  wymaga zaimportowania:  `import csv`




# 4. Skrypty

Podstawowe informacje o tworzeniu skryptów zawiera dokument znajdujący się w serwisie [GitHub](https://github.com/RemoteSys/entry/blob/master/scriptsInfo.md).

Przykład prostego skryptu znajduje się w pliku pod adresem [GitHub](https://github.com/RemoteSys/entry/blob/master/testScript.py).

