# QUESTION
# What is the difference between a list comprehension
# and a generator expression?
# When would you choose a generator?
#
# ANSWER
# A list comprehension [ ... ] builds the WHOLE list in
# memory immediately.
#
# A generator expression ( ... ) is LAZY - it produces
# values one at a time, only when asked, and stores
# nothing.

import sys


# The only visible difference is the brackets.
as_list = [n * n for n in range(10)]
as_generator = (n * n for n in range(10))

print(as_list[:5])
# Output:
# [0, 1, 4, 9, 16]

print(as_generator)
# Output:
# <generator object <genexpr> at 0x...>
#
# Nothing has been computed yet.

print(list(as_generator)[:5])
# Output:
# [0, 1, 4, 9, 16]


# MEMORY - the reason generators exist.

big_list = [n for n in range(100000)]
big_gen = (n for n in range(100000))

print(sys.getsizeof(big_list) > 100000)
# Output:
# True
#
# The list really does hold 100,000 items.

print(sys.getsizeof(big_gen) < 500)
# Output:
# True
#
# The generator is a few hundred bytes no matter how
# many values it will eventually produce.


# A GENERATOR IS EXHAUSTED AFTER ONE PASS.
#
# This catches people out constantly.

gen = (n for n in range(3))

print(list(gen))
# Output:
# [0, 1, 2]

print(list(gen))
# Output:
# []
#
# The values are gone. A list can be looped over
# as many times as you like; a generator cannot.


# WRITING ONE WITH yield.

def read_in_batches(items, size):

    # yield turns a function into a generator.
    #
    # Execution PAUSES at each yield and resumes from
    # that exact point on the next request - so we never
    # hold more than one batch in memory.
    batch = []

    for item in items:
        batch.append(item)

        if len(batch) == size:
            yield batch
            batch = []

    # Do not lose the final partial batch.
    if batch:
        yield batch


print(list(read_in_batches([1, 2, 3, 4, 5], 2)))
# Output:
# [[1, 2], [3, 4], [5]]


# WHEN TO CHOOSE WHICH
#
# Generator: large or infinite data, streaming a file,
#            you only need one pass.
#
# List:      you need len(), indexing, or more than
#            one pass over the data.
