#! /usr/bin/python

from sentence import *

def main():
    s = sentence('sample.txt')
    print(s.width())
    print(s.height())
    for l in s.getLines():
        print(l)

main()
