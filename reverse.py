#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]', description='Reverse anything')
parser.add_argument('input', help='string to be reversed. Use quotes for spaces.')

args = parser.parse_args()
print(args.input[::-1])
