import sys 
import re 
from collections import Counter

WORD_RE = re.compile(r"[a-záäčďéíĺľňóôŕšťúýž]+")
VALID_WORD = re.compile(r"^[a-záäčďéíĺľňóôŕšťúýž]{3,}$")

counter = Counter()

for line in sys.stdin: 
    for word in WORD_RE.findall(line.lower()):
        if not VALID_WORD.match(word):
            continue

        counter[word] += 1

for word, freq in counter.most_common():
    print(f"{word}\t {freq}")