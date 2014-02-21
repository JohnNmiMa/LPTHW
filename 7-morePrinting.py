# -*- coding: utf-8 -*-
# print out three stings, one of them with a variable
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."

# print out 10 dots
print "." *10 # what'd that do?

# Create 12 variable, each of them a string with a single character
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# whatch that comma at the end. try removing it to see what happens
# print out each of the characters to form the work Cheese Burger
# NOTE: there is no space between the strings when they are concatenated.
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

print "NOTE: *10 caused the string '.' to be repeated 10 times"
print "Hi "*5

print "NOTE: the comma at the end of the print statement kept a line return from being printed"
print "But, the string on the next line will be printed after a space is inserted after the first string"

print "Hi there 3 times - " * 3 + ":",
print "How are you?"
