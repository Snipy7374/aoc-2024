from scripts.constants import ASSETS_PATH
from aoc_2024.day_4 import xmas_counter, mas_x_counter


if __name__ == "__main__":
    with open(ASSETS_PATH / "day_4.txt") as f:
        data = f.readlines()
    
    solution = xmas_counter(data)
    print(f"The number of xmas is: {solution}")


    solution_2 = mas_x_counter(data)
    print(f"The number of mas X shaped is: {solution_2}")