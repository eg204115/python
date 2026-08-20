# QUESTION
# What do *args and **kwargs mean?
# What is the difference between using them in a
# function DEFINITION and in a function CALL?
#
# ANSWER
# In a DEFINITION they COLLECT extra arguments.
# In a CALL they UNPACK a collection into arguments.
#
# The names args/kwargs are only convention - the
# * and ** are what actually matter.


def show(*args, **kwargs):

    # *args collects extra POSITIONAL arguments
    # into a TUPLE.
    #
    # **kwargs collects extra KEYWORD arguments
    # into a DICT.
    print("args:", args)
    print("kwargs:", kwargs)


show(1, 2, 3, name="Nethmi", role="engineer")
# Output:
# args: (1, 2, 3)
# kwargs: {'name': 'Nethmi', 'role': 'engineer'}


# UNPACKING - the same symbols, the other direction.

def add(a, b, c):
    return a + b + c


numbers = [1, 2, 3]

# *numbers spreads the list into three separate
# arguments: add(1, 2, 3).
print(add(*numbers))
# Output:
# 6

values = {"a": 1, "b": 2, "c": 3}

# **values spreads the dict into keyword arguments:
# add(a=1, b=2, c=3).
#
# The dict keys MUST match the parameter names.
print(add(**values))
# Output:
# 6


# ARGUMENT ORDER
#
# The order in a definition is fixed:
#
#   def f(positional, *args, keyword_only, **kwargs)
#
# Anything written AFTER *args can only be passed by
# keyword - it can never be filled positionally,
# because *args has already swallowed the extras.

def report(title, *rows, separator=" | ", **options):
    line = separator.join(str(row) for row in rows)
    return f"{title}: {line} {options}"


print(report("Totals", 10, 20, 30, separator=" + ", debug=True))
# Output:
# Totals: 10 + 20 + 30 {'debug': True}


# WHY IT MATTERS
#
# *args/**kwargs are how you write a wrapper that
# forwards arguments to a function without knowing
# that function's signature - which is exactly what
# decorators do.
