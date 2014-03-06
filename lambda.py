#!/usr/local/bin/python

"""
Python has two tools for building functions: def and lambda.
* lambdas can take only a single expression (a Python expression returns a value)
  therefore, if it doesn't return a value, it isn't an expression and can't
  be put into a lamda.
* Assignment statements cannot be used in lambda.
* Simple operations (math, string, list comps,etc) are ok in lambda
* Function call are expressions, so are ok in lambda
* Print can be used in a lambda
* Even funcitons that return None can be used in a lambda
* Conditional expressions can be used in a lambda
"""


# This is a decorator that takes a funciton as an argument and returns
# a replacement (decorator) function.
def log_n_check(func): # pack arguments in variable args (a,b)
    def inner(*args):
        try:
            # Check that each parameter is convertable to a float
            args = [float(args[i]) for i, arg in enumerate(args)]
            result = func(*args)  # *args unpacks the args for the func
            print "Parameters of {} = {}".format(func.__name__, args)
            return result
        except ValueError as ex:
            print "ValueError: " + ex.message

    return inner  # return the decorator function


@log_n_check
def hypot_def(a,b):
    return (a**2 + b**2)**0.5

# @log_n_check  - can't wrap lambda with the 2 symbol
hypot_lambda = lambda a,b: (a**2 + b**2)**0.5


if __name__ == "__main__":
    hypot_lambda = log_n_check(hypot_lambda) # wrap the lambda
    print hypot_lambda(3, 4)
    print hypot_def(3, 4)
