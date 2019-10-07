import math
import sys

if sys.version_info[0] < 3:
    SMALLEST_INTEGER = -sys.maxint
    BIGGEST_INTEGER = sys.maxint
else:
    SMALLEST_INTEGER = float('-inf')
    BIGGEST_INTEGER = float('inf')

def locate(lst):
    length = len(lst)
    left = 0
    right = length
    biggest_element = SMALLEST_INTEGER
    smallest_element = BIGGEST_INTEGER

    # Calculates right offset
    for i, elem in enumerate(lst):
        biggest_element = max(elem, biggest_element)

        if biggest_element > elem:
            right = i

    # Calculates left offset
    for i, elem in enumerate(lst[::-1]):
        smallest_element = min(smallest_element, elem)

        if smallest_element < elem:
            left = length - i - 1

    return (left, right)


assert locate([3, 7, 5, 6, 9]) == (1, 3)
# smallest element at right
assert locate([3, 7, 5, 6, 9, 2]) == (0, 5)
assert locate([2, 3, 5, 6, 9]) == (0, 5)
assert locate([-1000, 2, 3, 4, 6, 5, 9]) == (4, 5)
