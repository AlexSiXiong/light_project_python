#!/usr/bin/env python3
"""Manually check an argument"""

import argparse


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Manually check an argument',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-v',
                        '--val',
                        help='Integer value between 1 and 10',  # brief description for usage
                        metavar='int',  # type hint for usage 这个是给提示用的
                        type=int,  # data type that the string must be converted to 这个是实际转换的
                        default=9,
                        )

    args = parser.parse_args()
    if not 1 <= args.val <= 10:
        parser.error(f'--val "{args.val}" must be between 1 and 10')

    return args


# --------------------------------------------------
def main() -> None:
    """Entrance"""

    args = get_args()
    print(f'val = {args.val}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
