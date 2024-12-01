from aoc_2024.constants import ASSETS_PATH
from aoc_2024.day_1_2 import list_similarity


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
    
    similarity = list_similarity(a, b)
    print(f"The similarity between the two lists is: {similarity}")
