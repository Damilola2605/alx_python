#!/usr/bin/python3

# Define a and b on separate lines
a = 1
b = 2

# Import the add function from add_0.py
from add_0 import add

# Perform the addition operation using the add function and print the result
print("{} + {} = {}".format(a, b, add(a, b)))