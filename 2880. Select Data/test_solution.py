import unittest
from solution import selectData
import pandas as pd


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        students = pd.DataFrame({
            'student_id': [101, 53, 128, 3],
            'name': ['Ulysses', 'William', 'Henry', 'Henry'],
            'age': [13, 10, 6, 11]
        })
        result = selectData(students)
        expected = pd.DataFrame({
            'name': ['Ulysses'],
            'age': [13]
        })
        self.assertEqual(result.equals(expected), True)
    