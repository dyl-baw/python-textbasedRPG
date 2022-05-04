from unittest import TestCase
from unittest.mock import patch
from game import make_board
from game import describe_current_location
import unittest


class TestDescribeCurrentLocation(TestCase):

    @patch('random.choice', return_value='You are in a Grass Field')
    def test_describe_current_location_grass_field(self, mock_output):
        board = make_board(2, 2)
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Health": 100, "Experience": 0, "Level": 1, "Attack": 10}
        expected = 'You are in a Grass Field'
        actual = describe_current_location(board, character)
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value='You are in a Plains')
    def test_describe_current_location_plains(self, mock_output):
        board = make_board(2, 2)
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Health": 100, "Experience": 0, "Level": 1, "Attack": 10}
        expected = 'You are in a Plains'
        actual = describe_current_location(board, character)
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value='You are in a Swamp')
    def test_describe_current_location_swamp(self, mock_output):
        board = make_board(2, 2)
        character = {"X-coordinate": 1, "Y-coordinate": 0, "Health": 100, "Experience": 0, "Level": 1, "Attack": 10}
        expected = 'You are in a Swamp'
        actual = describe_current_location(board, character)
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value='You are in a Forest')
    def test_describe_current_location_forest(self, mock_output):
        board = make_board(2, 2)
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Health": 100, "Experience": 0, "Level": 1, "Attack": 10}
        expected = 'You are in a Forest'
        actual = describe_current_location(board, character)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
