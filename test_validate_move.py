import unittest
from unittest import TestCase
from game import make_board
from game import validate_move


class TestValidateMove(TestCase):

    def test_validate_move_north(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        direction = "NORTH"
        expected = False
        actual = validate_move(make_board(2, 2), character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_west(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        direction = "WEST"
        expected = False
        actual = validate_move(make_board(2, 2), character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_east(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        direction = "EAST"
        expected = True
        actual = validate_move(make_board(2, 2), character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_south(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        direction = "SOUTH"
        expected = True
        actual = validate_move(make_board(2, 2), character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_east_from_one_coordinate(self):
        character = {"X-coordinate": 1, "Y-coordinate": 0}
        direction = "EAST"
        expected = False
        actual = validate_move(make_board(2, 2), character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_west_from_one_coordinate(self):
        character = {"X-coordinate": 1, "Y-coordinate": 0}
        direction = "WEST"
        expected = True
        actual = validate_move(make_board(2, 2), character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_north_from_one_coordinate(self):
        character = {"X-coordinate": 0, "Y-coordinate": 1}
        direction = "NORTH"
        expected = True
        actual = validate_move(make_board(2, 2), character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_south_from_one_coordinate(self):
        character = {"X-coordinate": 0, "Y-coordinate": 1}
        direction = "SOUTH"
        expected = False
        actual = validate_move(make_board(2, 2), character, direction)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
