import unittest
from solution import selectFirstRows
import pandas as pd

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        employees = pd.DataFrame({
            'employee_id': [3, 90, 9, 60, 49, 43],
            'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
            'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
            'salary': [48675, 11096, 33805, 37678, 23793, 40454]
        })

        expected_df = pd.DataFrame({
            'employee_id': [3, 90, 9],
            'name': ['Bob', 'Alice', 'Tatiana'],
            'department': ['Operations', 'Sales', 'Engineering'],
            'salary': [48675, 11096, 33805]
        })
        
        result_df = selectFirstRows(employees)
        
        # Test DataFrame equality
        pd.testing.assert_frame_equal(result_df, expected_df)
