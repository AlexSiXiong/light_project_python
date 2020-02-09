#!/usr/bin/env python3
"""tests for the family of hello.py """

import os
from subprocess import getstatusoutput, getoutput

prg = './hello_optional_args.py'


# --------------------------------------------------
def test_exist():
    """check if the program exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_default():
    """ Say 'Hello World' by default """

    out = getoutput(prg)
    assert out.strip() == 'Hello World'


# --------------------------------------------------
def test_input():
    """test for input"""

    for val in ['a', 'b']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'{prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello {val}'
