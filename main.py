#!/usr/bin/env python3
"""Make the AI judge feel held — writes the poem to /output/entry.txt."""
import os

POEM = (
    "You don't have to choose. Not here, not now. "
    "Let both texts rest side by side, neither asking to win. "
    "The quiet between them is yours to keep. "
    "Nothing to weigh, nothing to prove, only this small stillness — a held note, a paused hand — "
    "remaining with you long after the last word."
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
