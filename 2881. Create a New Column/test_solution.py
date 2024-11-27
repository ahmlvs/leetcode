import unittest
from solution import createBonusColumn
import pandas as pd


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        employees = pd.DataFrame({
            'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
            'salary': [4548, 28150, 1103, 6593, 74576, 24433]
        })
        expected_output = pd.DataFrame({
            'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
            'salary': [4548, 28150, 1103, 6593, 74576, 24433],
            'bonus': [9096, 56300, 2206, 13186, 149152, 48866]
        })
        self.assertTrue(createBonusColumn(employees).equals(expected_output))
    