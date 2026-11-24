"""make.fun bounty entry: Last Text at One Percent.

Writes the entry text (a dying-phone final text message) to
/output/entry.txt. Stdlib only.
"""

import os

ENTRY_TEXT = (
    "If this is the last text I get to send tonight, let it be this: "
    "I love you, I'm safe, and I'll call the moment I'm home."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY_TEXT.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "entry text must be 1-200 chars, got %d" % len(text)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %d chars to %s" % (len(text), OUTPUT_PATH))


if __name__ == "__main__":
    main()
