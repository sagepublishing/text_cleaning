"""This module contains method for removing footers."""


def remove_footers(string_value: str, opts: dict):
    """Removes the first line"""

    line = int(opts["footer_lines"])
    sent_text = string_value.split("\n")
    return ("\n").join(sent_text[: -(line + 1)])
