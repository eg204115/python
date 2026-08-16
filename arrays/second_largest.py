def second_largest(numbers):

    # set(numbers) removes duplicate values.
    #
    # Example:
    # [10, 5, 8, 10, 3, 8]
    #
    # becomes:
    # {10, 5, 8, 3}
    unique_numbers = set(numbers)

    # len() gives the number of items.
    #
    # If there are fewer than 2 unique numbers,
    # we cannot find a second largest number.
    if len(unique_numbers) < 2:
        return None

    # sorted() sorts the values.
    #
    # reverse=True means sort from largest to smallest.
    #
    # Example:
    # [10, 8, 5, 3]
    sorted_numbers = sorted(
        unique_numbers,
        reverse=True
    )

    # Indexing starts from 0.
    #
    # sorted_numbers[0] -> largest
    # sorted_numbers[1] -> second largest
    return sorted_numbers[1]


print(second_largest([10, 5, 8, 10, 3, 8]))
# Output:
# 8