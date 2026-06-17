from collections import Counter

logName = "Stats"

def baseStats(freq: Counter) -> None:
    print(f"{logName}: Base statistics")
    print(f"\tCount of words: {sum(freq.values())}")
    print(f"\tCount of unique words: {len(freq)}")
    singletons = sum(1 for count in freq.values() if count == 1)
    print(f"\tSingletons = {singletons} ({100 * singletons / len(freq):.2f}%)")

def frequencyThreshold(freq: Counter, thresholds: list[int]) -> None:
    print(f"{logName}: Threshold statistics ({thresholds})")
    for threshold in thresholds:
        count = sum(1 for freqCount in freq.values() if freqCount >= threshold)
        print(f"\t>={threshold} {count} ({100 * count / len(freq):.2f}%)")

def coverage(freq: Counter) -> None:
    print(f"{logName}: Coverage statistics")
    totalTokens = sum(freq.values())
    targets = [0.9, 0.95, 0.99]
    targetIndex = 0
    running = 0

    for index, (word, count) in enumerate(freq.most_common(), start=1):
        running += count
        coverage = running / totalTokens

        while (targetIndex < len(targets) and coverage >= targets[targetIndex]):
            print(f"\t{targets[targetIndex] * 100:.0f}% coverage: {index} words")
            targetIndex += 1

        if targetIndex == len(targets):
            break

def coverageAtThreshold(freq: Counter, thresholds: list[int]) -> None:
    print(f"{logName}: Coverage at thresholds statistics ({thresholds})")
    total = sum(freq.values())

    for threshold in thresholds:
        covered = sum(count for word, count in freq.items() if count >= threshold)
        print(f"\t>={threshold} {covered / total * 100:.2f}% coverage")