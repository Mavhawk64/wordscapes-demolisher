from difflib import get_close_matches

import pytesseract
from PIL import Image, ImageDraw, ImageOps


def recognize_letter_from_image(image_path, valid_letters, invert=False):
    # Load and convert image
    image = Image.open(image_path).convert("L")

    # Get image size and calculate diamond mask coordinates
    w, h = image.size
    center = (w // 2, h // 2)
    diamond = [
        (center[0], 0),  # top
        (w, center[1]),  # right
        (center[0], h),  # bottom
        (0, center[1]),  # left
    ]

    # Create diamond mask
    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon(diamond, fill=255)

    # If invert is True, flip white ↔ black after applying the mask
    bg_color = 0 if invert else 255
    image_out = Image.new("L", (w, h), bg_color)
    image_out.paste(image, mask=mask)

    # Optional: invert
    if invert:
        image_out = ImageOps.invert(image_out)

    # Debug: save intermediate image
    image_out.save("image_debug.png")

    # Threshold binarization
    image_out = image_out.point(lambda x: 0 if x < 128 else 255, "1")

    # OCR
    ocr_result = pytesseract.image_to_string(
        image_out,
        config="--psm 10 -c tessedit_char_whitelist=" + "".join(valid_letters),
    )
    letter = ocr_result.strip().upper()

    # Return best match
    if letter in valid_letters:
        return letter

    match = get_close_matches(letter, valid_letters, n=1, cutoff=0.5)
    if match:
        return match[0]
    elif not invert:
        return recognize_letter_from_image(image_path, valid_letters, invert=True)

    return None


if __name__ == "__main__":
    image_path = "letter.png"
    # fmt: off
    valid_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # fmt: on
    letter = recognize_letter_from_image(image_path, valid_letters)
    print(letter)  # Output: recognized letter or None
