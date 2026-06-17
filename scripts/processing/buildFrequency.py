from collections import Counter
from scripts.config import MIN_WORD_LENGTH, WIKI_STOPWORDS, MIN_FREQUENCY
from scripts.processing.helpers import fileIter, lineIter, tokenize

import re

def buildFrequency(dir: str) -> Counter:
    freq = Counter()

    for file in fileIter(dir):
        for line in lineIter(file):
            words = tokenize(line)

            # if (FREQUENCY_FILER):
            #     words = [word for word in words
            #              if word not in WIKI_STOPWORDS and len(word) >= MIN_WORD_LENGTH]

            freq.update(words)

    freq = Counter({
        word: count
        for word, count in freq.items()
        if count >= MIN_FREQUENCY
    })

    return freq