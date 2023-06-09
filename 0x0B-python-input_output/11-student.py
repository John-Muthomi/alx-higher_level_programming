#!/usr/bin/python3
"""
The class Student module
"""


class Student:
    """class with methods to_json for retrieves dictionary"""

    def __init__(self, first_name, last_name, age):
        """method for initialized all atributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
