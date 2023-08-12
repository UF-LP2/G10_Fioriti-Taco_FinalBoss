from src.Ship import Ship
class Cargo(Ship):
    def __init__(self, cargo, quality, draft, crew):
        self.cargo = cargo
        self.quality = quality
        super().__init__(draft, crew)

    def pesototal(self):
        acum = self.crew*1.5

        if self.quality == 1:
            acum = acum + self.cargo*3.5
        elif self.quality == 0.5:
            acum = acum + self.cargo*2
        elif self.quality == 0.25:
            acum = acum+self.cargo*0.5
        return acum

    def is_worth_it(self):
        if self.draft - self.pesototal() >= 20:
            return True
        else:
            raise ValueError


