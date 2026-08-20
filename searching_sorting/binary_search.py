# QUESTION
# Find the index of a target value in a SORTED list.
# Return -1 if it is not there.
#
# Example:
#   [1, 3, 5, 7, 9], target 7  ->  index 3
#
# ANSWER
# Binary search. Halve the search range each step,
# so O(log n) instead of O(n).
#
# The list MUST already be sorted for this to work.

import bisect


def binary_search(numbers, target):

    low = 0
    high = len(numbers) - 1

    # while low <= high, NOT low < high.
    #
    # Using < would skip the case where the range has
    # narrowed to a single element - a very common bug.
    while low <= high:

        # The midpoint.
        #
        # // is integer division, so 7 // 2 == 3.
        # Plain / would give a float and break indexing.
        mid = (low + high) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            # The target must be in the RIGHT half.
            # mid is already checked, so start past it.
            low = mid + 1

        else:
            # The target must be in the LEFT half.
            high = mid - 1

    # The range collapsed without a match.
    return -1


def insert_position(numbers, target):

    # Follow-up question interviewers like:
    # "where WOULD this value go to keep the list sorted?"
    #
    # The standard library already does this.
    # bisect_left returns the leftmost valid position.
    return bisect.bisect_left(numbers, target)


print(binary_search([1, 3, 5, 7, 9], 7))
# Output:
# 3

print(binary_search([1, 3, 5, 7, 9], 4))
# Output:
# -1

print(insert_position([1, 3, 5, 7, 9], 4))
# Output:
# 2
