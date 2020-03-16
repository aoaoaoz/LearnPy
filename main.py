# -*- coding: utf-8 -*-

' a test module '
__author__ = 'aoaoao'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('square', type=int, 
    help='diplay a aquare of a given number')
parser.add_argument('-v', '--verbose', action='store_true', 
    help = 'increase output verbosity')
args = parser.parse_args()
answer = args.square ** 2
if args.verbose:
    print('the square of %s equals %s' % (args.square, answer) )