from collections import Counter

import pytest

from words_with_friends import BadPlayError, Board, board_size, create_empty_2d_board


@pytest.fixture
def board():
    return Board("../dictionary.txt")


def test_basic_first_play_on_dw_down(board):
    assert board.play_word("hello", Counter("HELLOX"), (7, 7), "down") == 18
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "H", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "E", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "L", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "L", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "O", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles


def test_basic_first_play_on_dw_down_all_tiles_used(board):
    assert board.play_word("hello", Counter("HELLO"), (7, 7), "down") == 53
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "H", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "E", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "L", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "L", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "O", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles


def test_basic_first_play_on_dw_right(board):
    assert board.play_word("hello", Counter("HELLOX"), (7, 7), "right") == 18
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "H", "E", "L", "L", "O", None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles


def test_basic_first_play_on_dw_right_all_tiles_used(board):
    assert board.play_word("hello", Counter("HELLO"), (7, 7), "right") == 53
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "H", "E", "L", "L", "O", None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles


def test_basic_first_play_down(board):
    assert board.play_word("CAT", Counter("CATS"), (7, 7), "down") == 6
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "A", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "T", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles


def test_basic_first_play_right(board):
    assert board.play_word("CAT", Counter("CATS"), (7, 7), "right") == 6
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", "A", "T", None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles


def test_wildcard_usage_1(board):
    assert board.play_word("CAT", Counter("C?TS"), (7, 7), "right") == 5
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", "A", "T", None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles
    assert board.play_word("ADD", Counter("??"), (7, 8), "down") == 36
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", "A", "T", None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, "D", None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, "D", None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles


