# Python packages

### What is a package
- A package is a set of useful functions and classes that are useful for common tasks

### Why should we use them?
- Because they make writing code orders of magnitude easier and faster.
Instead of having to write the same code again and again, or putting energy and time into creating a codebase ex-novo, it's much more convenient to import packages that have already been tested and that have been improved to the point of reaching the best computational efficiency and speed possible.

##### Requests
- The package `requests` gives a splendid example of why we should use packages. One of the features that the creators of the package have implemented under the hood, is that it's possible to pass a `requests` object directly as a conditional:
```python
import requests

content = requests.get("a_URL")

if content:
	some_code
```
If the result of the `get()` function was a status code between 200 and 400 (normal functioning page), the object will be evaluated as `True`, and it will be evaluated as `False` otherwise.
This implementation is a significant help in coding terms, but it would never have been realistic to implement it if the code was written directly. 

### What is pip?
- `pip` is a package managed in Python, used to install any packages
- we use `pip install package_name` to install a package in Python2, `pip3 install package_name` in Python3