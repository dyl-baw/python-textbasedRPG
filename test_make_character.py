import unittest
from unittest import TestCase
from unittest.mock import patch
from game import make_character


class TestMakeCharacter(TestCase):

    @patch('builtins.input', side_effect=["bob", "1"])
    def test_make_character_shadow(self, _):
        actual = {'Attack': 25,
                  'Class': 'Shadow',
                  'Experience': 0,
                  'Health': 115,
                  'Level': 1,
                  'Name': 'bob',
                  'Special Attack': 'Back Stab',
                  'X-coordinate': 0,
                  'Y-coordinate': 0}
        expected = make_character()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["bob", "2"])
    def test_make_character_monk(self, _):
        actual = {'Attack': 20,
                  'Class': 'Monk',
                  'Experience': 0,
                  'Health': 125,
                  'Level': 1,
                  'Name': 'bob',
                  'Special Attack': 'One Punch',
                  'X-coordinate': 0,
                  'Y-coordinate': 0}
        expected = make_character()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["bob", "3"])
    def test_make_character_paladin(self, _):
        actual = {'Attack': 15,
                  'Class': 'Paladin',
                  'Experience': 0,
                  'Health': 150,
                  'Level': 1,
                  'Name': 'bob',
                  'Special Attack': 'Crusader Strike',
                  'X-coordinate': 0,
                  'Y-coordinate': 0}
        expected = make_character()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["bob", "4"])
    def test_make_character_mage(self, _):
        actual = {'Attack': 45,
                  'Class': 'Mage',
                  'Experience': 0,
                  'Health': 100,
                  'Level': 1,
                  'Name': 'bob',
                  'Special Attack': 'Fireball',
                  'X-coordinate': 0,
                  'Y-coordinate': 0}
        expected = make_character()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
