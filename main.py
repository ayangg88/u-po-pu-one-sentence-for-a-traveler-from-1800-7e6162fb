"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a time
traveler who has just stepped out of the year 1800, to /output/entry.txt.
The sentence is built only from things a person from 1800 already knows
(a road, a house, a letter, a book, a song, a horse) and stays within
the 200-character limit. Its one image, a road of light, is true as well
as vivid: the messages really do travel as light along thin glass roads.
"""

import os

ENTRY = (
    "It is a road of light joining every house on earth, down which "
    "letters, books, and songs run faster than any horse, at any hour, "
    "for anyone who asks."
)


def main() -> None:
    assert ENTRY, "entry must not be empty"
    assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing whitespace"
    assert ENTRY.count(".") == 1, "entry must be a single sentence"
    assert "\n" not in ENTRY, "entry must be one line"
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over the 200 limit"
    assert 1 <= len(ENTRY), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
