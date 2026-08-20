# QUESTION
# Count how many contiguous subarrays add up
# to exactly k.
#
# Example:
#   numbers = [1, 1, 1], k = 2  ->  2
#   (the subarrays [1,1] at positions 0-1 and 1-2)
#
# ANSWER
# The brute force answer is to test every subarray,
# which is O(n^2). Interviewers usually want better.
#
# The trick is PREFIX SUMS.
#
# Let running = sum of everything up to position i.
# A subarray ending at i sums to k exactly when
# some earlier prefix equals (running - k).
#
#   sum(j..i) = running_i - running_j
#   so  running_i - running_j = k
#   means  running_j = running_i - k
#
# So we count how often each prefix sum has occurred.
# O(n) time.

from collections import defaultdict


def subarray_sum(numbers, k):

    # seen maps:  prefix sum -> how many times we hit it
    #
    # We seed it with {0: 1} to represent the empty
    # prefix "before the list starts".
    #
    # That is what lets a subarray starting at index 0
    # be counted, because then running - k == 0.
    seen = defaultdict(int)
    seen[0] = 1

    running = 0
    count = 0

    for number in numbers:

        # Extend the prefix sum.
        running += number

        # How many earlier prefixes would leave
        # exactly k behind them?
        #
        # Each one marks a valid subarray ending here.
        count += seen[running - k]

        # Record the current prefix for future positions.
        seen[running] += 1

    return count


print(subarray_sum([1, 1, 1], 2))
# Output:
# 2

print(subarray_sum([1, 2, 3], 3))
# Output:
# 2

print(subarray_sum([1, -1, 0], 0))
# Output:
# 3
