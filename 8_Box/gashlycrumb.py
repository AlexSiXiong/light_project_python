#!/usr/bin/env python3

import argparse
import sys


# --------------------------------------------------
def get_args():
    """ get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('letter',
                        metavar='str',
                        type=str,
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        metavar='str',
                        type=argparse.FileType('r'),
                        help='Input file (default: gashlycrumb.txt)',
                        default='gashlycrumb.txt',
                        )

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """ Entrance """

    args = get_args()

    digits_dictionary = {
        line[0].upper(): line.rstrip() for line in args.file
    }

    letters_box = []
    for letter in args.letter:
        letters_box.append(letter)

    sentences = converter(letters_box, digits_dictionary)
    for i in sentences:
        print(i)

    for line in args.file:
        print(line.rstrip())


def count_characters(line) -> int:
    """if you do not want count Line Breaks and Spaces in lines"""

    characters = 0
    for word in line:
        if word != '\n' and word != ' ':
            characters += 1
    return characters


# --------------------------------------------------
def converter(letters, digits_dictionary):
    sentences = []

    keys = digits_dictionary.keys()

    for first_letter in letters:
        if first_letter.upper() in keys:
            sentences.append(digits_dictionary.get(first_letter.upper()))
        else:
            sentences.append('I do not know "' + first_letter + '".')
    return sentences


if __name__ == '__main__':
    main()
