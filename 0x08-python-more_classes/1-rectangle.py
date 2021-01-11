#!/usr/bin/python3
"""define a rectangle"""

class Rectangle:
    """define a rectangle class"""

    def __init__(self, width=0, height=0):
        """define the height and width"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """define width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """define height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
