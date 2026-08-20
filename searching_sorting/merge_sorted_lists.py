# QUESTION
# Merge two already-sorted lists into one sorted list.
# Do it in O(n + m) - do NOT just concatenate and sort,
# which would throw away the fact they are sorted.
#
# Example:
#   [1, 3, 5] and [2, 4, 6]  ->  [1, 2, 3, 4, 5, 6]
#
# ANSWER
# Two pointers, one per list. This is also the merge
# step inside merge sort.

import heapq


def merge_sorted(a, b):

    merged = []

    # i walks list a, j walks list b.
    i = 0
    j = 0

    # Keep going while BOTH lists still have items.
    while i < len(a) and j < len(b):

        # Take the smaller head value.
        #
        # <= rather than < keeps the merge STABLE:
        # when values tie, the item from `a` goes first.
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # One list is now exhausted. The other may still
    # have items, and they are all bigger, so they
    # can be appended as they are.
    #
    # Slicing past the end is safe in Python:
    # [1,2,3][5:] gives [] instead of an error.
    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged


def merge_sort(numbers):

    # Full merge sort, built on the merge above.
    # O(n log n).

    # BASE CASE - a list of 0 or 1 items is sorted.
    if len(numbers) <= 1:
        return list(numbers)

    # Split down the middle.
    mid = len(numbers) // 2

    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    # Sort each half, then merge the two sorted halves.
    return merge_sorted(left, right)


print(merge_sorted([1, 3, 5], [2, 4, 6]))
# Output:
# [1, 2, 3, 4, 5, 6]

print(merge_sort([5, 2, 9, 1, 5, 6]))
# Output:
# [1, 2, 5, 5, 6, 9]

# The standard library also merges any number of sorted
# inputs lazily, which is the practical answer for
# large files that do not fit in memory.
print(list(heapq.merge([1, 3, 5], [2, 4, 6], [0, 7])))
# Output:
# [0, 1, 2, 3, 4, 5, 6, 7]
