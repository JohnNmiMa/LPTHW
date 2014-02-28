import sys
 
def subtractor(a, b): # a and b are  parameters or arguments. add is the name of the function.
  """I do something WITH but not TO a and b"""  # this triple quoted text is called a doc string.
                                                # You should provide a short descriptive statement of what
                                                # the function does, if that's not already apparent
                                                # from the title.
  print "I'm a function. My name is {}".format(subtractor.__name__)
  print "I'm about to subtract {0} and {1}\n\n".format(a,b)
  return a - b  # i output a value by using the return statement
 
def print_function(): 
  """ I'm also a function, but I don't take any parameters"""
  print "I'm {}, and I'm printing now\n\n".format(print_function.__name__)
  
def function3(a=1, b=1):  #You can assign default parameter values to me, which will be subbed in
                        # if not parameters are supplied at run time.
  """ I'm a function that calls other functions """
  total = subtractor(a,b)
  print "I'm {} and I'm about to call print_function".format(function3.__name__)
  print_function()
  return total
  
def main(argv=sys.argv):    # By convention, "main" defines a routine to be executed
                            # if this file is run as a stand alone script.
  print "I'm the main function and I'm going to run a few other functions.\n\n"
  a = int(argv[1])
  b = int(argv[2])
  function_as_variable = function3    #You can assign a function to a variable 
  total = function_as_variable(a, b)  # And then you can use this variable like a function
                                      # Remember, though, to assign a function as a variable, 
                                      # you need to leave off the parentheses, or else the function 
                                      # will be called. 
  print ("Hey, it's me, main again. I got the value for total "
        "by calling those other functions. " +
        "The total for {0} minus {1} is {2} by".format(a, b, total)
        )
  
if __name__ == '__main__':  # In other words, if this script gets called from the command line.
  main()                    # w