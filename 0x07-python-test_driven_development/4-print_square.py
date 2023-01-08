#!/usr/bin/python3
"""Define function: print_square"""


def print_square(size):
    """Print a square with the character #

    Args:
        size (int) The length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    elif size == 0:
        pass
    else:
        for i in range(size ** 2):
            if i and not(i % size):
                print()
            print(f'#', end='')
        print()
