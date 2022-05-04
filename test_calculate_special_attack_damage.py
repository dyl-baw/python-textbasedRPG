from unittest import TestCase
import unittest
from unittest.mock import patch
from game import calculate_special_attack_damage
import io


class TestSpecialAttackDamage(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_special_attack_damage_shadow(self, mock_output):
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
        calculate_special_attack_damage(character, monster)
        actual = mock_output.getvalue()
        expected = "bob used Back Stab and hit goblin. You dealt 37.5 damage to goblin."
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_special_attack_damage_monk(self, mock_output):
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
        calculate_special_attack_damage(character, monster)
        actual = mock_output.getvalue()
        expected = "bob used One Punch and hit goblin. You dealt 30.0 damage to goblin."
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_special_attack_damage_paladin(self, mock_output):
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
        calculate_special_attack_damage(character, monster)
        actual = mock_output.getvalue()
        expected = "bob used Crusader Strike and hit goblin. You dealt 22.5 damage to goblin."
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_special_attack_damage_mage(self, mock_output):
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
        calculate_special_attack_damage(character, monster)
        actual = mock_output.getvalue()
        expected = "bob used Fireball and hit goblin. You dealt 67.5 damage to goblin."
        self.assertIn(expected, actual)


if __name__ == "__main__":
    unittest.main()
