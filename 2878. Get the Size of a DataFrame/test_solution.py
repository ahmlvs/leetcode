import unittest
import pandas as pd
from solution import getDataframeSize

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        # Input data
        players = pd.DataFrame(
            data=[
                [846, 'Mason', 21, 'Forward', 'RealMadrid'],
                [749, 'Riley', 30, 'Winger', 'Barcelona'],
                [155, 'Bob', 28, 'Striker', 'ManchesterUnited'],
                [583, 'Isabella', 32, 'Goalkeeper', 'Liverpool'],
                [388, 'Zachary', 24, 'Midfielder', 'BayernMunich'],
                [883, 'Ava', 23, 'Defender', 'Chelsea'],
                [355, 'Violet', 18, 'Striker', 'Juventus'],
                [247, 'Thomas', 27, 'Striker', 'ParisSaint-Germain'],
                [761, 'Jack', 33, 'Midfielder', 'ManchesterCity'],
                [642, 'Charlie', 36, 'Center-back', 'Arsenal']
            ],
            columns=['player_id', 'name', 'age', 'position', 'team']
        )

        # Expected output
        expected_output = [10, 5]

        # Call the function
        output = getDataframeSize(players)

        # Assertion
        self.assertEqual(output, expected_output)
        