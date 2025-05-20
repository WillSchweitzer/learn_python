"""Test file for the Util module"""

# ========== Imports ========== #

import unittest

from src.classes.student import Student, Tutor


# ========== Imports ========== #

class TestStudentClass (unittest.TestCase):
    """Test class for student"""

    def test_creation(self):
        """Test if the student is created correctly"""
        data: dict[str, str | int | float] = {
            'first' : 'John',
            'last' : 'Doe',
            'age' : 99,
            'gpa' : 4.00,
            'email' : 'john_doe@example.com'
        }

        s = Student(data)
        self.assertIsInstance(s, Student)

    def test_str(self):
        """Test the student can be output correctly"""
        data: dict[str, str | int | float] = {
            'first' : 'John',
            'last' : 'Doe',
            'age' : 99,
            'gpa' : 4.00,
            'email' : 'john_doe@example.com'
        }

        s = Student(data)
        self.assertTrue("STUDENT" in str(s))

class TestTutorClass (unittest.TestCase):
    """Test class for tutor"""

    def test_creation(self):
        """Test if the Tutor is created correctly"""
        data: dict[str, str | int | float] = {
            'first' : 'John',
            'last' : 'Doe',
            'age' : 99,
            'gpa' : 4.00,
            'email' : 'john_doe@example.com'
        }

        s = Tutor(data)
        self.assertIsInstance(s, Tutor)

    def test_str(self):
        """Test the Tutor can be output correctly"""
        data: dict[str, str | int | float] = {
            'first' : 'John',
            'last' : 'Doe',
            'age' : 99,
            'gpa' : 4.00,
            'email' : 'john_doe@example.com'
        }

        s = Tutor(data)
        self.assertTrue("TUTOR" in str(s))
