#!/usr/bin/python3

"""Module on Inheritance

This module demonstrates a Function of inheritance.
"""
def inherits_from(obj, a_class):
    """
    Check if an object is an instance of the specified class.
    
    Args:
        obj: to check if it inherited directly or indirectly.
        a_class: The class to compare the object against.

    Returns:
        bool: True if the object is an instance of the specified class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
