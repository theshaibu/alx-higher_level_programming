#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either width or height is not an int.
            ValueError: If either width or height <= 0.
            TypeError: If either x or y is not an int.
            ValueError: If either x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Properties for width, height, x, and y with type and value checks
    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_dimension(value, "height")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__validate_coordinate(value, "x")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__validate_coordinate(value, "y")
        self.__y = value

    def __validate_dimension(self, value, dimension_name):
        """Validate the dimension (width/height) value."""
        if not isinstance(value, int):
            raise TypeError(f"{dimension_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{dimension_name} must be > 0")

    def __validate_coordinate(self, value, coordinate_name):
        """Validate the coordinate (x/y) value."""
        if not isinstance(value, int):
            raise TypeError(f"{coordinate_name} must be an integer")
        if value < 0:
            raise ValueError(f"{coordinate_name} must be >= 0")

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            self.__update_with_args(args)
        elif kwargs:
            self.__update_with_kwargs(kwargs)

    def __update_with_args(self, args):
        """Update the Rectangle attributes using *args."""
        attributes = ["id", "width", "height", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, attributes[i], value)

    def __update_with_kwargs(self, kwargs):
        """Update the Rectangle attributes using **kwargs."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

