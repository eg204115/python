# QUESTION
# Given a list of integers, find the contiguous subarray
# with the largest sum, and return that sum.
#
# Example:
#   [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#   The best subarray is [4, -1, 2, 1] which sums to 6.
#
# ANSWER
# Kadane's algorithm. One pass, O(n) time, O(1) space.


def max_subarray(numbers):

    # Handle the empty list so we never
    # return something meaningless.
    if not numbers:
        return 0

    # best_here = the largest sum of a subarray
    #             that ENDS at the current position.
    #
    # best_total = the largest sum we have seen
    #              anywhere so far.
    #
    # Both start at the first number.
    best_here = numbers[0]
    best_total = numbers[0]

    # Start from index 1 because index 0
    # is already inside our starting values.
    for number in numbers[1:]:

        # The key decision at every step:
        #
        # Do we EXTEND the previous subarray,
        # or do we START a new one at this number?
        #
        # If best_here is negative, dragging it along
        # only hurts us, so we start fresh.
        #
        # Example:
        #   best_here = -3, number = 4
        #   -3 + 4 = 1   but   4 alone = 4
        #   So we start fresh with 4.
        best_here = max(number, best_here + number)

        # Record the best sum seen so far.
        best_total = max(best_total, best_here)

    return best_total


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# Output:
# 6

print(max_subarray([-3, -1, -2]))
# Output:
# -1
