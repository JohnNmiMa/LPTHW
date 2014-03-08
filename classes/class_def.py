class ClassDef:
    ''' ClassDef docstring '''
    count = 0
    def __init__(self):
        ClassDef.count += 1

    def explainClassVariables(self):
        print '''*** A class variable is accessed through a class object.
The class variable has the same value in all class instances.
'''

    def explainInstanceFunctions(self):
        print '''*** In a class definiton, all functions are assumed to operate on
*** an instance, which is always passes as the first parameter \'self\'.
*** These are instance functions.
'''

    @staticmethod
    def explainStaticFunctions():
        print '''*** A \'static method\' is an ordinary function that just happens
*** to live in the namespace defined by a class. It does not operate
*** on any kind of instance, and is defined by using the @staticmethod decorator.
'''

    @classmethod
    def explainClassFunctions(cls):
        print '''*** \'Class methods\' are methods that operate on the class
*** itself as an object. Defined using the @classmethod decorator, a class
*** method is different than an instance method in the the class is passed
*** as the first argument witch is named \'cls\' by convention.
'''

    @staticmethod
    def explainProperties():
        print '''*** Normally when you get an attribute value in an instance
*** or a class, the value that is stored is returned. A \'property\' is a 
*** special kind of attribute that computes its value when accessed, and is
*** defined by using the @property decorator.
'''
    # Properties:
    # Usage: instt.class_id
    @property
    def class_id(self):
        return id(ClassDef)
    @property # Usage: inst.instance_id
    def instance_id(self):
        return id(self)
