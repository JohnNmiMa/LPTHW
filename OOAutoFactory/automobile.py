""" Provides a class Automobile that can be used to build a generic automobile """
from threading import Thread, Event
from functools import wraps
import time


def set_state(func):
    ''' A decorator for each build stage method to set the state progress '''
    @wraps(func)
    def build_wrapper(self):
        """ Used to:
            1) Set the build stage flag before the work begins.
            2) Trigger the stage event to let other dependent threads
               know that the state is complete.
            3) Set the build stage flag after the work is complete.
        """
        if func.__name__ == 'build_engine':
            start_state = "building engine"
            end_state = "engine built"
            event = self.built_engine_event
        elif func.__name__ == 'build_transmission':
            start_state = "building transmission"
            end_state = "transmission built"
            event = self.built_transmission_event
        elif func.__name__ == 'build_frame':
            start_state = "building frame"
            end_state = "frame built"
            event = self.built_frame_event
        elif func.__name__ == 'build_chassis_part1':
            start_state = "building first part of chassis"
            end_state = "chassis part 1 built"
            event = self.built_chassis_part1_event
        elif func.__name__ == 'build_chassis_part2':
            start_state = "building second part of chassis"
            end_state = "chassis part 2 built"
            event = self.built_chassis_part2_event
        elif func.__name__ == 'build_chassis_part3':
            start_state = "building third part of chassis"
            end_state = "chassis part 3 built" 
            event = self.built_chassis_part3_event
        elif func.__name__ == 'post_chassis_assembly':
            start_state = "performing post chassis assembly"
            end_state = "post chassis assembly complete"
            event = self.post_chassis_assembled_event
        elif func.__name__ == 'add_fluids':
            start_state = "adding fluids"
            end_state = "fluids added"
            event = self.fluids_added_event
        elif func.__name__ == 'test_drive':
            start_state = "testing automobile"
            end_state = "Beep Beep"
            event = self.test_drive_complete_event

        self.state = start_state # Set the start state before building starts
        func(self)               # Build part of the automobile
        self.state = end_state   # Set the end state after building is finished
        event.set()

    return build_wrapper


