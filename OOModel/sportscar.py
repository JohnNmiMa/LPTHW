from automobile import Automobile, set_state

class SportsCar(Automobile):
    def __init__(self):
        Automobile.__init__(self)
        self.type = "sports car"

    @set_state
    def build_engine(self):
        #self.state = "building engine"
        print "    Machining aluminum engine block"
        print "    Boring and stroking the engine block"
        print "    Installing titanium pistons rods and valves, balanced crank, seals"
        print "    Installing timing chain"
        print "    Installing direct fuel injection"
        print "    Installing electronic ignitions system"
        print "    Installing belts"
        #self.state = "engine built"

        print "    Building monocoque frame"

    @set_state
    def build_chassis(self):
        self.state = "building chassis"
        self.build_frame()
        print "    Installing brake lining"
        print "    Installing fuel lining"
        print "    Installing firewall"
        print "    Installing dohc flat-6, 315bhp 266lb-ft @ 4500 rpm mid-engine"
        print "    Installing dual clutch transmission"
        print "    Installing driveshaft"
        print "    Installing limited-slip differential"
        print "    Installing MagneRide MacPherson strut, coil springs, anti-roll bar"
        print "    Installing exhaust system"
        print "    Installing rack & pinion hydraulic assist stearing assembly"
        print "    Installing gas tank and fuel pump"
        print "    Installing drive axles"
        print "    Installing wheel hub assymbly"
        print "    Installing 13\"/11.8\" 4 piston vented disc brake system"
        print "    Installing CV joints"
        print "    Applying chassis undercoating"
        self.state = "chassis built"

    @set_state
    def post_chassis_assembly(self):
        self.state = "performing post chassis assembly"
        print "    Post Chassis Assembly: Installing wiring harness"
        print "    Post Chassis Assembly: Installing cooling system"
        print "    Post Chassis Assembly: Installing body panels"
        print "    Post Chassis Assembly: Painting body with Saphire Blue Metalic"
        print "    Post Chassis Assembly: Installing clutch and transmission"
        print "    Post Chassis Assembly: Assembling Interior"
        interior = self.assemble_interior()
        print "    Post Chassis Assembly: Installing doors"
        print "    Post Chassis Assembly: Installling exterior lighting assemblies"
        interior = self.install_exterior_lighting()
        print "    Post Chassis Assembly: Installing wheels assembly"
        interior = self.install_wheel_assembly()
        print "    Post Chassis Assembly: Installing windshield and wipers"
        self.state = "post chassis assembly complete"

    def assemble_interior(self):
        print "    Installing dashboard"
        print "    Installing 10 speaker surround sound system"
        print "    Installing instrument cluster"
        print "    Installing Leather package"
        print "    Installing carpeting"
        print "    Installling Steering wheel and control assemblies"
        print "    Installing manually adjustable sport seating"
        print "    Testing interior lighting"

    def install_wheel_assembly(self):
        print "    Installing 235/35ZR-20 / 265/35Z/R-20 Pirelli PZero tires on wheels"
        print "    Mounting cast alloy 20\" wheels"

    #@set_state # don't decorate if baseclass function is called
    def test_drive(self):
        #Automobile.test_drive(self)
        super(SportsCar, self).test_drive()
        print "    Testing on Nurburgring"
        self.state = "Vroom Vroom"
