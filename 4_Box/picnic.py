#!/usr/bin/env python3

import argparse


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    """ get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('-s',
                        '--sorted',
                        default=False,
                        action='store_true',
                        help='Sort the items (default: False)'

                        )

    parser.add_argument('food',
                        metavar='str',
                        type=str,
                        help='Item(s) to bring',
                        nargs='+')

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """Entrance"""

    args = get_args()
    food = args.food
    formatted_food = ''

    flag = args.sorted
    food = sorted(food) if flag is True else food

    if len(food) == 1:
        formatted_food = food[0]
    elif len(food) == 2:
        formatted_food = ' and '.join(map(str, food))
    elif len(food) >= 3:
        formatted_food = ', '.join(map(str, food))
        index = formatted_food.rfind(',')
        formatted_food = formatted_food[:index + 1] + ' and ' + formatted_food[index + 2:]

    print(f'You are bringing {formatted_food}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
