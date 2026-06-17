from scripts import config
from scripts import processing
from scripts import stats

from pathlib import Path

from scripts.export import buildDict
from scripts.generateArgumentParser import generateArgumentParser
from scripts.processing import fileIter, loadFrequency, loadBigrams

logName = "Main"

def main():
    parser = generateArgumentParser()
    args = parser.parse_args()

    freq = None
    bigrams = None
    filteredFreq = False
    filteredBigrams = False

    if (args.stats):
        print(f"{logName}: Corpus statistics (raw)")
        stats.validateCorpus(config.EXTRACTED_DIR)

        print()

        print(f"{logName}: Corpus statistics (additional, freq)")
        stats.validateCorpus(config.ADDITIONAL_FREQ)

        print()

        print(f"{logName}: Corpus statistics (additional, bigrams)")
        stats.validateCorpus(config.ADDITIONAL_BIGRAMS)

    if (not args.skip_buildFreq):
        print(f"{logName}: Building frequency")
        freq = processing.buildFrequency(config.EXTRACTED_DIR)

        print(f"{logName}: Additional frequency loading..")
        for file in fileIter(config.ADDITIONAL_FREQ):
            addFreq, filtered = loadFrequency(file, True)
            freq.update(addFreq)

        print(f"{logName}: Frequency building done")
        print("-" * 10)

    # if (not args.skip_bigrams):
    #     print(f"{logName}: Building bigrams")
    #     bigrams = processing.createBigrams(config.EXTRACTED_DIR)
    #
    #     print(f"{logName}: Additional bigrams loading..")
    #     for file in fileIter(config.ADDITIONAL_BIGRAMS):
    #         addBigrams, filtered = loadBigrams(file, True)
    #         bigrams.update(addBigrams)
    #
    #     print(f"{logName}: Bigrams building done")
    #     print("-" * 10)

    if (config.PROCESSING_FILTER):
        print(f"{logName}: Processing filter")

        if (freq is None):
            print(f"{logName}: Loading frequency from {Path(config.FREQUENCIES_DIR) / config.FREQUENCIES_FILE}")
            freq, filteredFreq = processing.loadFrequency(Path(config.FREQUENCIES_DIR) / config.FREQUENCIES_FILE, False)

        if (not filteredFreq):
            freq = processing.filterFreq(freq)
            print(f"{logName}: Frequency filtering done")
            filteredFreq = True

        else:
            print(f"{logName}: Already filtered frequency")

        # if (bigrams is None):
        #     print(f"{logName}: Loading bigrams from {Path(config.BIGRAMS_DIR) / config.BIGRAMS_FILE}")
        #     bigrams, filteredBigrams = processing.loadBigrams(Path(config.BIGRAMS_DIR) / config.BIGRAMS_FILE)
        #
        # if (not filteredBigrams):
        #     bigrams = processing.filterBigrams(bigrams, freq)
        #     print(f"{logName}: Bigrams filtering done")
        #     filteredBigrams = True
        #
        # else:
        #     print(f"{logName}: Already filtered bigrams")
        #
        # print("-" * 10)

    if (not args.skip_buildFreq):
        print(f"{logName}: Saving frequency, dir = {config.FREQUENCIES_DIR}, file = {config.FREQUENCIES_FILE}")
        freqPath = Path(config.FREQUENCIES_DIR) / config.FREQUENCIES_FILE
        freqPath.parent.mkdir(parents=True, exist_ok=True)
        processing.saveFrequency(freq, freqPath, filteredFreq)
        print(f"{logName}: Saved\n-----------")

    # if (not args.skip_bigrams):
    #     print(f"{logName}: Saving bigrams, dir = {config.BIGRAMS_DIR}, file = {config.BIGRAMS_FILE}")
    #     bigramsPath = Path(config.BIGRAMS_DIR) / config.BIGRAMS_FILE
    #     bigramsPath.parent.mkdir(parents=True, exist_ok=True)
    #     processing.saveBigrams(bigrams, bigramsPath, filteredBigrams)
    #     print(f"{logName}: Saved\n-----------")

    if (args.stats):
        if (freq is None):
            freq = processing.loadFrequency(Path(config.FREQUENCIES_DIR) / config.FREQUENCIES_FILE)

        print(f"{logName}: Statistics")
        stats.baseStats(freq)
        print()
        stats.frequencyThreshold(freq, [1, 2, 5, 10, 20, 50, 70, 100, 200])
        print()
        stats.coverage(freq)
        print()
        stats.coverageAtThreshold(freq, [1, 2, 5, 10, 20, 50, 70, 100, 200])
        print("-----------\n")

    buildDict(config.OUT_DICT)

    # print(len(freq))
    # singletons = sum(
    #     1
    #     for count in freq.values()
    #     if count == 1
    # )
    #
    # print(singletons)

if (__name__ == "__main__"):
    main()