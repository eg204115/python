# QUESTION
# Flatten an arbitrarily nested list into a flat list.
#
# Example:
#   [1, [2, [3, 4], 5], 6]  ->  [1, 2, 3, 4, 5, 6]
#
# The nesting can be any depth, so a fixed number of
# loops will not do.
#
# ANSWER
# Recursion: if an item is itself a list, flatten it too.


def flatten(nested):

    flat = []

    for item in nested:

        # isinstance() checks the TYPE of a value.
        #
        # We accept both lists and tuples so that
        # [1, (2, 3)] also flattens.
        if isinstance(item, (list, tuple)):

            # The recursive step.
            #
            # flatten(item) returns an already-flat list,
            # and extend() adds all of its elements.
            #
            # Note extend() not append():
            #   append([2, 3])  ->  [[2, 3]]   (wrong)
            #   extend([2, 3])  ->  [2, 3]     (right)
            flat.extend(flatten(item))

        else:
            # A plain value - the base case.
            flat.append(item)

    return flat


def flatten_iterative(nested):

    # The same job without recursion, using a stack.
    # Worth knowing in case the interviewer asks for it,
    # or the nesting is deep enough to hit Python's
    # recursion limit (about 1000 frames by default).

    # Copy the input so we never mutate the caller's list.
    stack = list(nested)
    flat = []

    while stack:

        # pop(0) would be O(n), so we pop from the END
        # and reverse the result at the very end instead.
        item = stack.pop()

        if isinstance(item, (list, tuple)):
            # Push the children back on to be processed.
            stack.extend(item)
        else:
            flat.append(item)

    # We consumed the list back to front, so flip it.
    return flat[::-1]


print(flatten([1, [2, [3, 4], 5], 6]))
# Output:
# [1, 2, 3, 4, 5, 6]

print(flatten([1, [2, (3, [4])]]))
# Output:
# [1, 2, 3, 4]

print(flatten_iterative([1, [2, [3, 4], 5], 6]))
# Output:
# [1, 2, 3, 4, 5, 6]
