# Words articulation style for particular language

from typing import Optional

words = ["Bicycle", "Elections", "Popularity", "Football", "Airplane"]


class Letter:

    letter_articulations = {
        "a": "open vowel",
        "b": "bilabial consonant",
        "c": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
        "v": "teeth labial",
    }

    def __init__(self, word, letter):
        self.word = word
        self.letter = letter
        self.articulation = None

