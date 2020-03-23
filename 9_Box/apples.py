#!/usr/bin/env python3

import argparse
import os
# 考点：
# 命令行读取string或文件
# 命令行读取多参数
# choices参数来限制命令行输入参数


# --------------------------------------------------
def get_args():
    """ get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file'
                        )

    # use argument [choices] indicates the allowable values for the argument
    parser.add_argument('-v',
                        '--vowel',
                        metavar='str',
                        type=str,
                        help='The vowel to substitute (default: a)',
                        default='a',
                        choices=list(('aeiou')),
                        )

    args = parser.parse_args()

    # checking whether it is a file
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args


# --------------------------------------------------
def main():
    args = get_args()

    text = args.text
    vowel = args.vowel
    result = ''

    for char in text:
        if char in 'aeiou':
            char = vowel
        elif char in 'AEIOU':
            char = vowel.upper()
        result += char

    print(result)


# --------------------------------------------------
if __name__ == '__main__':
    main()


