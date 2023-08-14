from src.cCruise import Cruise
from src.Cargo import Cargo
from src.Ship import Ship
import csv


def main()->None:
    with open("src/ships.csv") as file:
        reader = csv.reader(file, delimiter=',')
        next(file, None)

        for line in reader:

                if line[3] == "" and line[2] != "":
                    crusero = Cruise(line[2], line[0], line[1])
                    try:
                        crusero.is_worth_it()
                    except ValueError:
                        print("Peso menor a 20, no asaltar")

                elif line[3] != "" and line[2] != "":
                    lol = line[3]
                    barco = Cargo(line[2], line[3], line[0], line[1])
                    try:
                        barco.is_worth_it()
                    except ValueError:
                        print("peso menor a 20, no asaltar")

                else:
                    barquito = Ship(line[0], line[1])
                    try:
                        barquito.is_worth_it()
                    except ValueError:
                        print("peso menor a 20, no robar")

#titanic = Cruise(4, 4, 4)
# bote = Cargo(4, 1, 4, 6)


if __name__ == "__main__":
  main()
