#!/user/bin/env python3
"""nargs=+, addition for n arguments"""

import argparse


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='nargs=+',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'numbers',
        metavar='INT',
        nargs='+',
        type=int,
        help='Numbers'
    )

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """Entrance"""

    args = get_args()
    numbers = args.numbers

    print('{} = {}'.format(' + '.join(map(str, numbers)), sum(numbers)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
