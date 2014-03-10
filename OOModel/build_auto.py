#!/usr/local/bin/python
import sys
from optparse import OptionParser
import automobile
import sportscar

def parse_options():
    parser = OptionParser()
    parser.add_option("-t", "--type", dest="type", help="Type of automobile to build: 'car','sports'")
    parser.add_option("-m", "--mode", dest="mode", help="Build automobile in: 'parallel' or 'serial'")
    (options,args) = parser.parse_args()
    if (not options.type):
        parser.error("You need to supply a type of automobile to build: --type")
    if (not options.mode):
        parser.error("You need to if the automobild is built in \'parallel\' or \'serial\': --mode")
    return dict(type=options.type, mode=options.mode)

options = parse_options()
mode = options['mode'].lower()
if options['type'].lower() == 'sports'.lower():
    auto = sportscar.SportsCar(mode)
else:
    auto = automobile.Automobile(mode)

auto.build()

