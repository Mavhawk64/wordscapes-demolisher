# 🧠 Wordscapes Auto-Solver

A Python-based automation tool that scrapes Wordscapes puzzle answers, identifies valid letter sequences, and simulates mouse movements to auto-solve the puzzle using computer vision and web scraping.

## 📌 Features

- 🔎 **Web Scraper**: Pulls Wordscapes level data (main and bonus words) from `yourdictionary.com`.
- 🧠 **OCR Integration**: Uses Tesseract to identify on-screen letters via screenshot.
- 🧩 **Word Matcher**: Generates all valid words from circle letters based on a local dictionary file (`words.txt`).
- 🖱️ **Auto Play**: Simulates mouse actions to draw out valid word sequences.
- 🤖 **Failsafe Handling**: Implements fuzzy matching in case of imperfect OCR results.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Tesseract-OCR installed and added to your system path
- `words.txt` — a local dictionary file with one word per line
- `wordscapes_levels.txt` — map of level ranges and groupings for scraping
- The game window should be visible and active during execution.

### Installation

```bash
pip install -r requirements.txt
```

Dependencies include:

- `pyautogui`
- `python-dotenv`
- `requests`
- `beautifulsoup4`
- `pytesseract`
- `Pillow`

### Tesseract Setup

Make sure Tesseract is installed:

- **Windows**: https://github.com/tesseract-ocr/tesseract
- **Mac**: `brew install tesseract`
- **Linux**: `sudo apt install tesseract-ocr`

## 📂 Project Structure

```
.
├── runner.py                  # Main script to run the solver
├── Letters.py                 # Data models for letters and coordinates
├── letter_grabber.py          # Captures letter positions and identifies them
├── letter_matcher.py          # OCR logic for identifying letters from screenshots
├── sol_scraper.py             # Web scraper for Wordscapes solution data
├── word_gen.py                # Generates valid letter sequences from available letters
├── wordscapes_path_lookup.py # Maps level numbers to URL paths
├── words.txt                  # Local dictionary
├── wordscapes_levels.txt      # Text mapping for level-to-path resolution
```

## ⚙️ Usage

Update the desired level number in `runner.py`:

```python
LEVEL = 20
```

Then run:

```bash
python runner.py
```

Ensure the Wordscapes puzzle is on screen and unobstructed.

## 📝 Notes

- Letters are arranged in a circle and OCR’d one-by-one using screenshots.
- The solver prioritizes the longest words first.
- A "no-ads" main word is moved to the back of the sequence so it can be triggered last.

## 🛠️ Troubleshooting

- **OCR misreads letters**? Improve screenshot quality or adjust Tesseract config.
- **Mouse events not aligning?** Tune the circle center and radius in `letter_grabber.py`.

## 📃 License

MIT License. Use at your own discretion—this project is for educational purposes only.
