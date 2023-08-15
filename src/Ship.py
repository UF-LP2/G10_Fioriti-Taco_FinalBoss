class Ship:
    numbarco=0
    def __init__(self, draft, crew):
        Ship.numbarco += 1
        self.numbarco = Ship.numbarco
        self.draft = float(draft)
        self.crew = float(crew)

    def is_worth_it(self):
        if self.draft - self.pesototal() < 20:
            raise ValueError
        return "Barco robado"



    def pesototal(self):
        return self.crew*1.5

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
        return "Barco robado"


