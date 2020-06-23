#!/usr/bin/env python

from __future__ import print_function

f = open('show_version.txt')
show_version = f.read()

print(show_version)
print(type(show_version))
f.close()

with open('show_version.txt') as f:
    show_version = f.readlines()
    print(show_version)
    print(type(show_version))
