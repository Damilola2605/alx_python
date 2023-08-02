#!/usr/bin/python3

"""Module on Inheritance

This module demonstrates a Function of inheritance.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of the specified class.
    Args:
    obj: The object to be checked.
    a_class: The class to compare the object against.

    Returns:
        bool: True if the object is an instance of the specified class, False otherwise.
    """
    return type(obj) is a_class
