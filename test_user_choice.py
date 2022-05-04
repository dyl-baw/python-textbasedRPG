import unittest
import io
from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice


class TestGetUserChoice(TestCase):

    @patch('builtins.input', side_effect=["1"])
    def test_get_user_choice_north(self, _):
        self.assertEqual("NORTH", get_user_choice())

    @patch('builtins.input', side_effect=["2"])
    def test_get_user_choice_south(self, _):
        self.assertEqual("SOUTH", get_user_choice())

    @patch('builtins.input', side_effect=["3"])
    def test_get_user_choice_west(self, _):
        self.assertEqual("WEST", get_user_choice())

    @patch('builtins.input', side_effect=["4"])
    def test_get_user_choice_east(self, _):
        self.assertEqual("EAST", get_user_choice())

    @patch('builtins.input', side_effect=["5", "2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_input(self, mock_output, mock_input):
        get_user_choice()
        actual = mock_output.getvalue()
        expected = "You have selected an invalid direction, select again."
        self.assertIn(expected, actual)


if __name__ == "__main__":
    unittest.main()
