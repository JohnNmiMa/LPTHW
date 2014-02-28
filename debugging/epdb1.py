#!/usr/local/bin/python
# epdb1.py -- experiment with the Python debugger, pdb
import pdb

def combine(s1,s2):      # define subroutine combine, which...
    s3 = s1 + s2 + s1    # sandwiches s2 between copies of s1, ...
    s3 = '"' + s3 +'"'   # encloses it in double quotes,...
    return s3            # and returns it.

a = "aaa"
b = "bbb"
c = "ccc"
pdb.set_trace()
try:
    assert a != b, "a must not be the same as b"
except AssertionError:
    print "a must not be equal to b"
final = combine(a,b)
print final
