#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Tyler Ward"


import sys
import argparse
import os

def echo(target):
    print(target)
    return target


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(description='Process echo command.')
    parser.add_argument('target',
                    help='an item to be echoed')

    return parser.parse_args()


def main():
    """Implementation of echo"""
    args = create_parser()

    if not args.target:
        print('Please specify something to be echoed.')
        return

    print(echo(args.target))


if __name__ == '__main__':
    main()
