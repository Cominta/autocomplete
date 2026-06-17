from pathlib import Path

def validateCorpus(rootDir: str | Path) -> None:
    root = Path(rootDir)

    if not root.exists():
        raise FileNotFoundError(f"Corpus directory does not exist: {root}")

    print("-" * 60)
    print(f"{'Source':15} {'Files':>8} {'Size (MB)':>12} {'Errors':>8}")
    print("-" * 60)

    totalFiles = 0
    totalSize = 0
    totalErrors = 0

    for sourceDir in sorted(root.iterdir()):
        if not sourceDir.is_dir():
            continue

        files = 0
        errors = 0

        for file in sourceDir.rglob("*"):
            if not file.is_file():
                continue

            files += 1
            totalFiles += 1

            try:
                with open(file, "r", encoding="utf-8") as f:
                    while f.read(1024 * 1024):
                        pass

            except UnicodeDecodeError:
                errors += 1
                totalErrors += 1
                print(f"[UTF-8 ERROR] {file}")

            except Exception as e:
                errors += 1
                totalErrors += 1
                print(f"[ERROR] {file}: {e}")

        sizeBytes = sum(
            file.stat().st_size
            for file in sourceDir.rglob("*")
            if file.is_file()
        )

        print(
            f"{sourceDir.name:15}"
            f"{files:>8}"
            f"{sizeBytes / 1024 / 1024:>12.1f}"
            f"{errors:>8}"
        )

        totalSize += sizeBytes / 1024 / 1024

    print("-" * 60)
    print(f"Total files: {totalFiles}")
    print(f"Total size: {totalSize:.1f} MB")
    print(f"Total errors: {totalErrors}")

    if totalErrors == 0:
        print("Corpus validation successful.")
    else:
        print("Corpus contains invalid files.")

    print("-" * 10)