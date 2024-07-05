# Linked Boxes
from typing import Optional

words = ["Bicycle", "Elections", "Popularity", "Football", "Airplane"]


class Box:

    def __init__(self, word, letter_index, letter):
        self.word = word
        self.letter_index = letter_index
        self.letter = letter
        self.previous_box: Optional[Box, bool] = None


class BoxContainer:

    def __init__(self):
        self.container = []


class Reading:

    def __init__(self, c_words: list[str]):
        self.c_words = c_words
        self.box_container = BoxContainer()

    def add_step(self, word, letter_index, letter):
        current_box = Box(word, letter_index, letter)
        self.box_container.container.append(current_box)
