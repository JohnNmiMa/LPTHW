from build_engine import BuildEngine
from build_chassis import BuildChassis

class BuildAuto:
    state = "not started"
    def build_state(self):
        return self.state

    def build_auto(self):
        print """
        *******************************************
        *** Start building a generic automobile ***
        *******************************************
        """
        self.build_engine()

    def build_engine(self):
        engine = BuildEngine()
        print "*** Start building the engine ***"
        self.state = "building engine"
        engine.build()
        self.state = "engine built"

    def build_chasis(self):
        engine = BuildChassis()
        print "*** Start building the chassis ***"
        self.state = "building chassis"
        engine.build()
        self.state = "chassis built"
