from unittest import TestCase
import unittest
from unittest.mock import patch
from game import calculate_monster_damage
import io


class TestCalculateMonsterDamage(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_monster_damage_deals_damage(self, mock_output):
        monster = {"Name": "goblin",
                   "health": 20,
                   "attack": 5,
                   "experience": 10}
        character = {'Attack': 25,
                     'Class': 'Shadow',
                     'Experience': 0,
                     'Health': 115,
                     'Level': 1,
                     'Name': 'bob',
                     'Special Attack': 'Back Stab',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        calculate_monster_damage(character, monster)
        actual = mock_output.getvalue()
        expected = "goblin hit bob. goblin dealt 5 damage to bob."
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_monster_damage_different_stats(self, mock_output):
        monster = {"Name": "goblin",
                   "health": 20,
                   "attack": 10,
                   "experience": 10}
        character = {'Attack': 25,
                     'Class': 'Shadow',
                     'Experience': 0,
                     'Health': 115,
                     'Level': 1,
                     'Name': 'bob',
                     'Special Attack': 'Back Stab',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        calculate_monster_damage(character, monster)
        actual = mock_output.getvalue()
        expected = "goblin hit bob. goblin dealt 10 damage to bob."
        self.assertIn(expected, actual)


if __name__ == "__main__":
    unittest.main()
