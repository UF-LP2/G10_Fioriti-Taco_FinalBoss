from src.Ship import Cruise
from src.Ship import Cargo
from src.Ship import Ship
import csv

def verificar(x):
    try:
        float(x)
        return x
    except ValueError:
        return False

def main()->None:
    with open("src/ships.csv") as file:
        reader = csv.reader(file, delimiter=',')
        next(file, None)

        for line in reader:

            if verificar(line[0]) and verificar(line[1]):

                if line[3] == "" and line[2] != "":
                    crucero = Cruise(verificar(line[2]), line[0], line[1])
                    try:
                        abordar = crucero.is_worth_it()
                        print(abordar)
                    except ValueError:
                        print("No asaltar")

                elif line[3] != "" and line[2] != "":
                    barco = Cargo(verificar(line[2]), verificar(line[3]), line[0], line[1])
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
