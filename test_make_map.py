from unittest import TestCase
from unittest.mock import patch
import io
from game import make_map
import unittest


class TestMakeMap(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_map_generate(self, mock_output):
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        make_map(character)
        actual = mock_output.getvalue()
        expected = "\n\n[@] [#] [#] \n[#] [#] [#] \n[#] [#] [#] \n{'X-coordinate': 0, 'Y-coordinate': 0}\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_map_generate_near_boss_room(self, mock_output):
        character = {"X-coordinate": 12, "Y-coordinate": 13}
        make_map(character)
        actual = mock_output.getvalue()
        expected = "[#] [#] [#] [#] [#] \n[#] [#] [#] [#] [#] \n[#] [#] [@] [#] [#] \n[#] [#] [#] !!! [#] \n[#] [#] [#] [#] [#] \n{'X-coordinate': 12, 'Y-coordinate': 13}\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_map_generate_on_boss_room(self, mock_output):
        character = {"X-coordinate": 13, "Y-coordinate": 14}
        make_map(character)
        actual = mock_output.getvalue()
        expected = "[#] [#] [#] [#] [#] \n[#] [#] [#] [#] [#] \n[#] [#] [@] [#] [#] \n[#] [#] [#] [#] [#] \n[#] [#] [#] [#] [#] \n{'X-coordinate': 13, 'Y-coordinate': 14}\n"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
