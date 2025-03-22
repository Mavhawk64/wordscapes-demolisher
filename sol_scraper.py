from collections import Counter
from functools import reduce

import requests
from bs4 import BeautifulSoup

from wordscapes_path_lookup import get_path


def get_letters(level=1):
    uri = "https://wordscapes.yourdictionary.com/answers"
    path = get_path(level)
    if path.startswith("Level"):
        print(f"{path}")
        return {
            "level": level,
            "error": f"Level {level} not found.",
            "main_words": [],
            "bonus_words": [],
            "circle_letters": [],
            "letter_frequencies": {},
        }

    url = f"{uri}{path}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <ul> blocks that contain word lists
    ul_lists = soup.find_all("ul", {"class": "list", "data-v-1e90d285": ""})

    # Handle both 1-UL and 2-UL cases
    if len(ul_lists) == 1:
        bonus_words = []
        main_words = [li.text.strip() for li in ul_lists[0].find_all("li")]
    elif len(ul_lists) >= 2:
        bonus_words = [li.text.strip() for li in ul_lists[0].find_all("li")]
        main_words = [li.text.strip() for li in ul_lists[1].find_all("li")]
    else:
        bonus_words = []
        main_words = []

    # Calculate correct circle letters with repetition
    if main_words:

        def merge_max(c1, c2):
            return c1 | c2

        circle_counter = reduce(
            merge_max, (Counter(word.upper()) for word in main_words)
        )
        circle_letters = sorted(
            letter for letter, count in circle_counter.items() for _ in range(count)
        )
    else:
        circle_counter = Counter()
        circle_letters = []

    # sort main words on length desc
    main_words.sort(key=len, reverse=True)

    # Return all useful info
    return {
        "level": level,
        "error": "",
        "main_words": main_words,
        "bonus_words": bonus_words,
        "circle_letters": circle_letters,
        "letter_frequencies": dict(circle_counter),
    }
