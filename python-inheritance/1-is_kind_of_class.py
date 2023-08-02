#!/usr/bin/python3

"""Module on Inheritance

This module demonstrates a Function of inheritance.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of the specified class.
    Args:
    obj: to check if it inherited directly or indirectly.
    a_class: The class to compare the object against.

    Returns:
    bool: True if the object is an instance of the specified class.
    """
    return isinstance(obj, a_class)
