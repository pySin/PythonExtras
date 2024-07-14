# Words articulation style for particular language

from typing import Optional

words = ["Bicycle", "Elections", "Popularity", "Football", "Airplane"]


class Letter:
    # Letter object with arbitrary number of characteristics

    # Dictionary with letter traits
    letter_articulations = {
        "a": ["open vowel", "closed"],
        "b": ["bilabial consonant", "open"],
        "c": ["teeth labial", "open"],
        "d": ["teeth labial", "closed"],
        "e": ["teeth labial", "open"],
        "g": ["teeth labial", "open"],
        "f": ["teeth labial", "open"],
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
        self.articulation = Letter.letter_articulations[letter][0]
        self.openness = Letter.letter_articulations[letter][1]


class Word:
    # Create a word package of letters with specific
    # characteristics.

    def __init__(self, word: str):
        self.word = word
        self.letters: list[Letter] = []

    # Add characterised letter representations to a letters
    # container to form a package.
    def add_letter(self, letter: str):
        self.letters.append(Letter(self.word, letter))


class Read:
    # Read and organise the word representations.

    def __init__(self, current_words):
        self.current_words = current_words
        self.words_info: list[Word] = []

    # Create the word and letter representations. Organise them
    # in a container.
    def word_profiles(self):
        for word in self.current_words:
            word_o = Word(word)
            for letter in word:
                word_o.add_letter(letter.lower())
            self.words_info.append(word_o)


# Create objects and call functions to form word profiles.
if __name__ == "__main__":
    words_traits = Read(words)
    words_traits.word_profiles()
    for word_package in words_traits.words_info:
        print(word_package)
        for o_letter in word_package.letters:
            print(o_letter.letter)
            print(o_letter.articulation)
            print(o_letter.openness)
            print(o_letter)
