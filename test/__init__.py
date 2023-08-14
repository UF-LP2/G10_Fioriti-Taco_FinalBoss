from src.cCruise import Cruise
from src.Cargo import Cargo
from src.Ship import Ship
import unittest

class Test1(unittest.TestCase):
    def test_is_worth_it(self):
        crucero = Cruise(172, 2198, 488)
        assert crucero.is_worth_it() == "Barco robado"

class Test2(unittest.TestCase):
    def test_ceros(self):
        barco = Cargo(0, 0, 0, 0)
        barco.is_worth_it()
        self.assertRaises(ValueError,"peso menor a 20, no asaltar")



class Test3(unittest.TestCase):
    def test_negativos(self):
        nave = Ship(-1, -5)
        assert nave.is_worth_it() == "peso menor a 20, no asaltar"
