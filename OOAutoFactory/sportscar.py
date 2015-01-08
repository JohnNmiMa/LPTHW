""" Provides a SportsCar class that can be used to build a sports car.

    SportsCar is a subclass of Automobile. To use properly, override any
    stage in the Automobile class to do work that is specific to building
    a sports car. For instance, the build_engine() method is a good method
    here to be overriden. The engine is a sports car is usually much more
    advanced than the engines in everyday generic automobiles. 

    The baseclass 'build()' method should most likely not be overrided, as
    that is a Template Method that specifies the general stages used to
    produce automobiles.
"""
from threading import Thread, Event
from automobile import Automobile, set_state


class SportsCar(Automobile):
    def __init__(self, mode, rate):
        Automobile.__init__(self, mode, rate)
        self.type = "sports car"

    @set_state
    def build_engine(self):
        print "*** Start building engine ***"; self._build_time(17)
        print "    Machining aluminum engine block"
        print "    Boring and stroking the engine block"
        print "    Installing titanium pistons rods and valves, balanced crank, seals"
        print "    Installing timing chain"
        print "    Installing direct fuel injection"
        print "    Installing electronic ignitions system"
        print "    Installing belts"

    @set_state
    def build_transmission(self):
        print "*** Start building clutch and transmission ***"; self._build_time(14)
        print "    Building transmission"
        print "    Building clutch"
        
    @set_state
    def build_frame(self):
        print "*** Start frame assembly ***"; self._build_time(22)
        print "    Building transmission"
        print "    Building graphite monocoque frame"

    @set_state
    def build_chassis_part1(self):
        self.built_frame_event.wait()
        print "*** Start assembling the first part of the chassis ***"; self._build_time(10)
        print "    Installing brake lining"
        print "    Installing fuel lining"
        print "    Installing firewall"
        print "    Installing wheel hub assymbly"

    @set_state
    def build_chassis_part2(self):
        self.built_engine_event.wait() 
        self.built_chassis_part1_event.wait()
        print "*** Start assembling the second part of the chassis ***"; self._build_time(6)
        print "    Installing dohc flat-6, 315bhp 266lb-ft @ 4500 rpm mid-engine"

    @set_state
    def build_chassis_part3(self):
        self.built_transmission_event.wait()
        self.built_chassis_part2_event.wait()
        print "*** Start assembling the third part of the chassis ***"; self._build_time(10)
        print "    Installing dual clutch transmission"
        print "    Installing driveshaft"
        print "    Installing limited-slip differential"
        print "    Installing suspension"
        print "    Installing MagneRide MacPherson strut, coil springs, anti-roll bar"
        print "    Installing exhaust system"
        print "    Installing rack & pinion hydraulic assist stearing assembly"
        print "    Installing gas tank and fuel pump"
        print "    Installing drive axles"
        print "    Installing wheel hub assymbly"
        print "    Installing 13\"/11.8\" 4 piston vented disc brake system"
        print "    Installing CV joints"
        print "    Applying chassis undercoating"

    @set_state
    def post_chassis_assembly(self):
        self.built_chassis_part3_event.wait() # let others know the first part of the chassis is built
        print "*** Start post chassis assembly ***"; self._build_time(18.5)
        print "    Installing wiring harness"
        print "    Installing cooling system"
        print "    Installing body panels"
        print "    Post Chassis Assembly: Painting body with Saphire Blue Metalic"
        print "    Installing clutch and transmission"

        # All three subassemblies can be done in parallel
        #self.assemble_interior()
        if self.mode == 'parallel':
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
        else:
            self.assemble_interior()
            self.install_exterior_lighting
            self.install_wheel_assembly

        print "    Installing doors"
        print "    Installing windshield and wipers"

    def assemble_interior(self):
        print "*   Assembling Interior"; self._build_time(36)
        print "    Installing dashboard"
        print "    Installing 10 speaker surround sound system"
        print "    Installing instrument cluster"
        print "    Installing Leather package"
        print "    Installing carpeting"
        print "    Installling Steering wheel and control assemblies"
        print "    Installing manually adjustable sport seating"
        print "    Testing interior lighting"

    def install_wheel_assembly(self):
        print "*   Installing Wheel Assembly *"; self._build_time(4)
        print "    Installing 235/35ZR-20 / 265/35Z/R-20 Pirelli PZero tires on wheels"
        print "    Mounting cast alloy 20\" wheels"

    #@set_state # don't decorate if baseclass function is called
    def test_drive(self):
        super(SportsCar, self).test_drive()
        print "    Testing on Nurburgring"; self._build_time(1.5)
        self.state = "Vroom Vroom"

