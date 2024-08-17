# Tests for minesweeper.py
import pytest as pt

from minesweeper import Minesweeper, MinesweeperAI

# Numbers arbitrary
HEIGHT = 12
WIDTH = 12
MINES = 8
expectedWinPercent = 85

# Win rate necessary 90 percent / `pytest -s`


@pt.mark.parametrize("execution_number", range(10))
def test(execution_number):
    return play1000()


# Complimentary function

def play1000():
    totalWon = 0
    for _ in range(10):  # 1000
        totalWon += play()

    print(f"\nWin rate:{totalWon // 10}%")

    assert totalWon >= expectedWinPercent * 10


def play():
    game = Minesweeper(height=HEIGHT, width=WIDTH, mines=MINES)
    ai = MinesweeperAI(height=HEIGHT, width=WIDTH)

    won = lost = False
    while not (won or lost):
        # AI choose a move
        move = ai.make_safe_move() or ai.make_random_move()
        if move is None:
            won = True
            break

        # Move and update AI
        if game.is_mine(move):
            lost = True
        else:
            nearby = game.nearby_mines(move)
            ai.add_knowledge(move, nearby)

    return won
