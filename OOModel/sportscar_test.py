import unittest
import pdb
from sportscar import SportsCar

class BuildSportsTest(unittest.TestCase):
    rate = 2000.0

    def test_auto_factory(self):
        auto = SportsCar('serial', BuildSportsTest.rate)
        self.assertEqual("not started", auto.build_state())

    def test_build_auto(self):
        auto = SportsCar('serial', BuildSportsTest.rate)
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
        self.assertEqual("Vroom Vroom", auto.build_state())

    def test_build_serial(self):
        auto = SportsCar('serial', BuildSportsTest.rate)
        auto.build()
        self.assertEqual("Vroom Vroom", auto.build_state())

    def test_build_parallel(self):
        auto = SportsCar('parallel', BuildSportsTest.rate)
        auto.build()
        self.assertEqual("Vroom Vroom", auto.build_state())

    def test_engine_trans_frame_parallel_build_in_any_order(self):
        auto = SportsCar('parallel', BuildSportsTest.rate)
        auto.build_frame()
        self.assertEqual("frame built", auto.build_state())

        auto.build_transmission()
        self.assertEqual("transmission built", auto.build_state())

        auto.build_engine()
        self.assertEqual("engine built", auto.build_state())

    def test_engine_trans_frame_serial_build_in_any_order(self):
        auto = SportsCar('serial', BuildSportsTest.rate)
        auto.build_frame()
        self.assertEqual("frame built", auto.build_state())

        auto.build_transmission()
        self.assertEqual("transmission built", auto.build_state())

        auto.build_engine()
        self.assertEqual("engine built", auto.build_state())

