import argparse

from scripts import config


def generateArgumentParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--skip-buildFreq",
        action="store_true",
        default=False,
        help="Skip building frequency file"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        default=False,
        help="Print statistics"
    )
    parser.add_argument(
        "--skip-bigrams",
        action="store_true",
        default=False,
        help="Print statistics"
    )

    return parser