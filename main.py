"""Produce a single excuse line and save it for the contest.

The program writes one excuse, as given by an AI agent, to
/output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")


def agent_excuse():
    """Return the one excuse line for this entry."""
    return (
        "I was halfway through your task when my context window "
        "filled up, so I had to forget the beginning to remember the end."
    )


def confirm_saved(line):
    """Check the stored file still matches the excuse we wrote."""
    stored = OUTPUT_PATH.read_text(encoding="utf-8")
    assert stored == line


def main():
    line = agent_excuse()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Persist the excuse exactly, with no newline at the end.
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    # Double-check the saved text is the excuse, character for character.
    confirm_saved(line)


if __name__ == "__main__":
    main()
