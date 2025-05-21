"""Test file for the Util module"""

# ========== Imports ========== #

import unittest

from src.util import EmptyQueue


# ========== Constants ========== #

DATA: tuple[str, str, int, float, str] = ('John', 'Doe', 99, 4.00, 'john_doe@example.com')


# ========== Tests ========== #

class TestUtilClass (unittest.TestCase):
    """Test class for util"""

    def test_empty_queue (self):
        """Test that EmptyQueue is a valid Exception"""
        with self.assertRaises(EmptyQueue):
            raise EmptyQueue()
