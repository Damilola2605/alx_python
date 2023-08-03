#!/usr/bin/python3
"""
Module on the BaseGeometry class.
"""

class TheMetaclass(type):
    """
    This class contain adefault parent obj.
    """
    def __dir__(subclass):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
class BaseGeometry():
    """
    An empty class file defining the base geometry.
    """
    def area(self):
        """
        calculate the area of the geometry

        Raises:
        Raise expection that is not implemented
        """
        raise Exception("area() is not implemented")