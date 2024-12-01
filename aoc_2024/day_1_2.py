from aoc_2024.day_1_1 import list_max_value

# The second part of the problem is even easier, I already implemented the core
# algorithm for the solution. Though I will adapt in this context.


# this is the same hystogram system used in the integer_sort
# that I implemented in the first part of the problem
def count_number(list_: list[int]) -> list[int]:
    # time O(n), memory O(1)
    n_max = list_max_value(list_) + 1

    # inizialize the hystogram
    # time and memory O(n)
    x = [0 for _ in range(n_max)]

    # count the occurrence of the numbers
    # time O(n) memory O(1)
    for n in list_:
        x[n] += 1
    return x


# time complexity: O(2n) ~ O(n)
# memory complexity: O(n)
def list_similarity(a: list[int], b: list[int]) -> int:
    hystogram = count_number(b)
    similarity = 0

    for n in a:
        similarity += n * hystogram[n]

    return similarity