class Automobile(object):
    ''' Used to build a generic automobile 
        Usage: 1) instantiate an Automobile object
               2) call 'build()' on the object
    '''

    def __init__(self, mode, rate):
        self.mode = mode
        self.rate = rate
        self.state = "not started"
        self.type = "generic automobile"

        # Create synchronization events
        self.built_engine_event = Event()
        self.built_transmission_event = Event()
        self.built_frame_event = Event()
        self.built_chassis_part1_event = Event()
        self.built_chassis_part2_event = Event()
        self.built_chassis_part3_event = Event()
        self.post_chassis_assembled_event = Event()
        self.fluids_added_event = Event()
        self.test_drive_complete_event = Event()
        self.interior_assembled_event = Event()
        self.exterior_ligiting_installed_event = Event()
        self.wheel_assembly_installed_event = Event()

    def build(self):
        ''' The main method used to start building the automobile '''
        start_msg = '*** Start building a {} in {}: build rate = {:.0f}x ***'\
                     .format(self.type, self.mode, self.rate)
        print '*' * (len(start_msg))
        print start_msg
        print '*' * (len(start_msg))

        if self.mode == 'parallel':
            self._build_parallel()
        else:
            self._build_serial()
        
        print "*** Finished building the automobile ***"

    def _build_serial(self):
        ''' A template method used to build automobiles in serial order '''

        self.build_engine()
        self.build_transmission()
        self.build_frame()
        self.build_chassis_part1()
        self.build_chassis_part2()
        self.build_chassis_part3()
        self.post_chassis_assembly()
        self.add_fluids()
        self.test_drive()

    def _build_parallel(self):
        ''' A template method used to build automobiles in parallel.
            Kick off a bunch of threads, and use events to synchronize the
            order in which the car is built.
        '''

        # Create threads
        be_thread = Thread(target=self.build_engine)
        bt_thread = Thread(target=self.build_transmission)
        bf_thread = Thread(target=self.build_frame)
        bc1_thread = Thread(target=self.build_chassis_part1)
        bc2_thread = Thread(target=self.build_chassis_part2)
        bc3_thread = Thread(target=self.build_chassis_part3)
        pca_thread = Thread(target=self.post_chassis_assembly)
        af_thread = Thread(target=self.add_fluids)
        td_thread = Thread(target=self.test_drive)

        # Start all threads - start building the auto
        be_thread.start()
        bt_thread.start()
        bf_thread.start()
        bc1_thread.start()
        bc2_thread.start()
        bc3_thread.start()
        pca_thread.start()
        af_thread.start()
        td_thread.start()

        # Wait for all threads to finish
        be_thread.join()
        bt_thread.join()
        bf_thread.join()
        bc1_thread.join()
        bc2_thread.join()
        bc3_thread.join()
        pca_thread.join()
        af_thread.join()
        td_thread.join()

    def _build_time(self, hours):
        ''' Convience method to convert the hours used to build a phase of
            the auto into seconds. Also, if there is a speedup rate, apply
            it to the time, so the build will go faster. This is used to
            simulate a full build without having to wait the actual amount
            of time specified.
        '''
        time.sleep(hours * 60.0 / self.rate)

    def build_state(self):
        ''' Used to query what stage the automobile is being built. This will
            not have a precise meaning if the car is being built in parallel.
        '''
        return self.state

    @set_state
    def build_engine(self):
        print "*** Start building engine ***"; self._build_time(4)
        print "    Casting engine block"
        print "    Boring and stroking the engine block"
        print "    Installing pistons, crank, valves, seals"
        print "    Installing timing belt"
        print "    Installing carburetor"
        print "    Installing distributor, sparkwires, sparkplugs, coil"
        print "    Installing belts"

    @set_state
    def build_transmission(self):
        print "*** Start building transmission ***"; self._build_time(6)
        print "    Building automatic transmission"

    @set_state
    def build_frame(self):
        print "*** Start frame assembly ***"; self._build_time(2)
        print "    Building frame"

    @set_state
    def build_chassis_part1(self):
        # Wait for the frame to be built
        self.built_frame_event.wait()
        print "*** Start assembling the first part of the chassis ***"; self._build_time(.5)
        print "    Installing brake lining"
        print "    Installing fuel lining"
        print "    Installing firewall"
        print "    Installing wheel hub assymbly"

    @set_state
    def build_chassis_part2(self):
        # Wait for both the engine and first part of chassis to be built
        self.built_engine_event.wait() 
        self.built_chassis_part1_event.wait()
        print "*** Start assembling the second part of the chassis ***"; self._build_time(0.2)
        print "    Installing engine"

    @set_state
    def build_chassis_part3(self):
        # Wait for both the transmission and second part of chassis to be built
        self.built_transmission_event.wait()
        self.built_chassis_part2_event.wait()
        print "*** Start assembling the third part of the chassis ***"; self._build_time(3.4)
        print "    Installing automatic transmission"
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

    @set_state
    def post_chassis_assembly(self):
        self.built_chassis_part3_event.wait()
        print "*** Start post chassis assembly ***"; self._build_time(2)
        print "    Installing wiring harness"
        print "    Installing cooling system"
        print "    Installing body panels"
        print "    Paint body"
        print "    Installing clutch and transmission"

        if self.mode == 'parallel':
            # All three subassemblies can be done in parallel
            ai_thread = Thread(target=self.assemble_interior)
            iel_thread = Thread(target=self.install_exterior_lighting)
            iwa_thread = Thread(target=self.install_wheel_assembly)

            ai_thread.start()
            iel_thread.start()
            iwa_thread.start()

            ai_thread.join()
            iel_thread.join()
            iwa_thread.join()
        else:
            self.assemble_interior()
            self.install_exterior_lighting
            self.install_wheel_assembly

        print "    Installing doors"
        print "    Installing windshield and wipers"

    def assemble_interior(self):
        print "*   Assembling Interior"; self._build_time(2.5)
        print "    Installing dashboard"
        print "    Installing sound system"
        print "    Installing instruments"
        print "    Installing surface coverings"
        print "    Installing carpeting"
        print "    Installling Steering wheel and control assemblies"
        print "    Installing seating"
        print "    Testing interior lighting"

    def install_exterior_lighting(self):
        print "*   Installing Exterior Lighting *"; self._build_time(.33)
        print "    Installing headlamp assembly"
        print "    Installing tail light assembly"
        print "    Installing side marker lights"
        print "    Installing fog lamps"
        print "    Installing parking lights"
        print "    Installing turn signal lights"

    def install_wheel_assembly(self):
        print "*   Installing Wheel Assembly *"; self._build_time(.25)
        print "    Installing tires on wheels"
        print "    Mounting wheels"

    @set_state
    def add_fluids(self):
        self.post_chassis_assembled_event.wait()
        print "*** Start adding fluids ***"; self._build_time(.17)
        print "    Adding engine coolant"
        print "    Adding engine oil"
        print "    Adding transmission oil"
        print "    Adding wiper fluid"
        print "    Adding break fluid"
        print "    Adding differential oil"

    @set_state
    def test_drive(self):
        self.fluids_added_event.wait()
        print "*** Start testing the automobile ***"; self._build_time(1.3)
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

