# QUESTION
# For every number in a list, find the next number
# to its RIGHT that is bigger than it.
# If there is none, use -1.
#
# Example:
#   [2, 1, 2, 4, 3]  ->  [4, 2, 4, -1, -1]
#
#   2 -> the next bigger to the right is 4
#   1 -> 2
#   2 -> 4
#   4 -> nothing bigger, so -1
#
# ANSWER
# The brute force is a nested loop, O(n^2).
#
# The stack answer is O(n): we keep a stack of
# positions that are still WAITING for their answer.
# When a bigger number arrives, it resolves all of them.


def next_greater_element(numbers):

    n = len(numbers)

    # Start by assuming nobody has an answer.
    result = [-1] * n

    # This stack holds INDEXES, not values.
    # Storing indexes is what lets us write the
    # answer back into the right slot.
    stack = []

    for i, number in enumerate(numbers):

        # While the number on top of the stack is
        # smaller than the current number, the current
        # number IS its next greater element.
        #
        # Example on [2, 1, 2, 4, 3] when i = 3 (number 4):
        #   the stack holds indexes 0, 1, 2 (values 2, 1, 2)
        #   4 is bigger than all of them, so all three
        #   get resolved to 4 in this one while loop.
        while stack and numbers[stack[-1]] < number:

            # Remove the waiting index and fill its answer.
            waiting_index = stack.pop()
            result[waiting_index] = number

        # The current number now waits for ITS answer.
        stack.append(i)

    # Anything left on the stack never found a bigger
    # number, and those slots are already -1.
    return result


print(next_greater_element([2, 1, 2, 4, 3]))
# Output:
# [4, 2, 4, -1, -1]

print(next_greater_element([5, 4, 3]))
# Output:
# [-1, -1, -1]
