#!/usr/bin/env python3
"""Two positional arguments"""

import argparse


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    """ get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Two positional arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('color',
                        metavar='str',
                        type=str,
                        help='Color',
                        )

    parser.add_argument('size',
                        metavar='int',
                        type=int,
                        help='Size'
                        )

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """ Entrance """

    args = get_args()
    print('color =', args.color)
    print('size =', args.size)


# --------------------------------------------------
if __name__ == '__main__':
    main()