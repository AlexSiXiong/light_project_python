#!/usr/bin/env python3

import sys


def greet(name):
    return f'Hola {name}'


def test_greet():
    assert greet('World') == 'Hola World'
    assert greet('Jone Jack') == 'Hola Jone Jack'


def main():
    args = sys.argv[1:]
    name = args[0] if args else 'World'
    print(greet(name))


if __name__ == '__main__':
    main()