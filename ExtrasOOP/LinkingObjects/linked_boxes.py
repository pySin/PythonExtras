# Linked Boxes
from typing import Optional

words = ["Bicycle", "Elections", "Popularity", "Football", "Airplane"]


class Box:

    def __init__(self, word_index, word, letter_index, letter, previous_box):
        self.word_index = word_index
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

    def add_step(self, word_index, word, letter_index, letter):
        current_box = Box(word_index, word, letter_index, letter, self.previous_box)
        self.box_container.container.append(current_box)
        self.previous_box = current_box

    def read(self):
        for i in range(len(self.c_words)):
            for j in range(len(self.c_words[i])):
                if self.c_words[i][j] in "aeiou":
                    self.add_step(i, self.c_words[i], j, self.c_words[i][j])
                else:
                    self.add_step(i, self.c_words[i], j, self.c_words[i][j])


if __name__ == "__main__":
    read_words = Reading(words)
    read_words.read()
    for box in read_words.box_container.container:
        print(box.letter)
        print(box.word)
        print("Word index:", box.word_index)
        print("Letter index:", box.letter_index)
        print(box.previous_box)

    # Link back Box objects
    box_item = read_words.box_container.container[-1]
    while box_item.previous_box is not None:
        print(box_item.word_index)
        print(box_item.letter_index)
        box_item = box_item.previous_box

