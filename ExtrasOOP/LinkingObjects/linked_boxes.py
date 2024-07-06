# Linked Boxes
from typing import Optional

words = ["Bicycle", "Elections", "Popularity", "Football", "Airplane"]


class Box:

    def __init__(self, word, letter_index, letter, previous_box):
        self.word = word
        self.letter_index = letter_index
        self.letter = letter
        self.previous_box: Optional[Box, bool] = previous_box


class BoxContainer:

    def __init__(self):
        self.container = []


class Reading:

    def __init__(self, c_words: list[str]):
        self.c_words = c_words
        self.box_container = BoxContainer()
        self.previous_box = None

    def add_step(self, word, letter_index, letter):
        current_box = Box(word, letter_index, letter, self.previous_box)
        self.box_container.container.append(current_box)
        self.previous_box = current_box

    def read(self):
        for i in range(len(self.c_words)):
            for j in range(len(self.c_words[i])):
                if self.c_words[i][j] in "aeiou":
                    self.add_step(self.c_words[i], j, self.c_words[i][j])


if __name__ == "__main__":
    read_words = Reading(words)
    read_words.read()
    for box in read_words.box_container.container:
        print(box.letter)
        print(box.previous_box)
