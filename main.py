from src.Ship import Cruise
from src.Ship import Cargo
from src.Ship import Ship
import csv


def main()->None:
    with open("src/ships.csv") as file:
        reader = csv.reader(file, delimiter=',')
        next(file, None)

        for line in reader:

                if line[3] == "" and line[2] != "":
                    crucero = Cruise(line[2], line[0], line[1])
                    try:
                        abordar = crucero.is_worth_it()
                        print(abordar)
                    except ValueError:
                        print("No asaltar")

                elif line[3] != "" and line[2] != "":
                    barco = Cargo(line[2], line[3], line[0], line[1])
                    try:
                        abordar = barco.is_worth_it()
                        print(abordar)
                    except ValueError:
                        print("No asaltar")

                else:
                    barquito = Ship(line[0], line[1])
                    try:
                        abordar = barquito.is_worth_it()
                        print(abordar)
                    except ValueError:
                        print("No asaltar")



if __name__ == "__main__":
  main()
