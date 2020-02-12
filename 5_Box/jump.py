#!/usr/bin/env python3
"""a puzzle that uses dictionary"""

import argparse


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('command',
                        metavar='str',
                        type=str,
                        help='show this help message and exit')

    return parser.parse_args()


digits_dictionary = {
    1: 9,
    2: 8,
    3: 7,
    4: 6,
    5: 0,
    6: 4,
    7: 3,
    8: 2,
    9: 1,
    0: 5,
}
