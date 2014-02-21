# -*- coding: utf-8 -*-
# Create a string that is used to format the printing output
formatter = "%r %r %r %r"

# Just print out the numbers one through four. A space will be inserted
# between each number, just as the formatter specified.
print formatter % (1,2,3,4)
# Just print out the numbers as spelled
print formatter % ("one", "two", "three", "four")
# Just print out the booleans
print formatter % (True, False, False, True)
# Just print out the formatter, four times, as specified in the formatter
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
print '.'*10
formatter2 = "%s %s %s %s"
print formatter2 % (formatter, formatter, formatter, formatter)
print """
NOTE: this printed out the %r four times, but with the
%%s formatter. Notice that quotes around the formatter are gone
""" % formatter
