#!/usr/local/bin/python
import sys

def fib(term):
    if (term == 0): return 0
    last_two = [0,1]
    for i in range(1,term):
        save = last_two[1]
        last_two[1] = last_two[0] + last_two[1]
        last_two[0] = save

    #print "Golden Ratio = ", float(last_two[1]) / float(last_two[0] + last_two[1])
    return last_two[1]

if __name__ == "__main__":
    print fib(int(sys.argv[1]))
