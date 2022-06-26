# sorted(iterable, *, key=None, reverse=False)
# Return a new sorted list from the items in iterable.
# Has two optional arguments which must be specified as keyword arguments.

# key specifies a function of one argument that is used to extract a comparison key from each element
# in iterable (for example, key=str.lower). The default value is None (compare the elements directly).

# reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.


# list.sort(*, key=None, reverse=False)
# Sort the items of the list in place
# (the arguments can be used for sort customization, see sorted() for their explanation).

# If a key function is given, apply it once to each list item and sort them,
# ascending or descending, according to their function values.

# The reverse flag can be set to sort in descending order.

letters = ['d', 'a', 'c', 'b', 'f', 'g', 'e']
letters2 = ['d', 'a', 'c', 'b', 'f', 'g', 'e']

letters.sort()  # sort in place in ASC order
sorted(letters2)

newSortedList = sorted(letters2, reverse=True)  # sort in DESC order

print(letters)
print(letters2)  # letters2 not affected since sorted returns a new sorted list
print("SORT DESC", newSortedList)


sortStringWithKeyLowercase = sorted("This is a test string from Andrew".split(), key=str.lower)

print(sortStringWithKeyLowercase)


# Say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd' ,'wa']


# Write a little function that takes a string, and returns its last letter.
# This will be the key function (takes in 1 value, returns 1 value).
def my_fn(s):
    return s[-1]


# Now pass key=my_fn to sorted() to sort by the last letter:
sortedByLastLetterInWord = sorted(strs, key=my_fn)
print(sortedByLastLetterInWord)  # ['wa', 'zb', 'xc', 'yd']
