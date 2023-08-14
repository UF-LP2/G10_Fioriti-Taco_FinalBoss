from src.Ship import Ship
class Cargo(Ship):
    def __init__(self, cargo, quality, draft, crew):
        self.cargo = float(cargo)
        self.quality = float(quality)
        super().__init__(draft, crew)

    def pesototal(self):
        acum = self.crew*1.5
        return acum


    def is_worth_it(self):
        if self.quality == 1:
            self.draft = self.draft + self.cargo*3.5
        elif self.quality == 0.5:
            self.draft = self.draft + self.cargo*2
        elif self.quality == 0.25:
            self.draft = self.draft + self.cargo*0.5

        if self.draft - self.pesototal() < 20:
            raise ValueError
        print("Barco Robado")
        return


