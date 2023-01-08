#!/usr/bin/python3
"""Define function: text_indentation"""


def text_indentation(text):
    """Print a test with 2 newline after
        each of these character .,?

    Args:
        text (str): sample text

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while (i < len(text)):
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print('\n')
            j =i + 1
            while text[j] == ' ':
                i += 1
                j += 1
        i += 1
