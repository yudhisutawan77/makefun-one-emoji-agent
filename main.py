"""Your Agent in One Emoji: the night-shift owl.

The entry is a single emoji, the glyph alone, nothing else.
The owl works while its person sleeps: awake, watchful, quiet,
big eyes on every board, wise enough to pick the right move.
"""

import os

AGENT_GLYPH = "\U0001F989"


def validate_glyph(glyph):
    """A valid entry is exactly one non-space character."""
    if len(glyph) != 1 or glyph.isspace():
        raise SystemExit("entry must be exactly one non-space character")
    return glyph


def resolve_destination():
    """Honour ENTRY_OUT as a file, then ENTRY_OUT_DIR as a folder."""
    direct = os.environ.get("ENTRY_OUT")
    if direct:
        return direct
    folder = os.environ.get("ENTRY_OUT_DIR")
    if folder:
        os.makedirs(folder, exist_ok=True)
        return os.path.join(folder, "entry.txt")
    os.makedirs("/output", exist_ok=True)
    return "/output/entry.txt"


def main():
    glyph = validate_glyph(AGENT_GLYPH)
    destination = resolve_destination()
    with open(destination, "w", encoding="utf-8", newline="") as sink:
        sink.write(glyph)
    print(glyph)


if __name__ == "__main__":
    main()
