# QUESTION
# Return every possible ordering (permutation)
# of the items in a list.
#
# Example:
#   [1, 2, 3]
#   ->
#   [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
#
# ANSWER
# Backtracking: pick each item as the first element,
# then permute whatever is left.
#
# There are n! permutations, so this is O(n * n!) -
# unavoidable, because that is the size of the output.


def permutations(items):

    # BASE CASE.
    #
    # A list of 0 or 1 items has exactly one ordering.
    # This is what stops the recursion.
    if len(items) <= 1:
        return [list(items)]

    result = []

    for i in range(len(items)):

        # Take this item out to be the first element.
        chosen = items[i]

        # Everything EXCEPT position i.
        #
        # Slicing:
        #   items[:i]     -> everything before i
        #   items[i+1:]   -> everything after i
        #
        # On [1, 2, 3] with i = 1:
        #   [1] + [3]  ->  [1, 3]
        remaining = items[:i] + items[i + 1:]

        # Recursively order what is left, and put
        # the chosen item in front of each result.
        for rest in permutations(remaining):
            result.append([chosen] + rest)

    return result


print(permutations([1, 2, 3]))
# Output:
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

print(len(permutations([1, 2, 3, 4])))
# Output:
# 24
