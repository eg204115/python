# QUESTION
# Group words that are anagrams of each other.
#
# Example:
#   ["eat", "tea", "tan", "ate", "nat", "bat"]
#   ->
#   [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
#
# ANSWER
# Anagrams share the same letters, so if we SORT the
# letters of each word we get a key that is identical
# for every member of the group.
#
#   "eat" -> "aet"
#   "tea" -> "aet"
#   "ate" -> "aet"
#
# Then it is just a dictionary of key -> list of words.

from collections import defaultdict


def group_anagrams(words):

    # defaultdict(list) means:
    # "if a key is missing, create an empty list for it".
    #
    # Without it we would need this every time:
    #
    #   if key not in groups:
    #       groups[key] = []
    #
    # defaultdict removes that boilerplate.
    groups = defaultdict(list)

    for word in words:

        # sorted(word) returns a LIST of characters:
        #   sorted("eat")  ->  ['a', 'e', 't']
        #
        # A list cannot be a dictionary key because it
        # is mutable, so we join it back into a string.
        #
        #   "".join(['a', 'e', 't'])  ->  "aet"
        key = "".join(sorted(word))

        groups[key].append(word)

    # groups.values() gives the lists of grouped words.
    # We wrap it in list() to return a plain list.
    return list(groups.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output:
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
