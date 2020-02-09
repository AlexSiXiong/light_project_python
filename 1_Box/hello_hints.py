#!/usr/bin/env python3
# Purpose: say hello

import os
import sys


def greet(name: str) -> str:
    return f'Hello {name}'


def test_greet() -> None:
    assert greet('World') == 'Hello World'
    assert greet('Axe Jack') == 'Hello Axe Jack'


def main() -> None:
    args = sys.argv[1:]
    if len(args) != 1:
        prg_name = os.path.basename(sys.argv[0])
        print(f'usage: {prg_name} Name')
        sys.exit(1)
    else:
        print(greet(args[0]))


if __name__ == '__main__':
    main()
