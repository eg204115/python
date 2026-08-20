# QUESTION
# Check whether a string is a palindrome,
# ignoring case, spaces and punctuation.
#
# Example:
#   "A man, a plan, a canal: Panama"  ->  True
#   "race a car"                      ->  False
#
# ANSWER
# Clean the string first, then compare it
# against its own reverse.


def is_palindrome(text):

    # Keep only letters and digits, and lowercase them.
    #
    # ch.isalnum() is True for letters and numbers,
    # and False for spaces, commas, colons, etc.
    #
    # This is a list comprehension: it builds a new
    # list by looping and filtering in one line.
    #
    #   "A man!"  ->  ['a', 'm', 'a', 'n']
    cleaned = [ch.lower() for ch in text if ch.isalnum()]

    # cleaned[::-1] is the reversed copy.
    #
    # Comparing the list to its reverse answers
    # the question directly.
    return cleaned == cleaned[::-1]


def is_palindrome_two_pointer(text):

    # The same question, solved the way an interviewer
    # often wants: no extra reversed copy.

    cleaned = [ch.lower() for ch in text if ch.isalnum()]

    # left starts at the front, right at the back.
    left = 0
    right = len(cleaned) - 1

    # Walk both pointers toward the middle.
    while left < right:

        # One mismatch is enough to fail.
        if cleaned[left] != cleaned[right]:
            return False

        left += 1
        right -= 1

    # The pointers met without a mismatch.
    return True


print(is_palindrome("A man, a plan, a canal: Panama"))
# Output:
# True

print(is_palindrome("race a car"))
# Output:
# False

print(is_palindrome_two_pointer("A man, a plan, a canal: Panama"))
# Output:
# True
