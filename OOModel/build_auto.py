#!/usr/local/bin/python
import sys
import time
from optparse import OptionParser
import automobile
import sportscar

def parse_options():
    parser = OptionParser()
    parser.add_option("-t", "--type", dest="type", default='car', help="Type of automobile to build: 'car','sportscar'")
    parser.add_option("-m", "--mode", dest="mode", default='serial', help="Build automobile in: 'parallel' or 'serial'")
    parser.add_option("-r", "--rate", dest="rate", default='100', help="Build automobile X times faster: 'rate'")
    (options,args) = parser.parse_args()
    """
    if (not options.type):
        parser.error("You need to supply a type of automobile to build: --type")
    if (not options.mode):
        parser.error("You need to if the automobild is built in \'parallel\' or \'serial\': --mode")
    """
    return dict(type=options.type, mode=options.mode, rate=options.rate)

options = parse_options()
mode = options['mode'].lower()
rate = float(options['rate'])

start_time = time.time()
if options['type'].lower() == 'sportscar'.lower():
    auto = sportscar.SportsCar(mode, rate)
elif options['type'].lower() == 'car'.lower():
    auto = automobile.Automobile(mode, rate)
else:
    sys.exit("Can't build unknown car type {!r}".format(options['type']))

auto.build()

end_time = (time.time() - start_time) * rate / 60.0
print "\n*** Time to build the automobile is {:.1f} hours ***".format(end_time)

