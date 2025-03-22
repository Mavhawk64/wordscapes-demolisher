# cv2.cvtColor takes a numpy ndarray as an argument
# importing OpenCV
import math
from typing import List

import pyautogui as p

from letter_matcher import recognize_letter_from_image
from Letters import Center, Letter, Letters


def d_grab_letters(letters: List[str]) -> Letters:
    print(letters)
    poss = get_circle_letter_positions(996, 711, 120, letters)
    ret = Letters()
    for pos in poss:
        x, y = pos
        p.moveTo(x, y)
        p.sleep(0.2)
        p.screenshot(region=(x - 50, y - 40, 100, 100), imageFilename=f"letter.png")
        letter = recognize_letter_from_image(f"letter.png", letters)
        print(letter, x, y)
        p.mouseDown()
        p.sleep(0.2)
        p.mouseUp()
        if letter:
            ret.append(Letter(Center(x, y), letter, 1.0))
        else:
            raise ValueError("Letter not found")
    return ret


def get_circle_letter_positions(x_c, y_c, r, letters):
    positions = []
    N = len(letters)

    for i in range(N):
        theta = 2 * math.pi * i / N
        x = x_c + r * math.cos(theta - math.pi / 2)
        y = y_c + r * math.sin(
            theta - math.pi / 2
        )  # flip sign if needed for image coordinate system
        positions.append((round(x), round(y)))

    return positions
