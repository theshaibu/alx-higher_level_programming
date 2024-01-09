#!/usr/bin/python3
"""Module: student_class
Defines a class Student that represents a student with attributes:
- First_name
- Last_name
- Age
"""

class Student:
    """Class that defines a student.

    Public attributes:
        - first_name
        - last_name
        - age

    Public method:
        - to_json(): Returns a dictionary representation of a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with given attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """Returns a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the attributes of the Student.
        """
        return self.__dict__

