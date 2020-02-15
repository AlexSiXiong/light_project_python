#!/usr/bin/env python3

import argparse
import sys


# --------------------------------------------------
def get_args():
    """ get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin],
                        type=argparse.FileType('r'),
                        help='Input file(s)',
                        )

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """ Entrance """

    args = get_args()

    total_lines = 0
    total_words = 0
    total_char = 0

    for fh in args.file:
        lines = 0
        words = 0
        chars = 0
        for line in fh:
            lines += 1
            words += len(line.split())
            chars += len(line)
            # characters += count_characters(line)
        total_lines += lines
        total_words += words
        total_char += chars

        print(f'{lines:8}{words:8}{chars:8} {fh.name}')

    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_char:8} total')


def count_characters(line) -> int:
    """if you do not want count Line Breaks and Spaces in lines"""

    characters = 0
    for word in line:
        if word != '\n' and word != ' ':
            characters += 1
    return characters


if __name__ == '__main__':
    main()



