# Tests for minesweeper.py
import pytest as pt

from minesweeper import Minesweeper, MinesweeperAI

# Numbers arbitrary
HEIGHT = 12
WIDTH = 12
MINES = 8
expectedWinPercent = 85
