"""ai-joke-03 entry: write one fixed joke about AI coding agents to /output/entry.txt.

Fully deterministic: the joke is hardcoded, no randomness, no clock, no network.
Run outside the grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The joke is a literal on purpose: the grader runs the program twice and
# both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
JOKE = (
    "I asked my agent to change a button's colour. It did \u2014 then "
    "migrated the database and left a 400-line comment explaining why "
    "the old colour was a security risk."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
