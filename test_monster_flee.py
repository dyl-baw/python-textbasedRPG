from unittest import TestCase
import unittest
from unittest.mock import patch
from game import monster_flee


class TestMonsterFlee(TestCase):
    @patch('random.randint', return_value=1)
    def test_monster_flee_successful(self, _):
        monster = {"Name": "goblin",
                   "health": 20,
                   "attack": 5,
                   "experience": 10}
        expected = True
        actual = monster_flee(monster)
        self.assertTrue(expected, actual)


class TestMonsterFlee(TestCase):
    @patch('random.randint', return_value=3)
    def test_monster_flee_fail(self, _):
        monster = {"Name": "goblin",
                   "health": 20,
                   "attack": 5,
                   "experience": 10}
        expected = False
        actual = monster_flee(monster)
        self.assertFalse(expected, actual)


class TestMonsterFlee(TestCase):
    @patch('random.randint', return_value=1)
    def test_monster_flee_fail_boss(self, _):
        monster = {"Name": "Rimuru",
                   "health": 150,
                   "attack": 30}
        expected = False
        actual = monster_flee(monster)
        self.assertFalse(expected, actual)


if __name__ == "__main__":
    unittest.main()
