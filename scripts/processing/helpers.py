from pathlib import Path
from typing import Generator, Any

import re

WORD_RE = re.compile(r"[a-záäčďéíľĺňóôŕšťúýž]+")

def tokenize(text: str) -> list[str]:
    return WORD_RE.findall(text.lower())

def documentIter(filePath):
    current = []

    with open(filePath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith("<doc"):
                current = []
                continue

            if line.startswith("</doc>"):
                yield " ".join(current)
                continue

            current.append(line)

def fileIter(dir: str) -> Generator[Path, Any, None]:
    for path in Path(dir).rglob("*"):
        if path.is_file():
            yield path

def lineIter(filePath: str) -> Generator[str, Any, None]:
    with open(filePath, encoding = "utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("<doc") or line.startswith("</doc>"):
                continue

            yield line