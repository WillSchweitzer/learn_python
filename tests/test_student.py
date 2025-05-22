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
        s = Student(*DATA)
        self.assertIsInstance(s, Student)

    def test_str(self):
        """Test the student can be output correctly"""
        s = Student(*DATA)
        self.assertTrue("STUDENT" in str(s))

    def test_odim (self):
        """Test if odin property output is correct"""
        s = Student(*DATA)
        self.assertEqual("john_doe", s.odin)

    def test_equals (self):
        """Test __eq__ """
        s1 = Student(*DATA)
        s2 = Student(*DATA)
        s3 = Student("Wrong", "Wrong", 0, 1.0, "Wrong")
        s4 = Tutor(*DATA)
        self.assertEqual(s1, s2)
        self.assertNotEqual(s1, s3)
        self.assertNotEqual(s1, s4)


class TestTutorClass (unittest.TestCase):
    """Test class for tutor"""

    def test_str(self):
        """Test the Tutor can be output correctly"""
        s = Tutor(*DATA)
        self.assertTrue("TUTOR" in str(s))
