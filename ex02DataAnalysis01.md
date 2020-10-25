# Task

Based on the material processed in class (see [firstNot.ipynb](https://github.com/RemoteSys/engineer/blob/master/notebooks/firstNot.ipynb), prepare your own jupyter notebook, which will allow you to quickly prepare the data - as described in the section ['Preparation of data'](#preparation-of-data)


*Explanation*:

>In the next class:

>  - current data will be downloaded
>  - the downloaded data will be cleaned using the notebook you write



# Simple data analysis exercises part 1.

 1. Data, [see](#data)
 2. Preparation of data, [see](#preparation-of-data)
 3. ... to be continued' ...



# Data

Download data from the addresses below:

  1. Data on the viruse covid pandemic - [WHO](https://covid19.who.int/table) (click the arrow in the upper right corner of the page to download the data)
  2. Population data of individual countries: [the United Nations](https://population.un.org/wpp/Download/Standard/Population/), `Total Population - Both Sexes (XLSX, 2.4 MB)` file





# Preparation of data

### 1. Conda environment

Prepare a virtual environment, with modules installed:

  - numpy
  - pandas
  - scipy
  - matplotlib
  - `xlrd` (Library for developers to extract data from Microsoft Excel (tm) spreadsheet files)
  - jinja2


### 2. Jupyter notebooks

Create a new jupyter notebook in which:

  - place a code that prepares data about the covid virus
  - place a code to prepare the population data of the world


In the next class, the notepad will be used for automatic data preparation - example:

  - download current data
  - enter the address of the new data file in the notebook
  - restart the notebook
  - the disk should contain a csv file with prepared data


### 3. Data preprocessing

Data preparation (see [firstNot.ipynb](https://github.com/RemoteSys/engineer/blob/master/notebooks/firstNot.ipynb)) includes:

  - selecting the required columns from the data table
  - shortening, unification of column names
  - to unify data in columns with the text of e.g. country names
  - setting the corresponding numerical data types (int, float)
  - matching country names in both tables (covid and population data)










