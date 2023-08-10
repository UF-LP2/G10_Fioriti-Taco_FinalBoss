from src.cCruise import Cruise
from src.Cargo import Cargo


def main() -> None:
    with open("ships.csv") as file:
        reader = csv.reader(file)
        #tenemos que decidir que tipo de barco es el que se refiere

    titanic = Cruise(4, 4, 4)
    bote = Cargo(4, 1, 4, 6)


if __name__ == "__main__":
  main()
