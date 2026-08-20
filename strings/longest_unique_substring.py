# QUESTION
# Find the length of the longest substring
# that contains NO repeated characters.
#
# Example:
#   "abcabcbb"  ->  3   (the substring "abc")
#   "bbbbb"     ->  1   (the substring "b")
#   "pwwkew"    ->  3   (the substring "wke")
#
# ANSWER
# Sliding window. The window is the stretch of text
# between `start` and the current position, and we
# guarantee it never contains a duplicate.
#
# O(n) time - each character is visited once.


def longest_unique_substring(text):

    # last_seen maps:  character -> the index we last saw it at
    last_seen = {}

    # start is the LEFT edge of the current window.
    start = 0

    longest = 0

    # i is the RIGHT edge of the window.
    for i, ch in enumerate(text):

        # Have we seen this character INSIDE the
        # current window?
        #
        # Both conditions matter:
        #   - the character exists in last_seen at all
        #   - and that sighting is at or after `start`,
        #     meaning it is still inside the window
        if ch in last_seen and last_seen[ch] >= start:

            # Shrink the window from the left so the
            # duplicate falls outside it.
            #
            # Example on "abca", at the second 'a':
            #   last_seen['a'] = 0
            #   start becomes 1, so the window is "bca"
            start = last_seen[ch] + 1

        # Record where we just saw this character.
        last_seen[ch] = i

        # The current window is text[start .. i],
        # so its length is i - start + 1.
        current_length = i - start + 1

        longest = max(longest, current_length)

    return longest


print(longest_unique_substring("abcabcbb"))
# Output:
# 3

print(longest_unique_substring("bbbbb"))
# Output:
# 1

print(longest_unique_substring("pwwkew"))
# Output:
# 3
