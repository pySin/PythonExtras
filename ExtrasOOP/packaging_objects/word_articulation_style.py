# Words articulation style for particular language

from typing import Optional

words = ["Bicycle", "Elections", "Popularity", "Football", "Airplane"]


class Letter:

    letter_articulations = {
        "a": ["open vowel", "closed"],
        "b": ["bilabial consonant", "open"],
        "c": ["teeth labial", "open"],
        "d": ["teeth labial", "closed"],
        "e": ["teeth labial", "open"],
        "g": ["teeth labial", "open"],
        "h": ["teeth labial", "open"],
        "i": ["teeth labial", "open"],
        "j": ["teeth labial", "closed"],
        "k": ["teeth labial", "closed"],
        "l": ["teeth labial", "closed"],
        "m": ["teeth labial", "open"],
        "n": ["teeth labial", "closed"],
        "o": ["teeth labial", "closed"],
        "p": ["teeth labial", "open"],
        "q": ["teeth labial", "closed"],
        "r": ["teeth labial", "open"],
        "s": ["teeth labial", "open"],
        "t": ["teeth labial", "open"],
        "u": ["teeth labial", "closed"],
        "v": ["teeth labial", "closed"],
        "w": ["teeth labial", "open"],
        "x": ["teeth labial", "open"],
        "y": ["double vowel", "closed"],
        "z": ["double teeth", "closed"]
    }

    def __init__(self, word: str, letter: str):
        self.word = word
        self.letter = letter
        self.articulation = Letter.letter_articulations[letter[0]]
        self.openness = Letter.letter_articulations[letter[1]]


class Word:

    def __init__(self, word: str):
        self.word = word
        self.letters: list[Letter] = []

    def add_letter(self, letter: str):
        self.letters.append(Letter(self.word, letter))


class Read:

    def __init__(self, current_words):
        self.current_words = current_words
        self.words_info: list[Word] = []

    def word_profiles(self):
        for word in self.current_words:
            self.words_info.append(Word(word))


if __name__ == "__main__":
    words_traits = Read(words)
    print(words_traits)
