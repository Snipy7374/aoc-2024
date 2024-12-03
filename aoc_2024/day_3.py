import re

MUL_PATTERN = r"\S?mul\((?P<number_1>\d+),(?P<number_2>\d+)\)"


def mul(instructions: str) -> int:
    pairs = re.findall(MUL_PATTERN, instructions)
    result = 0
    for (a, b) in pairs:
        result += int(a) * int(b)
    return result
