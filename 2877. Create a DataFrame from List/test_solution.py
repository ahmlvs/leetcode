import unittest
import pandas as pd
from solution import createDataframe

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        # Input data
        student_data = [
            [1, 15],
            [2, 11],
            [3, 11],
            [4, 20]
        ]
        
        # Expected DataFrame
        expected_df = pd.DataFrame(
            data=[
                [1, 15],
                [2, 11],
                [3, 11],
                [4, 20]
            ],
            columns=['student_id', 'age']
        )
        
        # Generate result
        result_df = createDataframe(student_data)
        
        # Test DataFrame equality
        pd.testing.assert_frame_equal(result_df, expected_df)
