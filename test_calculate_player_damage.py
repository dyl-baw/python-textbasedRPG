from unittest import TestCase
import unittest
from unittest.mock import patch
from game import calculate_player_damage
import io


class TestPlayerDamage(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_player_damage_shadow(self, mock_output):
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
        calculate_player_damage(character, monster)
        actual = mock_output.getvalue()
        expected = "bob hit goblin. You dealt 25 damage to goblin."
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_player_damage_monk(self, mock_output):
        monster = {"Name": "goblin",
                   "health": 20,
                   "attack": 5,
                   "experience": 10}
        character = {'Attack': 20,
                     'Class': 'Monk',
                     'Experience': 0,
                     'Health': 125,
                     'Level': 1,
                     'Name': 'bob',
                     'Special Attack': 'One Punch',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        calculate_player_damage(character, monster)
        actual = mock_output.getvalue()
        expected = "bob hit goblin. You dealt 20 damage to goblin."
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_player_damage_paladin(self, mock_output):
        monster = {"Name": "goblin",
                   "health": 20,
                   "attack": 5,
                   "experience": 10}
        character = {'Attack': 15,
                     'Class': 'Paladin',
                     'Experience': 0,
                     'Health': 150,
                     'Level': 1,
                     'Name': 'bob',
                     'Special Attack': 'Crusader Strike',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        calculate_player_damage(character, monster)
        actual = mock_output.getvalue()
        expected = "bob hit goblin. You dealt 15 damage to goblin."
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_player_damage_monk(self, mock_output):
        monster = {"Name": "goblin",
                   "health": 20,
                   "attack": 5,
                   "experience": 10}
        character = {'Attack': 45,
                     'Class': 'Mage',
                     'Experience': 0,
                     'Health': 100,
                     'Level': 1,
                     'Name': 'bob',
                     'Special Attack': 'Fireball',
                     'X-coordinate': 0,
                     'Y-coordinate': 0}
        calculate_player_damage(character, monster)
        actual = mock_output.getvalue()
        expected = "bob hit goblin. You dealt 45 damage to goblin."
        self.assertIn(expected, actual)




if __name__ == "__main__":
    unittest.main()
