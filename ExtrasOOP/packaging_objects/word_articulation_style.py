# Words articulation style for particular language

from typing import Optional

words = ["Bicycle", "Elections", "Popularity", "Football", "Airplane"]


class Letter:

    letter_articulations = {
        "a": "open vowel",
        "b": "bilabial consonant",
        "c": "teeth labial",
        "d": "teeth labial",
        "e": "teeth labial",
        "g": "teeth labial",
        "h": "teeth labial",
        "i": "teeth labial",
        "j": "teeth labial",
        "k": "teeth labial",
        "l": "teeth labial",
        "m": "teeth labial",
        "n": "teeth labial",
        "o": "teeth labial",
        "p": "teeth labial",
        "q": "teeth labial",
        "r": "teeth labial",
        "s": "teeth labial",
        "t": "teeth labial",
        "u": "teeth labial",
        "v": "teeth labial",
        "w": "teeth labial",
        "x": "teeth labial",
        "y": "teeth labial",
        "z": "teeth labial",
    }

    def __init__(self, word, letter):
        self.word = word
        self.letter = letter
        self.articulation = None

