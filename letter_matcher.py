from difflib import get_close_matches

import pytesseract
from PIL import Image


def recognize_letter_from_image(image_path, valid_letters):
    # Run Tesseract OCR
    image = Image.open(image_path)
    ocr_result = pytesseract.image_to_string(
        image, config="--psm 10 -c tessedit_char_whitelist=" + "".join(valid_letters)
    )
    letter = ocr_result.strip().upper()

    # Try exact match first
    if letter in valid_letters:
        return letter

    # Try fuzzy match if OCR is wrong
    match = get_close_matches(letter, valid_letters, n=1, cutoff=0.5)
    if match:
        return match[0]

    # If no match found
    return None


if __name__ == "__main__":
    image_path = "letter.png"
    # fmt: off
    valid_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # fmt: on
    letter = recognize_letter_from_image(image_path, valid_letters)
    print(letter)  # Output: recognized letter or None
