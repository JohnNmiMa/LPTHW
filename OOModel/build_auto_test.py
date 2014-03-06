import unittest
import pdb
from build_auto import BuildAuto

class BuildAutoTest(unittest.TestCase):
    def test_auto_factory(self):
        auto = BuildAuto()
        self.assertEqual("not started", auto.build_state())

    def test_build_engine(self):
        auto = BuildAuto()
        auto.build_engine()
        self.assertEqual("engine built", auto.build_state())

    def test_build_chassis(self):
        auto = BuildAuto()
        auto.build_chassis()
        self.assertEqual("chasis built", auto.build_state())

    
if __name__ == '__main__':
    bct = BuildAutoTest()

