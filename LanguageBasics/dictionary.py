import json
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

print("items as tuples in list", items) # shows updates to dictionary

print("dictionary", dictionary)

if "price" in dictionary:
    print("price found: ", dictionary["price"])

del dictionary["price"]

print(dictionary) # shows updates to dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel['iris'] = 1234
print(list(tel)) # prints list of keys in dictionary

print(tel)

tel.update({
    "abe": 1111,
    "joan": 321
})

def sortBySecondItem(tup) -> int:
    return tup[1]

sortTelUsingLambda = sorted(tel.items(), key=lambda t: t[1])  # returns sorted items in dictionary as tuples in list
sortTel = sorted(tel.items(), key=sortBySecondItem)

print('sorted list of tuples', sortTel)


# dict comprehension

exampleDictComp = {x: x**2 for x in (2, 4, 6, 8)}
print('exampleDictComp', exampleDictComp) # {2: 4, 4: 16, 6: 36, 8: 64}

# looping techniques

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# gallahad the pure
# robin the brave

def create_sample_response(guid: str, amount: str = None, createDate: str = None) -> str:

    example_json_obj = {
        "uid": guid,
        "body": {
            "number": 123,
        },
    }

    # Example use of dict comprehension with for loop
    example_json_obj["body"].update({ k: v for k, v in {
        "sampleAmount": amount,
        "createDate": createDate,
    }.items() if v})

    ser_json = json.dumps(example_json_obj)

    return ser_json

print(create_sample_response(guid="1", amount="11.00"))

