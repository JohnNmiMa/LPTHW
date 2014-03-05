# -*- coding: utf-8 -*-
import unittest
from pickler import Pickler
 
class PicklerTest(unittest.TestCase):

    pickle_file_name = 'cars_file'
    carlist = ['VW Jetta GLX','Ferarri 308 GTB','Lamboghini Miura',\
               'Porsche Boxter S', 'Olds 67 Cutlass', 'Chevy Corvette Stingray',\
               'Aston Martin D7', 'Jaguar E-Type', 'Alpha Romeo 33 Stradale',\
               'Austin Healy BN7', 'BMW Z8', 'Buick Riviera', 'Ford GT40',\
               'Chevy Corvair', 'Ferrari 360 Modena',\
               'Ford Mustang GT Fastback Bullitt', 'Porsche Cayman']
    lp = Pickler()

    def setUp(self):
        self.cars_file = open(self.pickle_file_name, 'wb+')

    def tearDown(self):
        self.cars_file.close()

    def test_list_pickler(self):
        self.lp.list_pickler(self.carlist, self.cars_file)
        self.cars_file.seek(0)
        cars = self.cars_file.read()
        self.assertIn('Cayman', cars)

    def test_unpickle(self):
        # Pickle the cars
        self.lp.list_pickler(self.carlist, self.cars_file)
        self.cars_file.seek(0)

        # Unpickle the cars
        unpickled_carlist = self.lp.unpickler(self.cars_file)

        self.assertEqual(unpickled_carlist, self.carlist)
 
