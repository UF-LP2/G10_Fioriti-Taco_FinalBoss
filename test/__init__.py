from src.cCruise import Cruise
from src.Cargo import Cargo
from src.Ship import Ship
import pytest

def Test_worth_it():
    crucero = Cruise(172, 2198, 488)
    assert crucero.is_worth_it() == "Barco robado"

def Test_ceros():
    barco = Cargo(0, 0, 0, 0)
    with pytest.raises(Exception):
        barco.is_worth_it()

class Test3(unittest.TestCase):
    def test_negativos(self):
        nave = Ship(-1, -5)
        assert nave.is_worth_it() == "peso menor a 20, no asaltar"
