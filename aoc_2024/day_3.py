import re

MUL_PATTERN = r"\S?mul\((?P<number_1>\d+),(?P<number_2>\d+)\)"


def mul(instructions: str) -> int:
    pairs = re.findall(MUL_PATTERN, instructions)
    result = 0
    for (a, b) in pairs:
        result += int(a) * int(b)
    return result


# not my solution (wasn't able to come up with a regex simple enough)
# made by https://github.com/Starwort
CONDITIONAL_MUL_PATTERN = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
def mul_pt_2(instructions: str) -> int:
    data = re.findall(CONDITIONAL_MUL_PATTERN, instructions)
    on = True
    result = 0
    for a, b, do, dont in data:
        if dont:
            on = False
        elif do:
            on = True
        elif on:
            result += int(a) * int(b)

    return result
