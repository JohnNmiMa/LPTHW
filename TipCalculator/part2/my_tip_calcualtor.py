#!/usr/local/bin/python
import sys
from optparse import OptionParser
 
def calculate_rate(base, percentage):
    return base * percentage
    #return float(base) * float(percentage)
 
def calculate_meal_costs(meal_base, tax_rate, tip_rate):
    """
    Calculates dollar amounts for tax, tip, and total meal cost
    """
    tax_value = calculate_rate(meal_base, tax_rate)
    meal_with_tax = tax_value + meal_base
    tip_value = calculate_rate(meal_with_tax, tip_rate)
    total = meal_with_tax + tip_value
    meal_info = dict(meal_base=meal_base,
                    tax_rate=tax_rate,
                    tip_rate=tip_rate,
                    tax_value=tax_value,
                    total = total)
    return meal_info
 
def get_float(item):
    while True:
        try:
            num = float(raw_input("Please enter a number for %s: " % item))
            return num
        except ValueError:
            print "Invalid number - please enter a number for %s " % item
 
def main(argv=sys.argv):
    if len(argv) < 4:
        sys.exit("Please enter three numbers: meal_cost, tax_percent, tip_percent")

    # Use a Dictionary comprehensions to store the meal options
    options = {item: argv[i+1] for i, item in enumerate(['meal', 'tax_percent', 'tip_percent'])}
    for item in options:
        try:
            options[item] = float(options[item])
        except ValueError:
            options[item] = get_float(item)

    meal_info = calculate_meal_costs(options['meal'], options['tax_percent'], options['tip_percent'])
    print "The base cost of your meal was ${0:.2f}.".format(meal_info['meal_base'])
    print "You need to pay ${0:.2f} for tax.".format(meal_info['tax_value'])
    print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
                                        int(100*meal_info['tip_rate']), 
                                        meal_info['tax_value'])
    print "The grand total of your meal is ${0:.2f}.".format(meal_info['total'])
 
if __name__ == '__main__':
    main()

