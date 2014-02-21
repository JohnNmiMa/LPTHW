# -*- coding: utf-8 -*-
# cryptic variable with formatting in it. Also the '10' var is part of
# the "x" variable.
x = "There are %d types of people." % 10
# Two strings one is a var with the exact same letters as the string it
# represents.
binary = "binary"
do_not = "don't"
# A string with two formatting characters. Hence the () with the two 
# variables.
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r formatter will print anything
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Adding/concatenating two string together
print w + e
print "-------------"

# The way I would have done it. I can really just put the var as part
# of the string.
z1 = "There are %r types of %s over %d feet tall and older than %f age."
z2 = "There are %r types of %r over %d feet tall and older than %f age."
people = "people"
num = 2
height = 5
age = 35.50
print z1 % (num, people, height, age)
print z2 % (num, people, height, age)
print "NOTE: the word %r has quotes when printed with the %%r formatter" % people
print "NOTE: the %r formatter only prints the quotes for string vars"
print "NOTE: use %r mostly for debugging"
