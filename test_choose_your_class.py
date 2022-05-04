from unittest import TestCase
from game import choose_your_class
from unittest.mock import patch
import unittest


class TestChooseYourClass(TestCase):

    @patch('builtins.input', side_effect=["1"])
    def test_choose_your_class_shadow(self, _):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Health": 100, "Experience": 0, "Level": 1, "Attack": 10}
        expected = {'Attack': 25,
                    'Class': 'Shadow',
                    'Experience': 0,
                    'Health': 115,
                    'Level': 1,
                    'Special Attack': 'Back Stab',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        actual = choose_your_class(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_choose_your_class_monk(self, _):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Health": 100, "Experience": 0, "Level": 1, "Attack": 10}
        expected = {'Attack': 25,
                    'Class': 'Monk',
                    'Experience': 0,
                    'Health': 125,
                    'Level': 1,
                    'Special Attack': 'One Punch',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        actual = choose_your_class(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3"])
    def test_choose_your_class_paladin(self, _):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Health": 100, "Experience": 0, "Level": 1, "Attack": 10}
        expected = {'Attack': 15,
                    'Class': 'Paladin',
                    'Experience': 0,
                    'Health': 150,
                    'Level': 1,
                    'Special Attack': 'Crusader Strike',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        actual = choose_your_class(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    def test_choose_your_class_mage(self, _):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Health": 100, "Experience": 0, "Level": 1, "Attack": 10}
        expected = {'Attack': 45,
                    'Class': 'Mage',
                    'Experience': 0,
                    'Health': 100,
                    'Level': 1,
                    'Special Attack': 'Fireball',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        actual = choose_your_class(character)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
