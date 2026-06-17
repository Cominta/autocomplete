from collections import Counter
from pathlib import Path

def addHeader(file, filtered) -> None:
    file.write("FILTERED\n" if filtered else "RAW\n")

def readHeader(file):
    header = file.readline().strip()

    if (header == "FILTERED"):
        return True

    return False

def saveFrequency(freq: Counter, outputFile: Path, filtered: bool) -> None:
    with open(outputFile, "w", encoding = "utf-8") as file:
        addHeader(file, filtered)
        for word, count in freq.most_common():
            file.write(f"{word} {count}\n")

def saveBigrams(bigrams: Counter, outputFile: Path, filtered: bool) -> None:
    with open(outputFile, "w", encoding = "utf-8") as file:
        addHeader(file, filtered)
        for (w1, w2), count in bigrams.most_common():
            file.write(f"{count} {w1} {w2}\n")

def loadFrequency(inputFile: Path, additional: bool) -> (Counter, bool):
    with open(inputFile, "r", encoding = "utf-8") as file:
        freq = Counter()
        filtered = False

        if (not additional):
            filtered = readHeader(file)

        for line in file:
            freq[line.split()[0]] = int(line.split()[1])

    return (freq, filtered)

def loadBigrams(inputFile: Path, additional: bool) -> (Counter, bool):
    with open(inputFile, "r", encoding = "utf-8") as file:
        bigrams = Counter()
        filtered = False

        if (not additional):
            filtered = readHeader(file)

        for line in file:
            lineSplit = line.split()
            pair = (lineSplit[1], lineSplit[2])
            bigrams[pair] = int(lineSplit[0])

    return (bigrams, filtered)