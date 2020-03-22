#!/usr/bin/env python3
""" howler """

import argparse
import os


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('message',
                        metavar='str',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        help='Output filename',
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    args = get_args()
    message = args.message
    outfile = args.outfile
    if len(outfile) == 0:
        print(message.upper())
    else:
        if not os.path.isfile(message):
            out_fh = open(outfile, 'wt')
            out_fh.write(message.upper())
            out_fh.close()
        else:
            fh = open(message)
            out_fh = open(outfile, 'wt')
            out_fh.write(fh.read().upper())
            out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()



