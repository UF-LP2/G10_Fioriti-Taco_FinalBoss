from src.cCruise import Cruise
from src.Cargo import Cargo
# incluir el archivo csv

def main() -> None:
    with open("ships.csv", "r") as file:
        yes = False
        reader = csv.reader(file, delimiter = ",")
        next(file, None)
        for line in file:

            if line[3] == 0:
                crusero = Cruise(line[2], list[0], line[1])
                yes = crusero.is_worth_it()


            else:
                barco = Cargo(line[2], line[3], line[0], line[1])
                yes = barco.is_worth_it()


  #  titanic = Cruise(4, 4, 4)
   # bote = Cargo(4, 1, 4, 6)


if __name__ == "__main__":
  main()
