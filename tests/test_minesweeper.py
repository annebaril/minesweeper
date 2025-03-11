import random

import pytest

from src import minesweeper


@pytest.fixture
def mocked_game():
    game = minesweeper.Minesweeper(3, 3, 0)
    game.mines = {(0, 0), (1, 1)}
    game.board = [["*", "", ""], ["", "*", ""], ["", "", ""]]
    return game


def test_module_exists():
    assert minesweeper


def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    assert len(game.mines) == 2


def test_reveal(mocked_game):
    game = mocked_game
    random_mine = random.choice(list(game.mines))
    assert game.reveal(random_mine[0], random_mine[1]) == "Game Over"
    assert game.reveal(0, 1) == "Continue"


def test_get_board(mocked_game):
    game = mocked_game
    assert game.get_board() == [["*", "", ""], ["", "*", ""], ["", "", ""]]
    game.reveal(0, 1)
    assert game.get_board() == [["*", "0", "0"], ["0", "*", "0"], ["", "", ""]]


def test_is_winner(mocked_game):
    game = mocked_game
    assert game.is_winner() == False
    game.reveal(0, 1)
    game.reveal(2, 1)
    assert game.is_winner() == True
