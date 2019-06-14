#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Tyler Ward"


import sys
import argparse
import os


def to_lower(text):
    return text.lower()


def to_upper(text):
    return text.upper()


def to_title(text):
    return text.title()


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(description='Perform transformation on input text.')
    parser.add_argument('text',
                    help='text to be manipulated')

    # exc_group = parser.add_mutually_exclusive_group()

    parser.add_argument('-u', '--upper',
        help='convert text to uppercase',
        action='store_true')
    parser.add_argument('-l', '--lower',
        help='convert text to lowercase',
        action='store_true')
    parser.add_argument('-t', '--title',
        help='convert text to titlecase',
        action='store_true')

    return parser


def main():
    """Implementation of echo"""
    args = create_parser().parse_args()

    if not args.text:
        print('Please specify something to be echoed.')
        return

    text = args.text

    if args.upper:
        text = to_upper(text)
    if args.lower:
        text = to_lower(text)
    if args.title:
        text = to_title(text)

    print(text)


if __name__ == '__main__':
    main()