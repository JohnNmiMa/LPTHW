#! /usr/local/bin/python
import os,sys
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
print os.name
print "System Path = ", sys.path
