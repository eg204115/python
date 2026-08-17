def missing_number(numbers):

    # len() returns the number of elements.
    #
    # [3, 0, 1]
    #
    # len = 3
    n = len(numbers)

    # Formula for the sum of numbers from 0 to n:
    #
    # n * (n + 1) // 2
    #
    # // means integer division.
    expected_sum = n * (n + 1) // 2

    # sum() adds all values in the list.
    actual_sum = sum(numbers)

    # The difference is the missing number.
    return expected_sum - actual_sum


print(missing_number([3, 0, 1]))
# Output:
# 2