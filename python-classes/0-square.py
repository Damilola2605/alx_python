#!/usr/bin/python3

"""Module on Square

This module demonstrates documentation of Class Square module that has Private instance attribute as size.

Example:
    Create a square instance with a size of 3:
    my_square = Square(3)

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension
"""

class Square:
    def __init__(self, size):
        self.__size = size