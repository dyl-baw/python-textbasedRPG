import unittest
from unittest import TestCase
from unittest.mock import patch
from game import make_board


class TestMakeBoard(TestCase):

    @patch('random.choice', return_value='You are in a Grass Field')
    def test_make_board_add_descriptions_to_coordinates(self, _):
        actual = make_board(2, 2)
        expected = {(0, 0): 'You are in a Grass Field',
                    (0, 1): 'You are in a Grass Field',
                    (1, 0): 'You are in a Grass Field',
                    (1, 1): 'You are in a Grass Field',
                    (13, 14): 'Boss Room'}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value='You are in a Mountains')
    def test_make_board_add_different_descriptions_to_coordinates(self, _):
        actual = make_board(2, 2)
        expected = {(0, 0): 'You are in a Mountains',
                    (0, 1): 'You are in a Mountains',
                    (1, 0): 'You are in a Mountains',
                    (1, 1): 'You are in a Mountains',
                    (13, 14): 'Boss Room'}
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
