#!/usr/bin/python3
"""Define a class called Square"""


class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
