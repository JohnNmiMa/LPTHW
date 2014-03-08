from threading import Thread, Event

# A decorator for each build method to set the state progress
def set_state(func):
    def inner(self):
        if func.__name__ == 'build_engine':
            start_state = "building engine"; end_state = "engine built"
        elif func.__name__ == 'build_transmission':
            start_state = "building transmission"; end_state = "transmission built"
        elif func.__name__ == 'build_frame':
            start_state = "building frame"; end_state = "frame built"
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
        self.built_engine_event = Event()
        self.built_transmission_event = Event()
        self.built_frame_event = Event()
        self.built_chassis_event = Event()
        self.post_chassis_assembled_event = Event()
        self.fluids_added_event = Event()
        self.test_drive_complete_event = Event()
        self.interior_assembled_event = Event()
        self.exterior_ligiting_installed_event = Event()
        self.wheel_assembly_installed_event = Event()

    def build_state(self):
        return self.state

    def build(self):
        print """
*******************************************
*** Start building a {} ***
*******************************************
        """.format(self.type)
        # A template method used to build automobiles
        #self.build_engine()
        be_thread = Thread(target=self.build_engine)
        be_thread.start()

        #self.build_transmission()
        bt_thread = Thread(target=self.build_transmission)
        bt_thread.start()

        #self.build_frame()
        bf_thread = Thread(target=self.build_frame)
        bf_thread.start()

        #self.build_chassis()
        bc_thread = Thread(target=self.build_chassis)
        bc_thread.start()
        
        #self.post_chassis_assembly()
        pca_thread = Thread(target=self.post_chassis_assembly)
        pca_thread.start()
        
        #self.add_fluids()
        af_thread = Thread(target=self.add_fluids)
        af_thread.start()
        
        #self.test_drive()
        td_thread = Thread(target=self.test_drive)
        td_thread.start()

        be_thread.join()
        bt_thread.join()
        bf_thread.join()
        bc_thread.join()
        pca_thread.join()
        af_thread.join()
        td_thread.join()
        
        print "*** Finished building the automobile ***"

    @set_state
    def build_engine(self):
        print "*** Start building engine ***"
        print "    Casting engine block"
        print "    Boring and stroking the engine block"
        print "    Installing pistons, crank, valves, seals"
        print "    Installing timing belt"
        print "    Installing carburetor"
        print "    Installing distributor, sparkwires, sparkplugs, coil"
        print "    Installing belts"
        self.built_engine_event.set() # let others know the engine is built

    @set_state
    def build_transmission(self):
        print "*** Start building transmission ***"
        self.built_transmission_event.set()

    @set_state
    def build_frame(self):
        print "*** Start frame assembly ***"
        print "    Frame build: Building frame"
        self.built_frame_event.set()

    @set_state
    def build_chassis(self):
        print "*** Start assembling the chassis ***"
        self.built_frame_event.wait()
        print "    Installing brake lining"
        print "    Installing fuel lining"
        print "    Installing firewall"
        print "    Installing wheel hub assymbly"
        self.built_engine_event.wait()
        print "    Installing engine"
        self.built_transmission_event.wait()
        print "    Installing clutch and transmission"
        print "    Installing driveshaft"
        print "    Installing differential"
        print "    Installing suspension"
        print "    Installing exhaust system"
        print "    Installing stearing assembly"
        print "    Installing gas tank and fuel pump"
        print "    Installing drive axles"
        print "    Installing brake system"
        print "    Installing CV joints"
        print "    Applying chassis undercoating"
        self.built_chassis_event.set() # let others know the chassis is built

    @set_state
    def post_chassis_assembly(self):
        self.built_chassis_event.wait()
        print "*** Start post chassis assembly ***"
        print "    Installing wiring harness"
        print "    Installing cooling system"
        print "    Installing body panels"
        print "    Paint body"
        print "    Installing clutch and transmission"

        # All three subassemblies can be done in parallel
        #self.assemble_interior()
        ai_thread = Thread(target=self.assemble_interior)
        ai_thread.start()

        #self.install_exterior_lighting()
        iel_thread = Thread(target=self.install_exterior_lighting)
        iel_thread.start()

        #self.install_wheel_assembly()
        iwa_thread = Thread(target=self.install_wheel_assembly)
        iwa_thread.start()

        ai_thread.join()
        iel_thread.join()
        iwa_thread.join()

        print "    Installing doors"
        print "    Installing windshield and wipers"
        self.post_chassis_assembled_event.set() # let others know the post chassis assy is done

    def assemble_interior(self):
        print "*   Assembling Interior"
        print "    Installing dashboard"
        print "    Installing sound system"
        print "    Installing instruments"
        print "    Installing surface coverings"
        print "    Installing carpeting"
        print "    Installling Steering wheel and control assemblies"
        print "    Installing seating"
        print "    Testing interior lighting"

    def install_exterior_lighting(self):
        print "*   Installing Exterior Lighting *"
        print "    Installing headlamp assembly"
        print "    Installing tail light assembly"
        print "    Installing side marker lights"
        print "    Installing fog lamps"
        print "    Installing parking lights"
        print "    Installing turn signal lights"

    def install_wheel_assembly(self):
        print "*   Installing Wheel Assembly *"
        print "    Installing tires on wheels"
        print "    Mounting wheels"

    @set_state
    def add_fluids(self):
        self.post_chassis_assembled_event.wait()
        print "*** Start adding fluids ***"
        print "    Adding engine coolant"
        print "    Adding engine oil"
        print "    Adding transmission oil"
        print "    Adding wiper fluid"
        print "    Adding break fluid"
        print "    Adding differential oil"
        self.fluids_added_event.set() # let others know the fluids are added

    @set_state
    def test_drive(self):
        self.fluids_added_event.wait()
        print "*** Start testing the automobile ***"
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
        self.test_drive_complete_event.set() # let others know the test drive is done

