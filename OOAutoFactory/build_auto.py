#!/usr/local/bin/python
""" Used to build automobiles 
    $ build_auto.py
      Will build a generic automobile in serial, 1000 times faster than normal

    $ build_auto.py -t sportscar -m parallel -r 2000
      Will build a sports car where some of the stages are done in parallel,
      2000 times faster than normal.
"""
import sys
import time
from optparse import OptionParser

import automobile
import sportscar


def parse_options():
    parser = OptionParser()
    parser.add_option("-t", "--type", dest="type", default='car',\
                      help="Type of automobile to build: 'car','sportscar'")
    parser.add_option("-m", "--mode", dest="mode", default='serial',\
                      help="Build automobile in: 'parallel' or 'serial'")
    parser.add_option("-r", "--rate", dest="rate", default='1000',\
                      help="Build automobile X times faster: 'rate'")
    (options,args) = parser.parse_args()

    return dict(type=options.type, mode=options.mode, rate=options.rate)


def main():
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
    print "\n*** Time to build the automobile is {:.1f} hours ***".\
           format(end_time)

if __name__ == "__main__":
    main()
