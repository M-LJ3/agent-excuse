"""Write one funny line to /output/entry.txt.

The line is an entry for a one-line joke contest: the excuse
an AI agent gives you.
"""

import os


def joke_line():
    """Return one funny excuse from an agent."""
    return (
        "I did not crash your build — I was just giving the code "
        "some quiet time to think about what it did."
    )


def main():
    line = joke_line()
    os.makedirs("/output", exist_ok=True)
    # Write the excuse with no trailing newline, exactly as entered.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    # Sanity check: the file must hold exactly the one excuse line.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        assert handle.read() == line


if __name__ == "__main__":
    main()
