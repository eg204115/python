# QUESTION
# What is the difference between assignment,
# a shallow copy, and a deep copy?
#
# ANSWER
# - Assignment copies the REFERENCE. Both names point
#   at the same object.
# - A shallow copy makes a new outer object, but the
#   items INSIDE are still shared.
# - A deep copy recursively copies everything.

import copy


# 1. ASSIGNMENT - not a copy at all.

original = [1, 2, 3]
alias = original

alias.append(4)

print(original)
# Output:
# [1, 2, 3, 4]
#
# Changing `alias` changed `original`, because both
# names refer to one single list.

print(original is alias)
# Output:
# True


# 2. SHALLOW COPY - new outer list, shared inner objects.

nested = [[1, 2], [3, 4]]

# All three of these make a SHALLOW copy:
#   nested.copy()
#   nested[:]
#   list(nested)
shallow = nested.copy()

# Replacing a whole element is fine - the outer
# lists are genuinely separate.
shallow.append([5, 6])
print(len(nested), len(shallow))
# Output:
# 2 3

# But MUTATING an inner list is visible in both,
# because the inner lists were never copied.
shallow[0].append(99)

print(nested)
# Output:
# [[1, 2, 99], [3, 4]]


# 3. DEEP COPY - everything is copied, all the way down.

nested2 = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested2)

deep[0].append(99)

print(nested2)
# Output:
# [[1, 2], [3, 4]]
#
# The original is untouched.

print(deep)
# Output:
# [[1, 2, 99], [3, 4]]


# RULE OF THUMB
#
# A shallow copy is enough when the contents are
# immutable (numbers, strings, tuples).
#
# Reach for deepcopy only when you have nested mutable
# data - it is slower and can be surprisingly expensive
# on large structures.
