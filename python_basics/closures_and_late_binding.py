# QUESTION
# What does this print?
#
#   functions = []
#   for i in range(3):
#       functions.append(lambda: i)
#   print([f() for f in functions])
#
# ANSWER
# [2, 2, 2]  - not [0, 1, 2].
#
# This is the LATE BINDING closure trap, and it is one
# of the most frequently asked Python interview
# questions.


# WHAT A CLOSURE IS
#
# A closure is a function that remembers variables from
# the scope where it was DEFINED, even after that scope
# has finished running.

def make_counter():

    count = 0

    def increment():

        # `nonlocal` is required to REBIND a variable
        # from the enclosing function.
        #
        # Without it, `count = count + 1` would create a
        # brand new local variable and raise
        # UnboundLocalError.
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()
print(counter(), counter(), counter())
# Output:
# 1 2 3
#
# `count` survived after make_counter() returned,
# because increment closed over it.


# THE TRAP
#
# A closure captures the VARIABLE, not the variable's
# value at the moment of definition.

functions = []

for i in range(3):
    functions.append(lambda: i)

print([f() for f in functions])
# Output:
# [2, 2, 2]
#
# All three lambdas share the SAME `i`. By the time
# they are finally called, the loop has ended and
# i is 2.


# FIX 1 - a default argument.
#
# Default arguments are evaluated at DEFINITION time,
# so this snapshots the current value of i.

functions = []

for i in range(3):
    functions.append(lambda i=i: i)

print([f() for f in functions])
# Output:
# [0, 1, 2]


# FIX 2 - a factory function.
#
# Each call to make_func creates a NEW scope with its
# own `value`, so there is nothing shared to overwrite.
# This is clearer than the default-argument trick.

def make_func(value):
    return lambda: value


functions = [make_func(i) for i in range(3)]

print([f() for f in functions])
# Output:
# [0, 1, 2]
