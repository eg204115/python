def find_duplicates(numbers):

    # set() creates an empty set.
    #
    # A set stores unique values.
    seen = set()

    # Another set to store duplicate numbers.
    duplicates = set()

    # Loop through every number in the list.
    for number in numbers:

        # "in" checks whether a value exists
        # inside a collection.
        if number in seen:

            # If the number already exists in seen,
            # it is a duplicate.
            duplicates.add(number)

        else:

            # If we haven't seen it before,
            # add it to seen.
            seen.add(number)

    # list() converts the set into a list.
    return list(duplicates)


print(find_duplicates([1, 2, 3, 2, 4, 5, 3, 6]))
# Output:
# [2, 3]