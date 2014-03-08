import unittest
import pdb
from automobile import Automobile

class BuildAutoTest(unittest.TestCase):
    def test_auto_factory(self):
        auto = Automobile()
        self.assertEqual("not started", auto.build_state())

    def test_build_auto(self):
        auto = Automobile()
        auto.build_engine()
        self.assertEqual("engine built", auto.build_state())

        auto.build_chassis()
        self.assertEqual("chassis built", auto.build_state())

        auto.build_chassis()
        self.assertEqual("chassis built", auto.build_state())

        auto.post_chassis_assembly()
        self.assertEqual("post chassis assembly complete", auto.build_state())

        auto.add_fluids()
        self.assertEqual("fluids added", auto.build_state())

        auto.test_drive()
        self.assertEqual("Beep Beep", auto.build_state())

    def test_build(self):
        auto = Automobile()
        auto.build()
        self.assertEqual("Beep Beep", auto.build_state())
