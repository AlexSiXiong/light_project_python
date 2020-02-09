#!/usr/bin/env python3
"""
Sometimes you want to limit the values of an argument.
Maybe you offer shirts in only primary colors.
You can pass in a list of valid values using the [choices] option.

Here we restrict the color to one of "red," "yellow," or "blue."
"""

import argparse


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choices',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'color',
        metavar='str',
        type=str,
        help='Choice',
        choices=['red', 'yellow', 'blue'],
    )

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """Entrance"""

    args = get_args()
    print('color =', args.color)


# --------------------------------------------------
if __name__ == '__main__':
    main()

