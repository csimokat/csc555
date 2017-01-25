#!/usr/bin/env python

import sys

filename = "myfile.txt"

with open(filename) as f:
        for line in f:
                words = line.split(' ')
                for word in words:
                        print '%s\t%s' % (word, 1)