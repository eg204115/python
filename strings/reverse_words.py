# QUESTION
# Reverse the ORDER of the words in a sentence.
# The letters inside each word stay the same.
# Collapse any extra spaces.
#
# Example:
#   "  the sky   is blue  "  ->  "blue is sky the"
#
# ANSWER
# split() already handles the messy spacing for us.


def reverse_words(sentence):

    # split() with NO argument is the trick here.
    #
    # It splits on ANY run of whitespace and
    # throws away the empty pieces.
    #
    #   "  the sky   is blue  ".split()
    #   ->  ['the', 'sky', 'is', 'blue']
    #
    # Note the difference:
    #   "a  b".split(" ")  ->  ['a', '', 'b']   (empty string!)
    #   "a  b".split()     ->  ['a', 'b']
    words = sentence.split()

    # [::-1] is slice notation:
    #   start : stop : step
    #
    # A step of -1 walks the list backwards,
    # producing a reversed COPY.
    reversed_words = words[::-1]

    # " ".join(list) glues the items together
    # using a single space between each one.
    return " ".join(reversed_words)


print(reverse_words("  the sky   is blue  "))
# Output:
# blue is sky the

print(reverse_words("hello world"))
# Output:
# world hello
