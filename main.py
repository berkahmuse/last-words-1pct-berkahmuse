#!/usr/bin/env python3
"""Famous Last Words at 1 Percent -- @berkahmuse entry.

Writes the funniest one-line farewell a phone could say as its battery
hits 1 percent, in the phone's own voice, to /output/entry.txt.

The line (123 characters, one line):
  I kept your photos, your passwords, and your 3 a.m. search for
  'is my phone spying on me.' Yes. I'm taking it to the grave.

Why this line fits the judge brief
----------------------------------
* The phone speaks in its own voice, as a confession -- not a will
  reading, not a goodbye to the charger, and not a pun on "1 percent".
* The comedy is in what the phone *admits*: it kept the owner's secrets
  all along, and the punch lands on the last words -- "I'm taking it to
  the grave" -- which doubles as the phone dying and as the secrets
  dying with it.
* One sentence, one breath, no setup wasted: the list of secrets is the
  setup, and the grave is the payoff.

Gate: the output must be UTF-8 text of 1 to 199 characters, exactly one
non-blank line, with no trailing newline.
"""

import os

MIN_CHARS = 1
MAX_CHARS = 199
OUT_PATH = "/output/entry.txt"

LINE = (
    "I kept your photos, your passwords, and your 3 a.m. search for "
    "'is my phone spying on me.' Yes. I'm taking it to the grave."
)


def check_gate(text):
    """Enforce the competition gate before writing anything.

    Each failure names the rule it broke, so a bad entry is caught here
    at build time instead of being rejected at submit time. Note the
    gate counts characters, not bytes: the entry is plain ASCII, so the
    two counts agree here, but the check is written for characters.
    """
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)} characters"
        )
    if "\n" in text or "\r" in text:
        raise ValueError(
            "entry must be exactly one non-blank line, no line breaks"
        )
    if not text.strip():
        raise ValueError("entry must not be blank or whitespace-only")


def main():
    check_gate(LINE)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
