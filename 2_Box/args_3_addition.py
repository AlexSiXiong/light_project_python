#!/usr/bin/env python3
""" addition - two arguments """

import argparse


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='nargs=2, addition',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('numbers',
                        metavar='int',
                        nargs=2,
                        type=int,
                        help='Numbers'
                        )

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """Entrance"""

    args = get_args()
    n1, n2 = args.numbers
    print(f'{n1} + {n2} = {n1 + n2}')


# --------------------------------------------------
if __name__ == '__main__':
    main()

