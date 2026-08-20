# QUESTION
# Write a function that returns the nth Fibonacci number.
# Then make it fast.
#
#   0, 1, 1, 2, 3, 5, 8, 13, ...
#
# ANSWER
# The plain recursive version is the classic interview
# trap: it recomputes the same values over and over and
# runs in roughly O(2^n).
#
# Three versions below, slowest to fastest.

from functools import lru_cache


def fib_slow(n):

    # The naive definition.
    #
    # fib(5) calls fib(4) and fib(3),
    # fib(4) calls fib(3) again... and so on.
    # The same work is repeated exponentially.
    if n < 2:
        return n

    return fib_slow(n - 1) + fib_slow(n - 2)


def fib_memo(n, cache=None):

    # MEMOISATION - remember answers we already computed.
    #
    # Note the default is None, not {}.
    # A mutable default argument like cache={} would be
    # SHARED across every call, which is a well known
    # Python bug (see python_basics/mutable_default_argument.py).
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    if n < 2:
        return n

    # Compute once, then store it.
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    return cache[n]


@lru_cache(maxsize=None)
def fib_cached(n):

    # The same idea, but Python does the caching for us.
    #
    # @lru_cache stores the result for each argument it
    # has already seen, turning the exponential version
    # into a linear one with one decorator line.
    if n < 2:
        return n

    return fib_cached(n - 1) + fib_cached(n - 2)


def fib_loop(n):

    # No recursion at all - usually the answer an
    # interviewer is happiest with.
    #
    # O(n) time, O(1) space.
    a, b = 0, 1

    for _ in range(n):
        # Swap in one line: a becomes b, b becomes a + b.
        a, b = b, a + b

    return a


print(fib_slow(10))
# Output:
# 55

print(fib_memo(50))
# Output:
# 12586269025

print(fib_cached(50))
# Output:
# 12586269025

print(fib_loop(50))
# Output:
# 12586269025
