# QUESTION
# For each position, return the product of every
# OTHER number in the list.
# You are not allowed to use division.
#
# Example:
#   [1, 2, 3, 4]  ->  [24, 12, 8, 6]
#
#   position 0: 2 * 3 * 4 = 24
#   position 1: 1 * 3 * 4 = 12
#
# ANSWER
# For each position, the answer is
# (product of everything on the left)
# multiplied by
# (product of everything on the right).
#
# Two passes, O(n) time.


def product_except_self(numbers):

    n = len(numbers)

    # Start with all 1s.
    #
    # 1 is the safe starting value for multiplication,
    # the same way 0 is for addition.
    result = [1] * n

    # PASS 1 - left to right.
    #
    # running holds the product of everything
    # BEFORE the current position.
    running = 1

    for i in range(n):

        # Store the left-side product first,
        # BEFORE folding in numbers[i].
        # That is what excludes the number itself.
        result[i] = running

        running = running * numbers[i]

    # After pass 1 on [1, 2, 3, 4]:
    # result = [1, 1, 2, 6]

    # PASS 2 - right to left.
    #
    # running now holds the product of everything
    # AFTER the current position.
    running = 1

    # range(n - 1, -1, -1) counts DOWN:
    # start at n-1, stop before -1, step -1.
    for i in range(n - 1, -1, -1):

        # Multiply the left product we already stored
        # by the right product we are carrying.
        result[i] = result[i] * running

        running = running * numbers[i]

    return result


print(product_except_self([1, 2, 3, 4]))
# Output:
# [24, 12, 8, 6]

print(product_except_self([2, 3]))
# Output:
# [3, 2]
