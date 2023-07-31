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
        if not isinstance(size, int):
         raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        def area(self):

            '''Represents the value of area

            Returns:
              int: the calculated square of the area
            '''
            return self.__size ** 2
