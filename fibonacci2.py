#!/usr/local/bin/python
""" Uses pure recursion - is simple, but is quite slow """
import sys

def fib(term):
    if term == 0 or term == 1: return term
    return fib(term-2) + fib(term-1)

if __name__ == "__main__":
    print fib(int(sys.argv[1]))

