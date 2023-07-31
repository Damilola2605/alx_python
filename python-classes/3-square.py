#!/user/bin/python3

"""Module on Square

This module demonstrates a Class Square that has Private attribute as size.

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

    """
         Represents a square.
         Attributes:
        __size (int): The size of the square.
        """
    def __init__(self, size=0):

        ''' Initializes a Square instance.
             Args:
        size (int, optional): The size of the square. Set to 0
        '''
        self.__size = size

    #This is the property line
    def size(self):

        ''' Retrieves the size of the square.
        Returns:
            int: The size of the square.
        '''
        return self.__size
    
    #This is the line for the setter
    def size(self, value):

        '''Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.'''
        

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        ''' Calculates the area of the square.

        Returns:
            int: The area of the square.'''
        return self.__size ** 2
