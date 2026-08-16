from collections import Counter


def word_frequency(sentence):

    # lower() converts the string to lowercase.
    #
    # "Python IS Easy"
    # becomes
    # "python is easy"
    sentence = sentence.lower()

    # split() divides a string into a list of words.
    #
    # "python is easy"
    #
    # becomes:
    # ["python", "is", "easy"]
    words = sentence.split()

    # Counter counts how many times
    # each word appears.
    return Counter(words)


sentence = "Python is easy and Python is powerful"

print(word_frequency(sentence))