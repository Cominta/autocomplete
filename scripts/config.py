from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

OUT_DICT = BASE_DIR / "data/sk_wordlist.txt"

EXTRACTED_DIR = BASE_DIR / "data/raw/rawText"
ADDITIONAL_DIR = BASE_DIR / "data/raw/additionalData"
ADDITIONAL_FREQ = ADDITIONAL_DIR / "freq"
ADDITIONAL_BIGRAMS = ADDITIONAL_DIR / "bigrams"

PROCESSING_FILTER = True

FREQUENCIES_DIR = BASE_DIR / "data"
FREQUENCIES_FILE = "frequencies.txt"
MIN_WORD_LENGTH = 2
MIN_FREQUENCY = 4
MIN_BIGRAM_FREQUENCY = 5
MAX_WORD_LENGTH = 30

BIGRAMS_DIR = BASE_DIR / "data"
BIGRAMS_FILE = "bigrams.txt"

MAX_BIGRAMS = 3
MAX_WORDS = 400_000

WIKI_STOPWORDS = {
    "pozri",
    "odkazy",
    "externé",
    "stránka",
    "stránke",
    "oficiálna",
    "isbn",
    "tzv",
    "napr",
    "ii",
    "iii",
    "iv",
    "the",
    "of",
    "and",
    "for",
    "with",
    "from",
    "open",
    "live",
    "http",
    "www",
    "org",
    "com",
    "isbn",
    "ngc",
    "pgc",
    "graf",
    "departement",
    "departementu",
    "francúzska",
    "J.",
    "K.",
    "L.",
    "M.",
    "N.",
    "s."
}