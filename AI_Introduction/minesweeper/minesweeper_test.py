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
    for _ in range(1000):
        totalWon += play()

    print(f"\nWin rate:{totalWon // 10}%")

    assert totalWon >= expectedWinPercent * 10
