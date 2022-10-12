# Spis

 1. [Zadanie_1](#Zadanie_1)
 2. [Projekt](#Projekt)
 3. [Dodatkowe_informacje](#Dodatkowe_informacje)


# Zadanie_1

Napisać skrypt podający bieżące kursy walut pobrane z serwisu internetowego. Funkcjonalność skryptu:

  - wyświetla pomoc po uruchomieniu z opcją `-h`
  - wyświetla kurs pojedynczej waluty
  - wyświetla całą tabelę kursów walut
  - opcjonalnie tworzy raport `html` z pobranymi danymi

### Szczegóły
 - użytkownik podaje nazwę kraju lub kod waluty aby pobrać informację o aktualnym kursie
 - użytkownik podaje nazwę tabeli aby pobrać tabelę kursów
 - użytkownik nie podaje nazwy tabeli i pobiera domyślnie ustawioną tabelę kursów



# Projekt
### Struktura katalogów

 - katalog główny: zawiera plik skryptu
 - podkatalog np. `moduły`: zawiera pliki modułów
    - moduł z funkcjami
    - moduł udostępniający dane o kodach walut
 - podkatalog `templates`: zawiera szablony raportów


### Serwis bankowy
Serwis bankowy udostępniający dane: [NBP](http://api.nbp.pl/)


### Potrzebne moduły

 - sys : [www](https://docs.python.org/3.9/library/sys.html)
 - argparse: [www](https://docs.python.org/3.9/library/argparse.html)
 - requests: [www](https://docs.python-requests.org/en/master/index.html)
 - json: [www](https://docs.python.org/3.9/library/json.html)
 - jinja2: [www](https://jinja2docs.readthedocs.io/en/stable/)



# Dodatkowe_informacje

### Szablon skryptu

Podstawowe informacje o tworzeniu skryptów zawiera dokument znajdujący się w serwisie [GitHub](https://github.com/RemoteSys/entry/blob/master/scriptsInfo.md).

Przykład prostego skryptu znajduje się w pliku pod adresem [GitHub](https://github.com/RemoteSys/entry/blob/master/testScript.py).


### JSON

>,,JavaScript Object Notation (JSON, pronounced /ˈdʒeɪsən/; also /ˈdʒeɪˌsɒn/[note 1]) is an open standard file format, and data interchange format, that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and array data types (or any other serializable value). It is a very common data format, with a diverse range of applications, such as serving as a replacement for XML in AJAX systems.''

(from *https://en.wikipedia.org/wiki/JSON*)


### CSV
>,,A comma-separated values (CSV) file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format. A CSV file typically stores tabular data (numbers and text) in plain text, in which case each line will have the same number of fields.''

(from *https://en.wikipedia.org/wiki/Comma-separated_values*)





