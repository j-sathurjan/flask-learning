"""
This module is to make calculation related to geometry
"""
import math

def area_of_rectangle(length, breadth):
    """_this is area calculation function of a rectangular

    Args:
        length (_type_): _length of the rectangular_
        breadth (_type_): _breadth of the rectangular_
    """
    return length * breadth

def area_of_circle(radius):
    """_this function output the area of circle based on the given radius_

    Args:
        radius (_type_): _radius of the circle_
    """
    return math.pi * radius * radius
