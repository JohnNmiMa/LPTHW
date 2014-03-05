#!/usr/local/bin/python
""" Uses recursion, but saves previous answers away for future use """
import sys

fibs = [0,1]
def fib(term):
    global fibs
    if term == 0 or term == 1: return fibs[term]
    if len(fibs) > term-2:
        fibm2 = fibs[term-2]
    else:
        fibm2 = fib(term-2)
    if len(fibs) > term-1:
        fibm1 = fibs[term-1]
    else:
        fibm1 = fib(term-1)

    fibs.append(fibm2 + fibm1)
    return fibs[term]

if __name__ == "__main__":
    print fib(int(sys.argv[1]))

