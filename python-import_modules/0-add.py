#!/usr/bin/python3
from add_0 import add

# Define a and b on separate lines
a = 1
b = 2

result = add(a, b)

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))