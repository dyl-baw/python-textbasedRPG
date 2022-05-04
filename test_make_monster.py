from unittest import TestCase
import unittest
from unittest.mock import patch
from game import make_monster


class TestMakeMonster(TestCase):

    @patch('random.randint', return_value=0)
    def test_make_monster_goblin(self, _):
        expected = make_monster()
        actual = {"Name": "goblin",
                  "health": 20,
                  "attack": 5,
                  "experience": 10}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=1)
    def test_make_monster_giant(self, _):
        expected = make_monster()
        actual = {"Name": "giant",
                  "health": 40,
                  "attack": 10,
                  "experience": 10}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_make_monster_rat(self, _):
        expected = make_monster()
        actual = {"Name": "rat",
                  "health": 20,
                  "attack": 5,
                  "experience": 10}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)
    def test_make_monster_wolf(self, _):
        expected = make_monster()
        actual = {"Name": "wolf",
                  "health": 20,
                  "attack": 5,
                  "experience": 10}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=4)
    def test_make_monster_slime(self, _):
        expected = make_monster()
        actual = {"Name": "slime",
                  "health": 20,
                  "attack": 5,
                  "experience": 10}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=5)
    def test_make_monster_bandit(self, _):
        expected = make_monster()
        actual = {"Name": "bandit",
                  "health": 35,
                  "attack": 15,
                  "experience": 10}
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
