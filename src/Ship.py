class Ship:
    numbarco=0
    def __init__(self, draft, crew):
        Ship.numbarco += 1
        self.numbarco = Ship.numbarco
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        if float(self.draft) - self.pesototal() <= 20:
            raise ValueError
        print("Barco robado")
        return



    def pesototal(self):
        return float(self.crew)*1.5

    def __del__(self):
        print("barco robado")