def test_game_1(board):
    assert board.play_word("CAT", Counter("CATS"), (7, 7), "right") == 6
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", "A", "T", None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles
    assert board.play_word("ALES", Counter("ALESX"), (5, 10), "down") == 15
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, "A", None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, "L", None, None, None, None],
                 [None, None, None, None, None, None, None, "C", "A", "T", "E", None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, "S", None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles


def test_game_2(board):
    assert board.play_word("CAT", Counter("CATS"), (7, 7), "down") == 6
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "A", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "T", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles
    assert board.play_word("ALES", Counter("ALESX"), (10, 5), "right") == 15
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "A", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "T", None, None, None, None, None, None, None],
                 [None, None, None, None, None, "A", "L", "E", "S", None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles
    assert board.play_word("BACCATED", Counter("BACDX"), (4, 7), "down") == 36
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "B", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "A", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "A", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "T", None, None, None, None, None, None, None],
                 [None, None, None, None, None, "A", "L", "E", "S", None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "D", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles
    with pytest.raises(BadPlayError, match="Secondary word not in dict"):
        board.play_word("FATS", Counter("FETAS"), (9, 5), "right")
    assert board.tiles == new_tiles
    assert board.play_word("FET", Counter("FE"), (9, 5), "right") == 65
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "B", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "A", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "A", None, None, None, None, None, None, None],
                 [None, None, None, None, None, "F", "E", "T", None, None, None, None, None, None, None],
                 [None, None, None, None, None, "A", "L", "E", "S", None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "D", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles


def test_board_unchanged_after_bad_play_down(board):
    board.play_word("CAT", Counter("CATS"), (7, 7), "right")
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", "A", "T", None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles
    with pytest.raises(BadPlayError, match="Secondary word not in dict"):
        board.play_word("SELL", Counter("SELLX"), (5, 10), "down")
    assert board.tiles == new_tiles


def test_board_unchanged_after_bad_play_right(board):
    assert board.play_word("CAT", Counter("CATS"), (7, 7), "down") == 6
    new_tiles = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "C", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "A", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, "T", None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
    assert board.tiles == new_tiles
    with pytest.raises(BadPlayError, match="Secondary word not in dict"):
        board.play_word("SELL", Counter("SELLX"), (10, 5), "right")
    assert board.tiles == new_tiles


def test_debug_mode(board):
    c = Counter("CATS")
    board.play_word("CAT", c, (7, 7), "down", debug=True)
    assert board.tiles == create_empty_2d_board(board_size, None)
    assert c + Counter() == Counter("CATS")

    c = Counter("ALESS")
    board.play_word("ALES", c, (7, 7), "right", debug=True)
    assert board.tiles == create_empty_2d_board(board_size, None)
    assert c == Counter("ALESS")

    c = Counter("FET")
    board.play_word("FET", c, (7, 7), "right", debug=True)
    assert board.tiles == create_empty_2d_board(board_size, None)
    assert c == Counter("FET")

    c = Counter("BA??????X")
    board.play_word("BACCATED", c, (7, 7), "down", debug=True)
    assert board.tiles == create_empty_2d_board(board_size, None)
    assert c == Counter("BA??????X")


def test_not_using_letters_in_rack(board):
    with pytest.raises(BadPlayError, match="Needed letter not in rack"):
        board.play_word("HELLO", Counter(""), (7, 7), "down")
    c = Counter("HLLO")
    with pytest.raises(BadPlayError, match="Needed letter not in rack"):
        board.play_word("HELLO", c, (7, 7), "down")
    assert c == Counter("HLLO")


def test_using_letters_in_rack(board):
    c = Counter("CATS")
    board.play_word("CAT", c, (7, 7), "down")
    assert c + Counter() == Counter("S")

    c = Counter("ALESS")
    board.play_word("ALES", c, (10, 5), "right")
    assert c + Counter() == Counter("S")

    c = Counter("FE")
    board.play_word("FET", c, (9, 5), "right")
    assert c + Counter() == Counter()

    c = Counter("BA??X")
    board.play_word("BACCATED", c, (4, 7), "down")
    assert c + Counter() == Counter("X")


def test_location_out_of_bounds(board):
    with pytest.raises(BadPlayError, match="Location out of bounds"):
        board.play_word("CAT", Counter("CATS"), (-1, 1), "down")
    with pytest.raises(BadPlayError, match="Location out of bounds"):
        board.play_word("CAT", Counter("CATS"), (-1, 0), "right")
    with pytest.raises(BadPlayError, match="Location out of bounds"):
        board.play_word("CAT", Counter("CATS"), (7, -1), "down")
    with pytest.raises(BadPlayError, match="Location out of bounds"):
        board.play_word("CAT", Counter("CATS"), (7, -1), "right")
    with pytest.raises(BadPlayError, match="Location out of bounds"):
        board.play_word("CAT", Counter("CATS"), (board_size, 0), "down")
    with pytest.raises(BadPlayError, match="Location out of bounds"):
        board.play_word("CAT", Counter("CATS"), (0, board_size), "right")


def test_invalid_location_based_on_tiles(board):
    board.play_word("hello", Counter("HELLOX"), (7, 7), "down")
    with pytest.raises(BadPlayError, match="Location given cannot be the start of the word"):
        board.play_word("HELLOS", Counter("HELLOS"), (8, 7), "down")
    with pytest.raises(BadPlayError, match="Location given cannot be the start of the word"):
        board.play_word("HELLOS", Counter("HELLOS"), (11, 7), "down")
    board.play_word("HELLOS", Counter("HELLOS"), (7, 7), "down")
    board.play_word("OPEN", Counter("OPEN"), (11, 7), "right")
    with pytest.raises(BadPlayError, match="Location given cannot be the start of the word"):
        board.play_word("OPENS", Counter("OPENS"), (11, 8), "right")


def test_word_not_in_dict(board):
    with pytest.raises(BadPlayError, match="Passed word not in dictionary"):
        board.play_word("ALKJSHDLIJGASLJDBLAKJSHD", Counter("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), (7, 7), "down")
    with pytest.raises(BadPlayError, match="Passed word not in dictionary"):
        board.play_word("2", Counter("2"), (7, 7), "down")
    with pytest.raises(BadPlayError, match="Passed word not in dictionary"):
        board.play_word("3RD", Counter("3RD"), (7, 7), "down")
    with pytest.raises(BadPlayError, match="Passed word not in dictionary"):
        board.play_word("?ELLO", Counter("HELLO?"), (7, 7), "down")


def test_bad_direction(board):
    with pytest.raises(BadPlayError, match="Bad direction"):
        board.play_word("HELLO", Counter("HELLO"), (7, 7), "dwon")
