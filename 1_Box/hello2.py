#!/usr/bin/env python3

import sys

args = sys.argv[1:]
print(sys.argv)
if args:
    name = args[0]
    print(f'Hello, {name}')
else:
    print('Hello World')
