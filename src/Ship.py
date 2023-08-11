class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        if self.draft - self.pesototal() <= 20:
            return True
        else:
            return False



    def pesototal(self):
        return self.crew*1.5

    def __del__(self):
        print("barco robado")
