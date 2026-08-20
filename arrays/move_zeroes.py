# QUESTION
# Move all zeroes in a list to the end,
# while keeping the order of the non-zero numbers.
# Do it IN PLACE (do not build a new list).
#
# Example:
#   [0, 1, 0, 3, 12]  ->  [1, 3, 12, 0, 0]
#
# ANSWER
# Two pointers. O(n) time, O(1) extra space.


def move_zeroes(numbers):

    # insert_at marks the position where the next
    # non-zero number should be placed.
    #
    # Everything to the LEFT of insert_at is already
    # a non-zero number in the correct order.
    insert_at = 0

    # First pass: pull every non-zero number
    # forward to the front of the list.
    for i in range(len(numbers)):

        if numbers[i] != 0:

            # Swap the current number into its slot.
            #
            # Python lets us swap in one line:
            # a, b = b, a
            #
            # Example on [0, 1, 0, 3, 12]:
            #   i = 1, insert_at = 0
            #   swap 0 and 1  ->  [1, 0, 0, 3, 12]
            numbers[insert_at], numbers[i] = numbers[i], numbers[insert_at]

            # Move the insert position forward.
            insert_at += 1

    # Every zero has now been pushed behind insert_at,
    # so the list is already finished.
    return numbers


print(move_zeroes([0, 1, 0, 3, 12]))
# Output:
# [1, 3, 12, 0, 0]

print(move_zeroes([0, 0, 1]))
# Output:
# [1, 0, 0]
