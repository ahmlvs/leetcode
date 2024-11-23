import unittest
from solution import RandomizedSet


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        randomizedSet = RandomizedSet()

        # Test insert
        self.assertTrue(randomizedSet.insert(1))  # 1 is inserted
        self.assertFalse(randomizedSet.insert(1))  # 1 already exists
        self.assertTrue(randomizedSet.insert(2))  # 2 is inserted

        # Test getRandom
        self.assertIn(randomizedSet.getRandom(), [1, 2])  # Should return 1 or 2

        # Test remove
        self.assertTrue(randomizedSet.remove(1))  # 1 is removed
        self.assertFalse(randomizedSet.remove(1))  # 1 does not exist anymore
        self.assertTrue(randomizedSet.insert(3))  # 3 is inserted

        # Test getRandom after modifications
        random_value = randomizedSet.getRandom()
        self.assertIn(random_value, [2, 3])  # Should return 2 or 3
