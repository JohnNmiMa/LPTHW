import unittest
import pdb
from automobile import Automobile

class BuildAutoTest(unittest.TestCase):
    def test_auto_factory(self):
        auto = Automobile('serial')
        self.assertEqual("not started", auto.build_state())

    def test_build_auto(self):
        auto = Automobile('serial')

        auto.build_engine()
        self.assertEqual("engine built", auto.build_state())

        auto.build_transmission()
        self.assertEqual("transmission built", auto.build_state())

        auto.build_frame()
        self.assertEqual("frame built", auto.build_state())

        auto.build_chassis_part1()
        self.assertEqual("chassis part 1 built", auto.build_state())
        auto.build_chassis_part2()
        self.assertEqual("chassis part 2 built", auto.build_state())
        auto.build_chassis_part3()
        self.assertEqual("chassis part 3 built", auto.build_state())

        auto.post_chassis_assembly()
        self.assertEqual("post chassis assembly complete", auto.build_state())

        auto.add_fluids()
        self.assertEqual("fluids added", auto.build_state())

        auto.test_drive()
        self.assertEqual("Beep Beep", auto.build_state())

    def test_build_serial(self):
        auto = Automobile('serial')
        auto.build()
        self.assertEqual("Beep Beep", auto.build_state())

    def test_build_parallel(self):
        auto = Automobile('parallel')
        auto.build()
        self.assertEqual("Beep Beep", auto.build_state())
