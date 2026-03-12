# largest number in a list
def largest_number(lst):
    if not lst:
        return None
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

# count vowels in a string
def count_vowels(s):   
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count    

# Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# Find the second largest number in a list
def second_largest(lst):
    if len(lst) < 2:
        return None
    first = second = float('-inf') # Assign negative infinity to handle cases with negative numbers
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

# Merge 2 dictionaries
dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}

merged = {**dict1, **dict2}

print(merged)
# Find the missing number in a list of consecutive numbers

def missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)

print(missing_number([1,2,3,5]))