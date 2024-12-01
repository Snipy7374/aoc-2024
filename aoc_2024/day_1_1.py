# The problem can be solved by sorting the lists and making the calculations
# as such the given problem, with the classic sorting solutions, is Omega(n log(n))
# hovewer we know the type of the items contained in the lists!
# They're always integers, as such we can use some peculiar algorithm that sorts in O(n)!


# time complexity: O(n)
# memory complexity: O(1)
def list_max_value(list_: list[int]) -> int:
    _n_max = list_[0]
    for i in range(1, len(list_)):
        if list_[i] > _n_max:
            _n_max = list_[i]

    return _n_max


# time and memory complexity: O(1)
def max_2(a: int, b: int) -> int:
    if a >= b:
        return a
    return b


# time complexity: O(4n) ~ O(n)
# memory complexity: O(n)
def integer_sort(list_: list[int]) -> None:
    # time O(n), memory O(1)
    n_max = list_max_value(list_) + 1

    # inizialize the histogram
    # time and memory O(n)
    x = [0 for _ in range(n_max)]

    # count the occurrence of the numbers
    # time O(n) memory O(1)
    for n in list_:
        x[n] += 1

    # index to keep track what element of
    # l to overwrite
    f = 0
    # time O(n) memory O(1)
    for i in range(len(x)):
        while x[i] > 0:
            list_[f] = i
            x[i] -= 1
            f += 1


# since the problem didn't specify if the two lists have always the same lenght
# I made this algorithm iterate based on the longest list; that's why, later on, I
# needed to catch possible IndexError(s)
# time complexity: O(3n) ~ O(n)
# memory complexity (considering integer_sort): O(2n) ~ O(n)
def list_distance(a: list[int], b: list[int]) -> int:
    # O(n)
    integer_sort(a)
    # O(n)
    integer_sort(b)

    result = 0
    # O(n)
    for i in range(max_2(len(a), len(b))):
        try:
            a_val = a[i]
        except IndexError:
            a_val = 0

        try:
            b_val = b[i]
        except IndexError:
            b_val = 0

        result += abs(a_val - b_val)
    return result


# Post-submit thoughts:
# the inputs were bigger than I thought, for even better performances it
# could be better to use radix_sort which reduces memory usage with a little
# time complexity increase (O(n log(k))) or even better use pivot randomized quick_sort
