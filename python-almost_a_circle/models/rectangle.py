#!/usr/bin/python3
"""
Module on a Rectangle class that inherits from Base
"""
from models.base import Base

class Rectangle (Base):
    """
    This is the calss defining the Rectangle

    Attribute include:
    __width -> width
    __height -> height
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This function intializes a Instance of the Rectangle

        Args:
         width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
        id (int): The value for the id attribute.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # Implement any validation logic you need
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        # Implement validation logic you need
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        # Implement validation logic you need
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        # Implement validation logic you need
        self.__y = value
