from unittest import TestCase
import unittest
from game import level_up


class TestLevelUp(TestCase):
    def test_level_up_shadow_to_trickster(self):
        character = {'Attack': 25,
                     'Class': 'Shadow',
                     'Experience': 100,
                     'Health': 115,
                     'Level': 1,
                     'Special Attack': 'Back Stab',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        expected = {'Attack': 35,
                    'Class': 'Trickster',
                    'Experience': 0,
                    'Health': 140,
                    'Level': 2,
                    'Special Attack': 'Back Stab',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        actual = level_up(character)
        self.assertEqual(expected, actual)

    def test_level_up_trickster_to_assassin(self):
        character = {'Attack': 35,
                     'Class': 'Trickster',
                     'Experience': 100,
                     'Health': 140,
                     'Level': 2,
                     'Special Attack': 'Back Stab',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        expected = {'Attack': 45,
                    'Class': 'Assassin',
                    'Experience': 0,
                    'Health': 165,
                    'Level': 3,
                    'Special Attack': 'Back Stab',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        actual = level_up(character)
        self.assertEqual(expected, actual)

    def test_level_up_monk_to_templar(self):
        character = {'Attack': 25,
                     'Class': 'Monk',
                     'Experience': 100,
                     'Health': 125,
                     'Level': 1,
                     'Special Attack': 'One Punch',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        expected = {'Attack': 35,
                    'Class': 'Templar',
                    'Experience': 0,
                    'Health': 150,
                    'Level': 2,
                    'Special Attack': 'One Punch',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        actual = level_up(character)
        self.assertEqual(expected, actual)

    def test_level_up_templar_to_inquisitor(self):
        character = {'Attack': 35,
                     'Class': 'Templar',
                     'Experience': 100,
                     'Health': 150,
                     'Level': 2,
                     'Special Attack': 'One Punch',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        expected = {'Attack': 45,
                    'Class': 'Inquisitor',
                    'Experience': 0,
                    'Health': 175,
                    'Level': 3,
                    'Special Attack': 'One Punch',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        actual = level_up(character)
        self.assertEqual(expected, actual)

    def test_level_up_mage_to_elementalist(self):
        character = {'Attack': 45,
                     'Class': 'Mage',
                     'Experience': 100,
                     'Health': 100,
                     'Level': 1,
                     'Special Attack': 'Fireball',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        expected = {'Attack': 55,
                    'Class': 'Elementalist',
                    'Experience': 0,
                    'Health': 125,
                    'Level': 2,
                    'Special Attack': 'Fireball',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        actual = level_up(character)
        self.assertEqual(expected, actual)

    def test_level_up_elementalist_to_ascendant(self):
        character = {'Attack': 55,
                     'Class': 'Elementalist',
                     'Experience': 100,
                     'Health': 125,
                     'Level': 2,
                     'Special Attack': 'Fireball',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        expected = {'Attack': 65,
                    'Class': 'Ascendant',
                    'Experience': 0,
                    'Health': 150,
                    'Level': 3,
                    'Special Attack': 'Fireball',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        actual = level_up(character)
        self.assertEqual(expected, actual)

    def test_level_up_paladin_to_crusader(self):
        character = {'Attack': 15,
                     'Class': 'Paladin',
                     'Experience': 100,
                     'Health': 150,
                     'Level': 1,
                     'Special Attack': 'Crusader Strike',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        expected = {'Attack': 25,
                    'Class': 'Crusader',
                    'Experience': 0,
                    'Health': 175,
                    'Level': 2,
                    'Special Attack': 'Crusader Strike',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        actual = level_up(character)
        self.assertEqual(expected, actual)

    def test_level_up_crusader_to_whiteknight(self):
        character = {'Attack': 25,
                     'Class': 'Crusader',
                     'Experience': 100,
                     'Health': 175,
                     'Level': 2,
                     'Special Attack': 'Crusader Strike',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        expected = {'Attack': 35,
                    'Class': 'White Knight',
                    'Experience': 0,
                    'Health': 200,
                    'Level': 3,
                    'Special Attack': 'Crusader Strike',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        actual = level_up(character)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
