"""Test file for the Util module"""

# ========== Imports ========== #

import unittest

from src.util import EmptyQueue


# ========== Tests ========== #

class TestUtilClass (unittest.TestCase):
    """Test class for util"""

    def test_empty_queue (self):
        """Test that EmptyQueue is a valid Exception"""
        with self.assertRaises(EmptyQueue):
            raise EmptyQueue()
