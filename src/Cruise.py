import Ship

class Cruise(Ship):
    def __init__(self, passengers, draft, crew):
            self.passengers = passengers
            super().__init__(draft,crew)

    def pesototal(self):
        return (self.passengers*2.25)+(self.crew*1.5)

    def is_worth_it(self):
        if self.draft - self.pesototal()<=20:
            return True
        else:
            return False


