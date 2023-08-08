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
