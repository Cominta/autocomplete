from scripts.processing.helpers import fileIter, lineIter, tokenize, documentIter

from collections import Counter
import re

def createBigrams(dir: str) -> Counter:
    bigrams = Counter()

    for file in fileIter(dir):
        for line in documentIter(file):
            sentences = re.split(r"[.!?]+", line)

            for sentence in sentences:
                words = tokenize(sentence)

                for i in range(len(words) - 1):
                    pair = (words[i], words[i + 1])
                    bigrams[pair] += 1

    return bigrams