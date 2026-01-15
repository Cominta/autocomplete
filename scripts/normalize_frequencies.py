import sys 
import math 

with open("stopwords.txt", encoding="utf-8") as f:
    STOPWORDS = set(w.strip() for w in f)

    MAX_FREQ = 255 

    words = []
    for line in sys.stdin: 
        word, freq = line.strip().split()

        if word in STOPWORDS:
            continue

        words.append((word, int(freq)))

    max_raw = max(freq for _, freq in words)

    for word, freq in words: 
        norm = int(MAX_FREQ * math.log(freq + 1) / math.log(max_raw + 1))

        if (norm > 0):
            print(f"{word}\t{norm}")