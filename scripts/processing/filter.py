from collections import Counter

from scripts.config import MIN_WORD_LENGTH, WIKI_STOPWORDS, MIN_FREQUENCY, MIN_BIGRAM_FREQUENCY, MAX_WORD_LENGTH


def isValidWord(word: str) -> bool:
    return (len(word) >= MIN_WORD_LENGTH and word not in WIKI_STOPWORDS
            and "," not in word
            and "=" not in word
            and "\t" not in word
            and "\n" not in word)

def filterFreq(freq: Counter) -> Counter:
    return Counter({
        word: count
        for word, count in freq.items()
        if isValidWord(word) and len(word) <= MAX_WORD_LENGTH
    })

def filterBigrams(bigrams: Counter, filteredFreq: Counter) -> Counter:
    return Counter({
        (w1, w2): count
        for (w1, w2), count in bigrams.items()
        if (
                count >= MIN_BIGRAM_FREQUENCY
                and w1 in filteredFreq
                and w2 in filteredFreq
        )
    })