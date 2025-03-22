from typing import List


class Center(object):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


class Letter(object):
    VALID_LETTERS = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    def __init__(self, center: Center, letter: str, score: float):
        self.center = center
        self.letter = "O" if letter == "0" else letter.upper()
        self.score = score
        if self.letter not in Letter.VALID_LETTERS:
            raise ValueError(f"Invalid letter: {self.letter}")

    def __str__(self):
        return f"{self.letter} ({self.center.x}, {self.center.y})"


class Letters(object):
    def __init__(self, letters: List[Letter]):
        self.letters = letters

    def __init__(self):
        self.letters = []

    def __getitem__(self, index):
        return self.letters[index]

    def __len__(self):
        return len(self.letters)

    def __iter__(self):
        return iter(self.letters)

    def __str__(self):
        return str([str(letter) for letter in self.letters])

    def __repr__(self):
        return self.__str__()

    def append(self, letter):
        self.letters.append(letter)

    def extend(self, letters):
        self.letters.extend(letters)
