class Calculator(object):
 
    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x+y
        else:
            raise ValueError

if __name__ == "__main__":
    cal = Calculator()
    print "Add 40 and 50 = ", cal.add(40, 50)

