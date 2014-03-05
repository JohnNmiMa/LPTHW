#!/usr/local/bin/python

# This is a decorator that takes a funciton as an argument and returns
# a replacement function.
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

def hypot(a,b,*extra):
    return (a**2 + b**2)**0.5


@log_n_check  # the @ decorator symbol - will wrap the next function - cool!
def hypot_with_at_wrapper(a,b,*extra):
    hypot(a,b)


if __name__ == "__main__":
    print hypot(3,4)

    # Decoration method 1
    decorator = log_n_check(hypot)
    print decorator(3, 4)
    print decorator('3', '4')

    # Same thing, but decorate the original hypot function with a decorator
    # using the same name. Keeps namespace clean.
    hypot = log_n_check(hypot)
    hypot(3, 4)
    hypot('3', '4')
    hypot('three', 'four')

    # Decoration method 2: use @ symbol
    # This is the same thing as:
    #   hwaw = log_n_check(hypot_with_at_wrapper)
    #   hwaw(9,12)
    print hypot_with_at_wrapper(9,12)
