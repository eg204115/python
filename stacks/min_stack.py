# QUESTION
# Design a stack that supports push, pop, top
# and get_min - where get_min() returns the smallest
# value currently in the stack.
#
# All four operations must run in O(1).
#
# ANSWER
# The trap is scanning the stack to find the minimum,
# which would be O(n).
#
# Instead we keep a SECOND stack that remembers what
# the minimum was at each point in time. Popping the
# main stack pops that history too.


class MinStack:

    def __init__(self):

        # The real stack of values.
        self.items = []

        # mins[-1] is always the minimum of the
        # values currently in self.items.
        self.mins = []

    def push(self, value):

        self.items.append(value)

        # The new minimum is either the value we just
        # pushed, or the minimum we already had.
        #
        # If mins is empty this is the first value,
        # so it is the minimum by default.
        if not self.mins:
            self.mins.append(value)
        else:
            self.mins.append(min(value, self.mins[-1]))

    def pop(self):

        if not self.items:
            return None

        # Pop BOTH stacks so the two stay in step.
        # This is what makes the history correct.
        self.mins.pop()

        # list.pop() with no argument removes and
        # returns the LAST item.
        return self.items.pop()

    def top(self):

        # [-1] means "the last item", which is the
        # top of the stack.
        if not self.items:
            return None

        return self.items[-1]

    def get_min(self):

        # O(1) - we just read the answer we stored.
        if not self.mins:
            return None

        return self.mins[-1]


stack = MinStack()
stack.push(5)
stack.push(2)
stack.push(7)

print(stack.get_min())
# Output:
# 2

stack.pop()
print(stack.get_min())
# Output:
# 2

stack.pop()
print(stack.get_min())
# Output:
# 5
