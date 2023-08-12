from src.cCruise import Cruise
from src.Cargo import Cargo
import csv

def main()->None:
    with open("ships.csv") as file:
        yes = False
        reader = csv.reader(file, delimiter = ",")
        next(file, None)
        try:
            for line in file:

                if line[3] == 0:
                    crusero = Cruise(line[2], list[0], line[1])
                    yes = crusero.is_worth_it()


                else:
                    barco = Cargo(line[2], line[3], line[0], line[1])
                    yes = barco.is_worth_it()
        except ValueError:
            print("Peso menor a 20, no asaltar")

#titanic = Cruise(4, 4, 4)
   # bote = Cargo(4, 1, 4, 6)


if __name__ == "__main__":
  main()
