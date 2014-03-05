#!/usr/local/bin/python

my_number = 10
my_list = [10,11,13]

def change(a_number, a_list):
  print "In change, before change, a_number = {}, a_number id = {}".format(a_number, id(a_number))
  print "In change, before change, a_list = {}, a_list id = {}".format(a_list, id(a_list))

  a_number = 3
  a_list[2] = 12
  
  print "In change, after change, a_number = {}, a_number id = {}".format(a_number, id(a_number))
  print "In change, after change, a_list = {}, a_list id = {}".format(a_list, id(a_list))
  # a_number is a new local variable, and does not change my_number


print "my_number={}, my_list={}, my_number id={}, my_list id = {}".format(my_number,my_list,id(my_number),id(my_list))

change(my_number,my_list)

print "my_number={}, my_list={}, my_number id={}, my_list id = {}".format(my_number,my_list,id(my_number),id(my_list))
