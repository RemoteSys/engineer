# Command line parser

1. Python `argparse`:
 - [doc](https://docs.python.org/3/library/argparse.html)
 - [tutorial](https://docs.python.org/3/howto/argparse.html#id1)

The `argparse` is recommended command-line parsing module in the Python standard library. 
This module handles the argument list provided by `sys.argv`.

2. Python `sys.argv` [doc](https://docs.python.org/3/library/sys.html#sys.argv)


# Test `sys.argv`
 > - create test script: `test.py`
 > - add 2 lines of code to the script:
```python
import sys
print(sys.argv)
```

 > - run the script several times with different arguments to see `sys.argv` in action e.g.:
```
python test.py 20 abc -o 677 --arg3 xxxx
```


# Short

1. Create an argument parser object:
 > - parser = argparse.ArgumentParser()

2. Specify the script arguments. Example:
 > - parser.add_argument("name", help='some help string') - positional argument
 > - parser.add_argument("-e", "--age", help='some help string') - optional argument

3. Script arguments handling:
 > - `sys.argv` returns a list of arguments, e.g.: `args_list = ['John','-e','25']`
 > - `argparse` parses the list: `args = parser.parse_args(args_list)`

4. In the script, write a function that parses the script arguments. Example:

```python
def my_parser():
    parser = argparse.ArgumentParser()

    # specify the script arguments

    return parser.parse_args()
```
  
