from scripts.constants import ASSETS_PATH
from aoc_2024.day_2_1 import analyze_safe_reports
from aoc_2024.day_2_2 import analyze_safe_reports_pt2


if __name__ == "__main__":
    reports: list[list[int]] = []
    with open(ASSETS_PATH / "day_2.txt") as f:
        data = f.readlines()
    
    for line in data:
        reports.append(list(map(int, line.split(" "))))
    
    solution = analyze_safe_reports(reports)
    print(f"The total number of safe reports is: {solution}")

    solution = analyze_safe_reports_pt2(reports)
    print(f"The total number of safe reports is: {solution}")
