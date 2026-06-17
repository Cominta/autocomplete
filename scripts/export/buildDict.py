from collections import defaultdict, Counter
import heapq
import time
from pathlib import Path
import math

from scripts.config import FREQUENCIES_DIR, FREQUENCIES_FILE, ADDITIONAL_BIGRAMS, MAX_WORDS, MIN_WORD_LENGTH, \
    MAX_WORD_LENGTH

from scripts.processing.helpers import fileIter
from scripts.processing.filehandler import loadFrequency
from scripts.config import MAX_BIGRAMS

logName = "BuildDict"

def normalize(value: int, max_value: int) -> int:
    if value <= 0:
        return 1

    return max(1, min(255, round(255 * math.log1p(value) / math.log1p(max_value))))

def buildDict(outputFile: Path):
    print(f"{logName}: Loading frequencies...")

    freq_raw, _ = loadFrequency(FREQUENCIES_DIR / FREQUENCIES_FILE, additional=False)

    freq = Counter()

    for word, count in freq_raw.items():
        word = word.strip().lower()

        if not word:
            continue

        if word.count("-") > 1:
            continue

        if not all(ch.isalpha() or ch == "-" for ch in word):
            continue

        if len(word) < MIN_WORD_LENGTH or len(word) > MAX_WORD_LENGTH:
            continue

        freq[word] += count

    maxFreq = max(freq.values())
    validWords = set(freq.keys())

    print(f"{logName}: Loading bigrams...")
    bigrams = defaultdict(list)

    for file in fileIter(ADDITIONAL_BIGRAMS):
        print(f"{logName}: Reading", file)

        with open(file, encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()

                if len(parts) != 3:
                    continue

                try:
                    count = int(parts[0])
                except ValueError:
                    continue

                w1 = parts[1].strip().lower()
                w2 = parts[2].strip().lower()

                if w1 not in validWords:
                    continue

                if w2 not in validWords:
                    continue

                heap = bigrams[w1]

                if len(heap) < MAX_BIGRAMS:
                    heapq.heappush(heap, (count, w2))

                else:
                    heapq.heappushpop(heap, (count, w2))

    print(f"{logName}: Writing dictionary...")

    with open(outputFile, "w", encoding="utf-8") as out:
        out.write(
            f"dictionary=main:sk,"
            f"locale=sk,"
            f"description=Slovencina,"
            f"date={int(time.time())},"
            f"version=1\n"
        )

        for i, (word, wordFreq) in enumerate(freq.most_common()):
            if (i >= MAX_WORDS):
                break

            if not any(ch.isalpha() for ch in word):
                continue

            normalized = normalize(wordFreq, maxFreq)

            out.write(
                f" word={word},"
                f"f={normalized},"
                f"flags=,"
                f"originalFreq={normalized}\n"
            )

            if word not in bigrams:
                continue

            lst = sorted(bigrams[word], reverse = True)
            max_bigram = lst[0][0]

            for count, next_word in lst:
                out.write(f"  bigram={next_word},f={normalize(count, max_bigram)}\n")

    print(f"{logName}: Done.")