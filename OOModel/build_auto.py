#!/usr/local/bin/python
import sys
from optparse import OptionParser
import automobile
import sportscar

def parse_options():
    parser = OptionParser()
    parser.add_option("-t", "--type", dest="type", help="Type of automobile to build")
    (options,args) = parser.parse_args()
    if (not options.type):
        parser.error("You need to supply a type of automobile to build: --type")
    return dict(type=options.type)

options = parse_options()
if options['type'].upper() == 'sports'.upper():
    auto = sportscar.SportsCar()
else:
    auto = automobile.Automobile()

auto.build()

