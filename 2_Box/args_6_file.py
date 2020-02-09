#!/usr/bin/env python3
"""Python version of `cat -n`"""

import argparse


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    """Get command-line args"""

    parser = argparse.ArgumentParser(
        description='Python version of `cat -n`',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'file',
        metavar='FILE',
        type=argparse.FileType('r'),
        help='Input file',
    )

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """Entrance"""

    args = get_args()

    for i, line in enumerate(args.file, start=1):
        print(f'{i:6}  {line}', end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
