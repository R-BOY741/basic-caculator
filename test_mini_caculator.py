from main import Add
import unittest

class TestAdd(unittest.TestCase):
    def test_Add(self):
        a_method = Add()
        self.assertEqual(2, a_method.add(1, 1), "Adding 1 to 1 should be 2")
