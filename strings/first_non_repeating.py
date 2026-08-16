# Counter is a class from Python's collections module.
# It counts how many times each item appears.
from collections import Counter


# def is used to define a function.
# s is the parameter (input) of the function.
def first_non_repeating(s):

    # Counter(s) counts each character in the string.
    #
    # Example:
    # "swiss"
    #
    # Counter becomes:
    # {'s': 3, 'w': 1, 'i': 1}
    count = Counter(s)

    # for char in s:
    # Take each character from s one by one.
    #
    # First char = 's'
    # Second char = 'w'
    # Third char = 'i'
    # ...
    for char in s:

        # count[char] gets the number of times
        # the current character appears.
        #
        # == means "is equal to"
        if count[char] == 1:

            # return immediately stops the function
            # and sends the value back.
            return char

    # If no non-repeating character was found,
    # return None.
    #
    # None means "no value".
    return None


print(first_non_repeating("swiss"))
# Output:
# w