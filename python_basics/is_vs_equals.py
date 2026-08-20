# QUESTION
# What is the difference between `is` and `==`?
# When would they disagree?
#
# ANSWER
# == compares VALUES  ("are these equal?")
# is compares IDENTITY ("are these the exact same object
#                        in memory?")


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
# Output:
# True
#
# Same contents.

print(a is b)
# Output:
# False
#
# Two separate list objects that happen to look alike.

print(id(a) == id(b))
# Output:
# False
#
# id() shows the identity `is` actually compares.


# THE CONFUSING PART - CPython caches small integers.
#
# Careful: two identical literals written in the SAME
# block of code are folded into one shared constant by
# the compiler, so this prints True for ANY value and
# tells us nothing:
#
#   x = 1000
#   y = 1000
#   x is y      ->  True
#
# To see the real behaviour we have to build the numbers
# at runtime, where the compiler cannot fold them.

small_1 = int("256")
small_2 = int("256")
print(small_1 is small_2)
# Output:
# True
#
# CPython pre-creates the integers -5 to 256 and reuses
# them, so both names land on the same cached object.

big_1 = int("1000")
big_2 = int("1000")
print(big_1 is big_2)
# Output:
# False
#
# 1000 is outside the cached range, so these really are
# two separate objects that merely compare equal.

print(big_1 == big_2)
# Output:
# True

# The cache is a CPython implementation detail, NOT a
# language rule. That is exactly why you must never use
# `is` to compare values - it can appear to work on small
# numbers and then quietly break on larger ones.


# WHERE `is` IS CORRECT
#
# Use it for singletons - objects there is only ever
# one of: None, True, False.

value = None

print(value is None)
# Output:
# True
#
# `is None` is the idiomatic check. Prefer it over
# `== None`, because a custom class can override __eq__
# and make `== None` return anything it likes.
