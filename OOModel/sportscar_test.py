import unittest
import pdb
from sportscar import SportsCar

class BuildSportsTest(unittest.TestCase):
    def test_auto_factory(self):
        auto = SportsCar()
        self.assertEqual("not started", auto.build_state())

    def test_build_auto(self):
        auto = SportsCar()
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
        self.assertEqual("Vroom Vroom", auto.build_state())

    def test_build(self):
        auto = SportsCar()
        auto.build()
        self.assertEqual("Vroom Vroom", auto.build_state())
