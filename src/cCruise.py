from src.Ship import Ship
class Cruise(Ship):
    def __init__(self, passengers, draft, crew):
        self.passengers = float(passengers)
        super().__init__(draft, crew)

    def pesototal(self):
        peso = self.passengers*2.25 + self.crew*1.5
        return peso

    def is_worth_it(self):
        if self.draft - self.pesototal() < 20:
            raise ValueError
        return "Barco robado"
