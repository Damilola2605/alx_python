#!/usr/bin/python3
from add_0 import add

a = 1
b = 2

"""My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """

result = add(a, b)

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, result))
