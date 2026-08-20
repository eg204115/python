# QUESTION
# What does this print, and why?
#
#   def add_item(item, basket=[]):
#       basket.append(item)
#       return basket
#
#   print(add_item("apple"))
#   print(add_item("banana"))
#
# ANSWER
# ['apple']
# ['apple', 'banana']       <- surprising!
#
# Default arguments are evaluated ONCE, when the
# function is DEFINED - not each time it is called.
#
# So every call that relies on the default shares the
# SAME list object. This is one of the most commonly
# asked Python gotchas.


def add_item_buggy(item, basket=[]):

    # basket is the same list object on every call.
    basket.append(item)
    return basket


print(add_item_buggy("apple"))
# Output:
# ['apple']

print(add_item_buggy("banana"))
# Output:
# ['apple', 'banana']


# THE FIX
#
# Use None as the default, and build a fresh list
# inside the function body.


def add_item_fixed(item, basket=None):

    # None is immutable and shared safely.
    #
    # `if basket is None` rather than `if not basket`,
    # because an empty list passed in on purpose
    # should still be used, not replaced.
    if basket is None:
        basket = []

    basket.append(item)
    return basket


print(add_item_fixed("apple"))
# Output:
# ['apple']

print(add_item_fixed("banana"))
# Output:
# ['banana']


# The same trap applies to any MUTABLE default:
# lists, dicts, sets.
#
# Immutable defaults (int, str, tuple, None) are safe,
# because they cannot be changed in place.
