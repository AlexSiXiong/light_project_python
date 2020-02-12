#!/usr/bin/env python3
"""a puzzle that uses dictionary"""

import argparse


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('text',
                        metavar='str',
                        type=str,
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """ Entrance """
    args = get_args()
    info = args.text
    result = convert_text(info)
    print(result)


# --------------------------------------------------
def convert_text(text) -> str:
    """convert the text using dictionary"""

    digits_dictionary = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5',
    }
    keys = digits_dictionary.keys()
    result = ''

    for i in text:
        if i in keys:
            result += digits_dictionary.get(i)
        else:
            result += i

    return result


# --------------------------------------------------
if __name__ == '__main__':
    main()
