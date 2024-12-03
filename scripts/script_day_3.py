from scripts.constants import ASSETS_PATH
from aoc_2024.day_3 import mul

if __name__ == "__main__":
    with open(ASSETS_PATH / "day_3.txt") as f:
        data = f.read()
    
    solution = mul(data)
    print(f"The result of the mul instructions is: {solution}")
