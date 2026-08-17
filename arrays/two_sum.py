def two_sum(numbers, target):

    # Create an empty dictionary.
    #
    # We will store:
    #
    # number → index
    #
    # Example:
    # {2: 0, 7: 1}
    seen = {}

    # enumerate() gives us BOTH:
    #
    # index
    # value
    #
    # Example:
    #
    # numbers = [2, 7, 11]
    #
    # enumerate(numbers) gives:
    # (0, 2)
    # (1, 7)
    # (2, 11)
    for i, number in enumerate(numbers):

        # Calculate what number we need
        # to reach the target.
        #
        # target = 9
        # number = 7
        #
        # complement = 9 - 7
        #             = 2
        complement = target - number

        # Check whether the required number
        # already exists in our dictionary.
        if complement in seen:

            # seen[complement] gives the index
            # where the complement was found.
            #
            # i is the current index.
            return [seen[complement], i]

        # Store the current number and its index.
        #
        # Example:
        # seen[2] = 0
        seen[number] = i

    # If no pair is found,
    # return an empty list.
    return []


print(two_sum([2, 7, 11, 15], 9))
# Output:
# [0, 1]