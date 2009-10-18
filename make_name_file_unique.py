#!/usr/bin/python

import sys

def uniquify(filename):
    for name in set([x.strip() for x in open(filename).readlines()]):
	print name

if __name__ == '__main__':
    uniquify(sys.argv[1])
