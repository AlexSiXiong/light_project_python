#!/usr/bin/env python3

import argparse
import random
# 考点：
# 随即种子，seed用法
# Formatting a string
# 操作String：split and join
# 约束命令行参数

adjectives = 'bankrupt base caterwauling corrupt cullionly detestable dishonest false filthsome filthy foolish foul gross heedless indistinguishable infected insatiate irksome lascivious lecherous loathsome lubbery old peevish rascaly rotten ruinous scurilous scurvy slanderous sodden-witted thin-faced toad-spotted unmannered vile wall-eyed'
adjectives = adjectives.split()

nouns = 'Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool gull harpy jack jolthead knave liar lunatic maw milksop minion ratcatcher recreant rogue scold slave swine traitor varlet villain worm'
nouns = nouns.split()


# --------------------------------------------------
def get_args():
    """
    This program called abuse.py that will insult the user
    by randomly selecting adjectives and nouns to create slanderous epithets.
    """
    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('-a',
                        '--adjectives',
                        metavar='int',
                        type=int,
                        default=2,
                        help='Number of adjectives',
                        )

    parser.add_argument('-n',
                        '--number',
                        metavar='int',
                        type=int,
                        default=3,
                        help='Number of adjectives',
                        )

    parser.add_argument('-s',
                        '--seed',
                        metavar='int',
                        type=int,
                        help='Random seed',
                        default=None,
                        )

    args = parser.parse_args()

    # Check the arguments before outputting.
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')
    return args


# --------------------------------------------------
def main():
    """ Entrance """
    args = get_args()
    num_adj = args.adjectives
    times = args.number

    # This is how to use random seed.
    random.seed(args.seed)

    for i in range(times):
        adj_list = random.sample(adjectives, num_adj)
        print(f'You {", ".join(adj_list)} {random.choice(nouns)}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()