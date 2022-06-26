# the object implements the __getitem__() method && __setitem() method. In other words,
# it describes objects that are "containers", meaning they contain other objects.
# This includes strings, lists, tuples, and dictionaries.

class Produce(object):
    def __init__(self):
        self.produce = {
            "Apple": { "fruit": True, "vegetable": False },
            "Pear": { "fruit": True, "vegetable": False },
            "Banana": { "fruit": True, "vegetable": False },
            }

    def __getitem__(self, item):
        return self.produce[item]

    def __setitem__(self, name, value):
        self.produce[name] = value


foodAisle = Produce()
print(foodAisle["Apple"]["fruit"])

foodAisle['Zuchinni'] = { "fruit": False, "vegetable": True }


print(foodAisle["Zuchinni"])
