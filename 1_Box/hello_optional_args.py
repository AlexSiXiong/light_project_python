#!/usr/bin/env python3
"""
Purpose: Say hello
Author: Alex
"""

import argparse


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Say hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-n',  # short option name
                        '--name',  # long option name
                        default='World',
                        metavar='str',  # hind to user the data type
                        help='The name to greet')

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """Entrance"""

    args = get_args()
    print(greet(args.name))


# --------------------------------------------------
def greet(name: str) -> str:
    """Create a greeting"""

    return f'Hello {name}'


# --------------------------------------------------
def test_greet() -> None:
    """test greet"""

    assert greet('World') == 'Hello World'
    assert greet('a b') == 'Hello a b'


# --------------------------------------------------
if __name__ == '__main__':
    main()
