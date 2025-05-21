"""Test file for the Util module"""

# ========== Imports ========== #

import unittest

from src.classes.student import Student
from src.classes.containers import Queue
from src.util import EmptyQueue
from tests.test_util import DATA


# ========== Tests ========== #

class TestQueueClass (unittest.TestCase):
    """Test class for Queue"""

    def test_create_queue (self):
        """Test queue creation"""
        q = Queue[Student]()
        self.assertIsInstance(q, Queue)

    def test_is_empty (self):
        """Test the is_empty() function"""
        q = Queue[Student]()
        self.assertTrue(q.is_empty())

    def test_enqueue (self):
        """Test that enqueue adds an element"""
        q = Queue[Student]()
        s = Student(*DATA)
        q.enqueue(s)
        self.assertFalse(q.is_empty())

    def test_dequeue (self):
        """Test dequeue removes an element"""
        q = Queue[Student]()
        s = Student(*DATA)
        q.enqueue(s)
        self.assertIsInstance(q.dequeue(), Student)
        self.assertTrue(q.is_empty())

        # Test that dequeue raises an exception if called while the queue is empty.
        with self.assertRaises(EmptyQueue):
            q.dequeue()
