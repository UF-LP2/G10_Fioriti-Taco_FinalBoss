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
        print("Barco robado")
        return



    def pesototal(self):
        return self.crew*1.5

    def __del__(self):
        print("barco robado")
