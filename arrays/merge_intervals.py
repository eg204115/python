# QUESTION
# Given a list of intervals [start, end],
# merge all the overlapping ones.
#
# Example:
#   [[1, 3], [2, 6], [8, 10], [15, 18]]
#   ->
#   [[1, 6], [8, 10], [15, 18]]
#
#   [1, 3] and [2, 6] overlap because 2 <= 3,
#   so they become [1, 6].
#
# ANSWER
# Sort by start time, then sweep through once.
# O(n log n) because of the sort.


def merge_intervals(intervals):

    if not intervals:
        return []

    # Sort by the START of each interval.
    #
    # key=lambda pair: pair[0] tells sorted()
    # to compare using the first element.
    #
    # Sorting is what makes the sweep work:
    # once sorted, an interval can only ever
    # overlap the one directly before it.
    intervals = sorted(intervals, key=lambda pair: pair[0])

    # merged holds the finished result.
    # We seed it with the first interval.
    #
    # list(...) makes a copy so we never
    # modify the caller's data.
    merged = [list(intervals[0])]

    for start, end in intervals[1:]:

        # last is the most recently added interval.
        # We may still be able to stretch it.
        last = merged[-1]

        # Overlap test.
        #
        # last = [1, 3], current = [2, 6]
        # start (2) <= last[1] (3)  ->  they overlap
        if start <= last[1]:

            # Stretch the end of the previous interval.
            #
            # max() matters for a nested interval:
            # [1, 10] then [2, 3] must stay [1, 10].
            last[1] = max(last[1], end)

        else:
            # No overlap, so this interval starts
            # a brand new block.
            merged.append([start, end])

    return merged


print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
# Output:
# [[1, 6], [8, 10], [15, 18]]

print(merge_intervals([[1, 10], [2, 3]]))
# Output:
# [[1, 10]]
