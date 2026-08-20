# QUESTION
# Given a list of dictionaries (rows of data),
# sort them by a field. Then sort by two fields,
# one ascending and one descending.
#
# This one comes up constantly in data-focused
# interviews because it is real day-to-day work.
#
# ANSWER
# sorted() with a key function.

from operator import itemgetter

people = [
    {"name": "Nimal", "age": 32, "city": "Kandy"},
    {"name": "Amara", "age": 25, "city": "Colombo"},
    {"name": "Kasun", "age": 32, "city": "Colombo"},
]


# SORT BY ONE FIELD.
#
# key= takes a function that is called on each item,
# and the RETURN value is what gets compared.
#
# So key=lambda person: person["age"] means
# "compare these dictionaries by their age".
by_age = sorted(people, key=lambda person: person["age"])

print([p["name"] for p in by_age])
# Output:
# ['Amara', 'Nimal', 'Kasun']


# itemgetter("age") does the same thing as the lambda
# above, and is slightly faster because it is C code.
by_age_2 = sorted(people, key=itemgetter("age"))

print([p["name"] for p in by_age_2])
# Output:
# ['Amara', 'Nimal', 'Kasun']


# SORT BY TWO FIELDS.
#
# Returning a TUPLE compares the first element first,
# and only uses the second to break ties.
#
# Here: city ascending, then name ascending.
by_city_then_name = sorted(
    people,
    key=lambda person: (person["city"], person["name"]),
)

print([(p["city"], p["name"]) for p in by_city_then_name])
# Output:
# [('Colombo', 'Amara'), ('Colombo', 'Kasun'), ('Kandy', 'Nimal')]


# MIXED DIRECTIONS - the tricky follow-up.
#
# reverse=True would flip BOTH fields, which is not
# what we want.
#
# For a NUMBER, negating it flips just that one field.
# Here: age descending, then name ascending.
by_age_desc_name_asc = sorted(
    people,
    key=lambda person: (-person["age"], person["name"]),
)

print([(p["age"], p["name"]) for p in by_age_desc_name_asc])
# Output:
# [(32, 'Kasun'), (32, 'Nimal'), (25, 'Amara')]


# For a STRING you cannot negate, so sort twice instead.
# Python's sort is STABLE, meaning equal items keep their
# relative order - so sort by the secondary key FIRST,
# then by the primary key.
stable_two_pass = sorted(people, key=itemgetter("name"))
stable_two_pass = sorted(stable_two_pass, key=itemgetter("city"), reverse=True)

print([(p["city"], p["name"]) for p in stable_two_pass])
# Output:
# [('Kandy', 'Nimal'), ('Colombo', 'Amara'), ('Colombo', 'Kasun')]
