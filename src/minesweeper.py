"""This module implements the Minesweeper game."""

# minesweeper.py
import random


class Minesweeper:
    def __init__(self, rows: int, cols: int, num_mines: int):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [["" for _ in range(cols)] for _ in range(rows)]
        self.mines = set()
        self.revealed = set()
        self.place_mines()

    def place_mines(self):
        """Randomly place mines on the board, updating adjacent cells with mine counts."""
        while len(self.mines) < self.num_mines:
            i = random.randint(0, self.rows - 1)
            j = random.randint(0, self.cols - 1)
            self.mines.add((i, j))
            self.board[i][j] = "*"
            for i_ in range(-1, 2):
                for j_ in range(-1, 2):
                    if 0 <= i + i_ < self.rows and 0 <= j + j_ < self.cols:
                        if self.board[i + i_][j + j_] != "*":
                            if self.board[i + i_][j + j_] == "":
                                self.board[i + i_][j + j_] = "1"
                            else:
                                self.board[i + i_][j + j_] = str(
                                    int(self.board[i + i_][j + j_]) + 1
                                )

    def reveal(self, row: int, col: int) -> str:
        """Reveal a cell on the board.
        Any adjacent cells with no mines are also revealed.
        Returns "Game Over" if a mine is revealed, "Continue" otherwise.
        """
        if (row, col) in self.mines:
            return "Game Over"
        self.revealed.add((row, col))
        self.board[row][col] = "0"

        # adjacent cells with no mines are also revealed
        for i_ in range(-1, 2):
            for j_ in range(-1, 2):
                if 0 <= row + i_ < self.rows and 0 <= col + j_ < self.cols:
                    if self.board[row + i_][col + j_] != "*":
                        self.revealed.add((row + i_, col + j_))
                        self.board[row + i_][col + j_] = "0"

        return "Continue"

    def get_board(self) -> list:
        """Return the current state of the board."""
        return self.board

    def is_winner(self) -> bool:
        """Check if the game has been won."""
        for ligne in self.board:
            for element in ligne:
                if element == "":
                    return False
        return True

    def restart(self) -> None:
        """Restart the game with the same parameters."""
        self.__init__(self.rows, self.cols, self.num_mines)


if __name__ == "__main__":
    game = Minesweeper(3, 3, 0)
    game.is_winner()
