#from src.cCruise import Cruise
#from src.Cargo import Cargo
from src.Ship import Ship
from src.Ship import Cargo
from src.Ship import Cruise

import pytest

def test_worth_it():
    crucero = Cruise(172, 2198, 488)
    assert crucero.is_worth_it() == "Barco robado"

def test_ceros():
    barco = Cargo(0, 0, 0, 0)
    with pytest.raises(ValueError):
        barco.is_worth_it()

def test_negativos():
    nave = Ship(-1, -5)
    with pytest.raises(ValueError):
        nave.is_worth_it()
