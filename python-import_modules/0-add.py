#!/usr/bin/python3
# Import the add function from add_0.py
from add_0 import add

# Define a and b on separate lines
a = 1
b = 2

result = add(a, b)
print("{} + {} = {}".format(a, b, add(a, b)))