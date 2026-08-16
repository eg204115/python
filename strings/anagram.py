from collections import Counter


def is_anagram(s1, s2):

    # replace(" ", "") removes spaces.
    #
    # Example:
    # "hello world"
    # becomes
    # "helloworld"
    clean_s1 = s1.replace(" ", "").lower()
    clean_s2 = s2.replace(" ", "").lower()

    # Counter counts the characters.
    #
    # == compares whether the two Counter objects
    # contain the same character counts.
    return Counter(clean_s1) == Counter(clean_s2)


print(is_anagram("listen", "silent"))
# True

print(is_anagram("hello", "world"))
# False