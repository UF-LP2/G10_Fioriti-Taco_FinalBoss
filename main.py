from src.cCruise import Cruise
from src.Cargo import Cargo
import csv


def main()->None:
    with open("src/ships.csv") as file:
        reader = csv.reader(file)
        next(file, None)

        for line in file:

                if line[3] == '' and line[2] != 0:
                    crusero = Cruise(line[2], list[0], line[1])
                    try:
                        crusero.is_worth_it()
                    except ValueError:
                        print("Peso menor a 20, no asaltar")



                else:
                    barco = Cargo(line[2], line[3], line[0], line[1])
                    try:
                        barco.is_worth_it()
                    except ValueError:
                        print("peso menor a 20, no asaltar")


#titanic = Cruise(4, 4, 4)
   # bote = Cargo(4, 1, 4, 6)


if __name__ == "__main__":
  main()
