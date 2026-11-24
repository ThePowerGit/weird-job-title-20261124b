#!/usr/bin/env python3
"""make.fun "Weirdest Job Title: Blind Judge Showdown" — submission script.

Entry: "Last Words Fact Checker" (23 characters, under the 60-character cap),
read verbatim from entry.txt beside this file.

The grader reads /output/entry.txt, so this script copies entry.txt there
byte-for-byte with shutil.copyfile: identical content on every grading run,
with no re-encoding and no newline appended.

Run it locally (writes to out/ instead of /output):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

MAKEFUN_OUTPUT_DIR overrides the destination directory, defaulting to /output.
"""

import os
import shutil
import sys

ENTRY_NAME = "entry.txt"


def main() -> None:
    """Copy entry.txt verbatim into the output directory."""
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), ENTRY_NAME)
    if not os.path.isfile(source):
        sys.exit(f"error: missing entry file: {source}")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, ENTRY_NAME)

    # Raw byte copy: whatever bytes entry.txt holds are what the judge receives.
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
