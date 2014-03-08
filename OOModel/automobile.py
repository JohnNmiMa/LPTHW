# A decorator for each build method to set the state progress
def set_state(func):
    def inner(self):
        if func.__name__ == 'build_engine':
            start_state = "building engine"; end_state = "engine built"
        elif func.__name__ == 'build_chassis':
            start_state = "building chassis"; end_state = "chassis built"
        elif func.__name__ == 'post_chassis_assembly':
            start_state = "performing post chassis assembly";
            end_state = "post chassis assembly complete"
        elif func.__name__ == 'add_fluids':
            start_state = "adding fluids"; end_state = "fluids added"
        elif func.__name__ == 'test_drive':
            start_state = "testing automobile"; end_state = "Beep Beep"
        self.state = start_state; # Set the start state before building starts
        #print "Wrapping {}".format(func.__name__)
        func(self)                # Build part of the automobile
        self.state = end_state;   # Set the end state after building is finished
    return inner

class Automobile(object):
    type = "generic automobile"

    def __init__(self):
        self.state = "not started"
        self.type = "generic automobile"

    def build_state(self):
        return self.state

    def build(self):
        print """
*******************************************
*** Start building a {} ***
*******************************************
        """.format(self.type)
        # A template method used to build automobiles
        print "*** Start building the engine ***"
        self.build_engine()

        print "*** Start assembling the chassis ***"
        self.build_chassis()
        
        print "*** Start post chassis assembly ***"
        self.post_chassis_assembly()
        
        print "*** Start adding fluids ***"
        self.add_fluids()
        
        print "*** Start testing the automobile ***"
        self.test_drive()
        
        print "*** Finished building the automobile ***"

    @set_state
    def build_engine(self):
        print "    Casting engine block"
        print "    Boring and stroking the engine block"
        print "    Installing pistons, crank, valves, seals"
        print "    Installing timing belt"
        print "    Installing carburetor"
        print "    Installing distributor, sparkwires, sparkplugs, coil"
        print "    Installing belts"

    def build_frame(self):
        print "    Frame build: Building frame"

    @set_state
    def build_chassis(self):
        self.build_frame()
        print "    Installing brake lining"
        print "    Installing fuel lining"
        print "    Installing firewall"
        print "    Installing engine"
        print "    Installing clutch and transmission"
        print "    Installing driveshaft"
        print "    Installing differential"
        print "    Installing suspension"
        print "    Installing exhaust system"
        print "    Installing stearing assembly"
        print "    Installing gas tank and fuel pump"
        print "    Installing drive axles"
        print "    Installing wheel hub assymbly"
        print "    Installing brake system"
        print "    Installing CV joints"
        print "    Applying chassis undercoating"

    @set_state
    def post_chassis_assembly(self):
        print "    Installing wiring harness"
        print "    Installing cooling system"
        print "    Installing body panels"
        print "    Paint body"
        print "    Installing clutch and transmission"
        print "    Assembling Interior"
        interior = self.assemble_interior()
        print "    Installing doors"
        print "    Installling exterior lighting assemblies"
        interior = self.install_exterior_lighting()
        print "    Installing wheels assembly"
        interior = self.install_wheel_assembly()
        print "    Installing windshield and wipers"

    def assemble_interior(self):
        print "    Installing dashboard"
        print "    Installing sound system"
        print "    Installing instruments"
        print "    Installing surface coverings"
        print "    Installing carpeting"
        print "    Installling Steering wheel and control assemblies"
        print "    Installing seating"
        print "    Testing interior lighting"

    def install_exterior_lighting(self):
        print "    Installing headlamp assembly"
        print "    Installing tail light assembly"
        print "    Installing side marker lights"
        print "    Installing fog lamps"
        print "    Installing parking lights"
        print "    Installing turn signal lights"

    def install_wheel_assembly(self):
        print "    Installing tires on wheels"
        print "    Mounting wheels"

    @set_state
    def add_fluids(self):
        print "    Adding engine coolant"
        print "    Adding engine oil"
        print "    Adding transmission oil"
        print "    Adding wiper fluid"
        print "    Adding break fluid"
        print "    Adding differential oil"

    @set_state
    def test_drive(self):
        print "    Testing acceleration"
        print "    Testing cornering"
        print "    Testing breaking"
        print "    Testing under heavy load"
        print "    Testing on wet roads"
        print "    Testing at altitude"
        print "    Testing at extreme temperatures"
        print "    Testing on track"
        print "    Testing off road"
        print "    Testing in city"

