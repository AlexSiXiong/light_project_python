#!/bin/usr/env python3
"""
Purpose: Say hello
Author: Alex
"""

import argparse


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    """ dedicated to getting the command-line arguments"""

    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('name', metavar='str', help='The name to greet')
    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """ Entrance """

    args = get_args()
    print(greet(args.name))


# --------------------------------------------------
def greet(name: str) -> str:
    """ Creat a greeting """

    return f'Hello {name}'


# --------------------------------------------------
def test_greet() -> None:
    """ Test greet"""

    assert greet('World') == 'Hello World'
    assert greet('c c') == 'Hello c c'
