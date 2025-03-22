import itertools
from typing import List

from letter_grabber import grab_letters
from Letters import Letter, Letters


def get_words(letters: Letters) -> List[Letters]:
    # Read and normalize dictionary words
    with open("words.txt", "r") as f:
        words = set(
            word.strip().upper() for word in f if 3 <= len(word.strip()) <= len(letters)
        )

    valid_words = []

    for word in words:
        result = find_letter_sequence(word, letters)
        if result is not None:
            valid_words.append(result)

    # order by length
    valid_words.sort(key=len, reverse=True)
    return valid_words


def find_letter_sequence(word: str, available_letters: Letters) -> Letters:
    used_indices = set()
    word_letters = Letters()

    for ch in word:
        for i, letter in enumerate(available_letters):
            if i not in used_indices and letter.letter == ch:
                used_indices.add(i)
                word_letters.append(letter)
                break
        else:
            # Letter not found or already used
            return None

    return word_letters


if __name__ == "__main__":
    letters = grab_letters()
    valid_letter_sequences = get_words(letters)

    for seq in valid_letter_sequences:
        word = "".join([l.letter for l in seq])
        centers = [l.center for l in seq]
        print(f"{word} -> {centers}")
