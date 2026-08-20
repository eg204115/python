# QUESTION
# What is a decorator? Write one that measures how long
# a function takes.
#
# ANSWER
# A decorator is just a function that TAKES a function
# and RETURNS a replacement for it.
#
#   @my_decorator
#   def greet(): ...
#
# is exactly the same as writing:
#
#   greet = my_decorator(greet)

import functools
import time


def timer(func):

    # @functools.wraps copies the original function's
    # name, docstring and signature onto the wrapper.
    #
    # WITHOUT it, greet.__name__ would report "wrapper",
    # which breaks debugging, logging and help().
    # Interviewers very often ask about this line.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        # *args/**kwargs let the wrapper accept ANY
        # arguments and pass them straight through,
        # so one decorator works on any function.
        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")

        # Returning the result matters. Forgetting this
        # line silently turns every decorated function
        # into one that returns None.
        return result

    return wrapper


@timer
def slow_add(a, b):
    """Add two numbers, slowly."""
    time.sleep(0.1)
    return a + b


print(slow_add(2, 3))
# Output:
# slow_add took 0.1...s
# 5

print(slow_add.__name__)
# Output:
# slow_add
#
# Thanks to @functools.wraps. Without it: "wrapper".


# A DECORATOR THAT TAKES ARGUMENTS
#
# This needs THREE layers, which is the part people
# get stuck on:
#
#   outer  - receives the decorator's arguments
#   middle - receives the function
#   inner  - receives the call's arguments


def repeat(times):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return decorator


@repeat(times=3)
def greet(name):
    return f"Hi {name}"


print(greet("Nethmi"))
# Output:
# ['Hi Nethmi', 'Hi Nethmi', 'Hi Nethmi']


# WHERE YOU MEET THEM
#
# @property, @staticmethod, @classmethod,
# @functools.lru_cache, and most web framework routes
# (@app.route) are all just decorators.
