# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# An OrderedDictionary is a dictionary subclass that remembers the order that keys were first inserted.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

# From Python's perspective, dictionaries are defined as objects with the data type 'dict': <class 'dict'>

dictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# get value
accessMethod1 = dictionary["brand"]
accessMethod2 = dictionary.get("brand")
print(accessMethod1)
print(accessMethod2)

# return a list of keys
listOfKeys = dictionary.keys()

# return a list of values
listOfValues = dictionary.values()

print("listOfKeys: " + str(listOfKeys))
print("listOfValues:", listOfValues)

# Update key value
dictionary["brand"] = "Toyota"
dictionary["model"] = "Corolla"

# The update() method will update the dictionary with the items from a given argument.
dictionary.update({ "year": 2020 }) # If the item does not exist, the item will be added.



# add a value to dictionary
dictionary["price"] = 30000
print(dictionary)

# items method - Get a list of the key:value pairs
# will return each item in a dictionary, as tuples in a list.

print(dictionary.items()) # dict_items([('brand', 'Toyota'), ('model', 'Corolla'), ('year', 1964), ('price', 30000)])

# dictionary.items() references original dictionary therefor any changes to original dictionary will be reflected in items
items = dictionary.items()

dictionary["price"] = 50000

print(items) # shows updates to dictionary

if "price" in dictionary:
    print("price found: ", dictionary["price"])