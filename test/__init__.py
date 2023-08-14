from src.cCruise import Cruise
from src.Cargo import Cargo
from src.Ship import Ship
def test_is_worth_it():
    crucero = Cruise(172, 2198, 488)
    assert crucero.is_worth_it() == "Barco robado"
