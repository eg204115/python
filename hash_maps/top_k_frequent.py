from collections import Counter


def top_k_frequent(numbers, k):

    # Count how many times each number appears.
    #
    # Example:
    #
    # [1, 1, 1, 2, 2, 3]
    #
    # becomes:
    #
    # {
    #     1: 3,
    #     2: 2,
    #     3: 1
    # }
    count = Counter(numbers)

    # most_common(k) returns the k most frequent
    # elements.
    #
    # Example:
    #
    # count.most_common(2)
    #
    # gives:
    #
    # [(1, 3), (2, 2)]
    #
    # Each tuple contains:
    # (number, frequency)
    frequent = count.most_common(k)

    # List comprehension.
    #
    # for number, frequency in frequent
    # extracts each tuple.
    #
    # We only want number.
    return [number for number, frequency in frequent]


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
# Output:
# [1, 2]