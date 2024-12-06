from scripts.constants import ASSETS_PATH
from aoc_2024.day_5 import check_page_ordering, fix_page_ordering


if __name__ == "__main__":
    with open(ASSETS_PATH / "day_5.txt") as f:
        data = f.read()
    
    solution = check_page_ordering(data)
    print(f"The sum of the valid updates middle page is: {solution}")

    solution_pt2 = fix_page_ordering(data)
    print(f"The sum of the fixed updates middle page is: {solution_pt2}")
