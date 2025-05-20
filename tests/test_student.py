"""Test file for the Util module"""

# ========== Imports ========== #

import unittest

from src.classes.student import Student, Tutor
from tests.test_util import DATA


# ========== Tests ========== #

class TestStudentClass (unittest.TestCase):
    """Test class for student"""

    def test_creation(self):
        """Test if the student is created correctly"""
        s = Student(DATA)
        self.assertIsInstance(s, Student)

    def test_str(self):
        """Test the student can be output correctly"""
        s = Student(DATA)
        self.assertTrue("STUDENT" in str(s))

    def test_odim (self):
        """Test if odin property output is correct"""
        s = Student(DATA)
        self.assertEqual("john_doe", s.odin)

class TestTutorClass (unittest.TestCase):
    """Test class for tutor"""

    def test_str(self):
        """Test the Tutor can be output correctly"""
        s = Tutor(DATA)
        self.assertTrue("TUTOR" in str(s))
