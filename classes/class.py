#!/usr/local/bin/python
class BaseClass:
    ''' A base class named BaseClass '''
    class_var = "class variable in BaseClass"
    bvar = "class variable in BaseClass"
    cvar = "class variable in BaseClass"
    def __init__(self):
        print "* Observing from BaseClass.__init__() *"
        self.cvar = 'instance variable - shadows class variable cvar'
        self.inst_dvar = 'instance variable'
        print "  self.class_var = {!r}: id={}".format(self.class_var, id(self.class_var))
        print "  BaseClass.class_var = {!r}: id={}".format(BaseClass.class_var, id(BaseClass.class_var))
        print "  BaseClass.bvar = {!r}: id={}".format(BaseClass.bvar, id(BaseClass.bvar))
        print "  BaseClass.cvar = {!r}: id={}".format(BaseClass.cvar, id(BaseClass.cvar))
        print "  self.cvar = {!r}: id={}".format(self.cvar, id(self.cvar))
        print "  self.inst_dvar = {!r}: id={}".format(self.inst_dvar, id(self.inst_dvar))
    def afunc(self):
        print "* Observing BaseClass.afunc() *"
        print "  self.{} in BaseClass: id={}".format(self.afunc.__name__,id(self.afunc))
    def bfunc(self):
        print "* Observing BaseClass.bfunc() *"
        print "  self.{} in BaseClass: id={}".format(self.bfunc.__name__,id(self.bfunc))

class SubClass(BaseClass):
    ''' A derived class named SubClass '''
    sub_class_var = "class variable in SubClass"
    bvar = "class variable in SubClass"
    def __init__(self):
        print "* Observing from SubClass.__init__() *"
        BaseClass.__init__(self)
        print "  self.sub_class_var = {!r}: id={}".format(self.sub_class_var, id(self.sub_class_var))
        print "  self.bvar = {!r}: id={}".format(self.bvar, id(self.bvar))
        print "  BaseClass.bvar = {!r}: id={}".format(BaseClass.bvar, id(BaseClass.bvar))
        print "  SubClass.bvar = {!r}: id={}".format(SubClass.bvar, id(SubClass.bvar))
        print "  self.{} from SubClass: id={}".format(self.afunc.__name__,id(self.afunc))
        print "  self.{} from SubClass: id={}".format(self.bfunc.__name__,id(self.bfunc))
    def bfunc(self):
        print "* Observing SubClass.bfunc() *"
        print "  self.{} in SubClass: id={}".format(self.bfunc.__name__,id(self.bfunc))
        
def main():
    print "*** Observe from the base class ***"
    bc = BaseClass()
    bc.afunc()
    bc.bfunc()
    print "* Observing from main() *"
    print "  bc.class_var = {!r}: id={}".format(bc.class_var, id(bc.class_var))
    print "  bc.bvar = {!r}: id={}".format(bc.bvar, id(bc.bvar))
    print "  bc.cvar = {!r}: id={}".format(bc.cvar, id(bc.cvar))
    print "  BaseClass.cvar = {!r}: id={}".format(BaseClass.cvar, id(BaseClass.cvar))
    print "  bc.inst_dvar = {!r}: id={}".format(bc.inst_dvar, id(bc.inst_dvar))
    print "* Listing of BaseClass dictionary *"
    for key in BaseClass.__dict__:
        print '  {} : {}'.format(key, BaseClass.__dict__[key])
    print "* Listing of BaseClass instance (bc) dictionary *"
    for key in bc.__dict__:
        print '  {} : {}'.format(key, bc.__dict__[key])

    print "*** Observe from the derived class ***"
    sc = SubClass()
    sc.afunc()
    sc.bfunc()
    print "  sc.class_var from SubClass = {!r}: id={}".format(sc.class_var, id(sc.class_var))
    print "  sc.class_sub_var from SubClass = {!r}: id={}".format(sc.class_sub_var, id(sc.class_sub_var))
    print "  sc.bvar =   {!r}: id={}".format(sc.bvar, id(sc.bvar))
    print "  sc.cvar =   {!r}: id={}".format(sc.cvar, id(sc.cvar))

    print "Observe from the class object"
    print "  BaseClass.class_var = {!r}: id={}".format(BaseClass.class_var, id(BaseClass.class_var))
    print "  BaseClass.bvar = {!r}: id={}".format(BaseClass.bvar, id(BaseClass.bvar))
    print "  SubClass.class_var =  {!r}: id={}".format(SubClass.class_var, id(SubClass.class_var))
    print "  SubClass.bvar =  {!r}: id={}".format(SubClass.bvar, id(SubClass.bvar))


if __name__ == "__main__":
    main()
