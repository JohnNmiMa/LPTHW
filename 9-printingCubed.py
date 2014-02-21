# -*- coding: utf-8 -*-
days = "Mon The Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApy\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months:", months
print "Here are the months with the %%s formatter: %s" % months
print "Here are the months with the %%r formatter: %r" % months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

print '.'*10
print "String one,", "String two,", "String three"
print "String one," + "String two," + "String three"

print "NOTE: the %r operator will print just as the string was written. All formatting operators will be ignored"
note1 = "NOTE: Concatenating or using a %s formatter will 'glue' strings"
note2 = " together without any 'space' characters separating the strings."
print note1 + note2
print "      The comma operator when printing strings just prints out",
print "one string after another, each separated by a space."
print """      And the tripple quote operator will allow mulitple lines of
text to be printed just as typed in the code, with line-returns
and line lengths output just as shown in the code. """
