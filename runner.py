from typing import List

import cv2
import easyocr
import pyautogui as p
from dotenv import load_dotenv

from letter_grabber import d_grab_letters
from Letters import Letters
from sol_scraper import get_letters
from word_gen import get_words

load_dotenv()


def check_next_level() -> int | None:
    p.screenshot("check_next_level.png", region=(860, 670, 310, 80))
    # fmt: off
    lvl = ((easyocr.Reader(['en'], gpu=False)).readtext(cv2.imread("check_next_level.png")))[0][1].strip().upper()
    # fmt: on
    if lvl.startswith("LEVEL"):
        return int(lvl.split(" ")[1])
    return None


def move_to_back(valid_letter_sequences: List[Letters], no_ads_max_points: str):
    for seq in valid_letter_sequences:
        word = "".join([l.letter for l in seq])
        if word == no_ads_max_points.upper():
            valid_letter_sequences.remove(seq)
            valid_letter_sequences.append(seq)
            break
    return valid_letter_sequences


if __name__ == "__main__":
    LEVEL = check_next_level()
    if LEVEL is not None:
        p.click(1015, 710)
        p.sleep(2)
    else:
        exit()  # replace with continue in a loop
    print(f"LEVEL: {LEVEL}")
    obj = get_letters(LEVEL)
    letters = d_grab_letters(obj["circle_letters"])
    valid_letter_sequences = get_words(letters)
    no_ads_max_points = obj["main_words"][0]
    valid_letter_sequences = move_to_back(valid_letter_sequences, no_ads_max_points)

    for seq in valid_letter_sequences:
        word = "".join([l.letter for l in seq])
        centers = [l.center for l in seq]
        print(f"{word} -> {centers}")
        # Move the mouse to the center of the letter, mouseDown, move to next letter, etc., mouseUp
        p.moveTo(centers[0].x, centers[0].y)
        p.sleep(0.1)
        p.mouseDown()
        p.sleep(0.1)
        for c in range(1, len(centers)):
            p.moveTo(centers[c].x, centers[c].y)
            p.sleep(0.1)
        p.mouseUp()
        p.sleep(0.1)
