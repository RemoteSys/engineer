# Table of Contents

 1. [Task_1](#Task_1)
 2. [Project](#Project)
 3. [Additional_information](#Additional_information)


# Task_1

Write a script showing the current exchange rates downloaded from the website. Script functionality:

 - show help when run with the `-h` option
 - displays the rate of a single currency
 - displays the entire table of exchange rates
 - optionally creates an `html` report with the downloaded data


### Details

 - the user enters the name of the country or the currency code to download information about the current exchange rate
 - the user gives the name of the table to download the table of rates 
 - the user does not provide the name of the table and downloads the default table of rates 



# Project
### Directory structure

  - root directory: contains the script file
  - subdirectory e.g. `modules`: contains module files
     - module with functions
     - module that provides data on currency codes
  - `templates` subdirectory: contains report templates


### Bank service
Banking service that provides data: [NBP](http://api.nbp.pl/)


### Modules

 - sys : [www](https://docs.python.org/3.9/library/sys.html)
 - argparse: [www](https://docs.python.org/3.9/library/argparse.html)
 - requests: [www](https://requests.readthedocs.io/en/latest/)
 - json: [www](https://docs.python.org/3.9/library/json.html)
 - jinja2: [www](https://jinja.palletsprojects.com/en/2.10.x/)



# Additional_information

### Script template

For basic information on creating scripts, see the document on the [GitHub](https://github.com/RemoteSys/entry/blob/master/e06_about_scripts.md).

An example of a simple script is available in the file at [GitHub](https://github.com/RemoteSys/entry/blob/master/e07_script_example.py). 




### JSON

>,,JavaScript Object Notation (JSON, pronounced /ˈdʒeɪsən/; also /ˈdʒeɪˌsɒn/[note 1]) is an open standard file format, and data interchange format, that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and array data types (or any other serializable value). It is a very common data format, with a diverse range of applications, such as serving as a replacement for XML in AJAX systems.''

(from *https://en.wikipedia.org/wiki/JSON*)


### CSV
>,,A comma-separated values (CSV) file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format. A CSV file typically stores tabular data (numbers and text) in plain text, in which case each line will have the same number of fields.''

(from *https://en.wikipedia.org/wiki/Comma-separated_values*)





