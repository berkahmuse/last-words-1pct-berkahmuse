#!/usr/bin/env python3
"""Famous Last Words at 1 Percent -- @berkahmuse entry.

Writes the funniest one-line farewell a phone could say as its battery
hits 1 percent, in the phone's own voice, to /output/entry.txt.

The line (123 characters, one line):
  I kept your photos, your passwords, and your 3 a.m. search for
  'is my phone spying on me.' Yes. I'm taking it to the grave.
"""

import os

LINE = (
    "I kept your photos, your passwords, and your 3 a.m. search for "
    "'is my phone spying on me.' Yes. I'm taking it to the grave."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
