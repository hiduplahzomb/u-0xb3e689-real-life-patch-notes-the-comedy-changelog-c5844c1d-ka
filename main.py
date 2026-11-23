"""One-line entry for make.fun's "Real-Life Patch Notes" bounty.

A terse software patch note for a bug in real life: sleep's nightly
recharge is broken. The joke is a release note treating the human body
as shipped software — the sleep cycle runs its full course while the
user still wakes up with an empty battery. The failure lands faster
because no procedural filler sits between the cycle and the 0%.
"""

import os
import sys

# The entry: one line, 1-160 characters.
# Angle: sleep bug — the 8-hour cycle runs, the user wakes at 0%.
TEXT = (
    "v2.4.1: fixed a bug where a full 8-hour sleep cycle ran but the "
    "user still woke up at 0% battery."
)


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if not (1 <= len(TEXT) <= 160):
        print(f"gate failed: entry is {len(TEXT)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(TEXT)} characters -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
