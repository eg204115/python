def is_valid_parentheses(s):

    # Create an empty list.
    #
    # We will use this list as a STACK.
    stack = []

    # Dictionary containing matching brackets.
    #
    # Key   → closing bracket
    # Value → opening bracket
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # Go through every character.
    for char in s:

        # Check whether the character is
        # an opening bracket.
        if char in "([{":

            # append() adds an item
            # to the end of the list.
            #
            # This is PUSH in a stack.
            stack.append(char)

        # Otherwise, check if it is a closing bracket.
        elif char in ")]}":

            # stack[-1] means:
            # get the LAST element.
            #
            # not stack means:
            # the stack is empty.
            #
            # OR condition:
            # either condition can be True.
            if not stack or stack[-1] != pairs[char]:

                # Invalid parentheses.
                return False

            # pop() removes the last element.
            #
            # This is POP in a stack.
            stack.pop()

    # If stack is empty,
    # all brackets were correctly matched.
    #
    # len(stack) == 0 produces True/False.
    return len(stack) == 0


print(is_valid_parentheses("()[]{}"))
# True

print(is_valid_parentheses("([)]"))
# False