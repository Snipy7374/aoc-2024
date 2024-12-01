from aoc_2024.constants import ASSETS_PATH
from aoc_2024.day_1_1 import list_distance


if __name__ == "__main__":
    a: list[int] = []
    b: list[int] = []
    with open(ASSETS_PATH / "day_1.txt") as f:
        data = f.readlines()
    
    for pair in data:
        splitted = pair.split("   ")

        try:
            a.append(int(splitted[0].strip()))
            b.append(int(splitted[1].strip()))
        except ValueError:
            print("An error occurred while casting a string to int!")
    
    distance = list_distance(a, b)
    print(f"The distance between the two lists is: {distance}")
