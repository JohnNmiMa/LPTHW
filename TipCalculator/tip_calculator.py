#! /usr/local/bin/python
meal = float(raw_input("Enter cost of meal: "))
tax = float(raw_input("Enter tax rate: "))
tip = float(raw_input("Enter your tip rate: "))

tax_value = meal * (tax / 100.0)
meal_with_tax = meal +  tax_value
tip_value = meal_with_tax * (tip / 100.0)

total = meal_with_tax + tip_value

print "The cost of the meal is $%.2f" % meal
print "The tax on the meal is $%.2f" % tax_value
print "The tip on the meal is $%.2f" % tip_value
print "The total bill for the meal is $%.2f" % total
