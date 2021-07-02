cars = ["Ford", "Volvo", "BMW"]
print(cars[0])

# loop through list
for car in cars:
    print(car)

# modify each element in list
for i, car in enumerate(cars):
    cars[i] = car + " "

#print modified cars
print(cars)

# modify via iterating through range in list
for n in range(len(cars)):
    cars[n] += "car"

#print modified cars
print(cars)

# add element to list
# You can use the append() method to add an element to an list.

cars.append("Honda")

print(cars)


fruits = ["apple", "banana", "cherry"]

# insert(index, element) inserts element at index
fruits.insert(1, "orange")

print(fruits)

# pop(index) Removes the element at the specified position
fruits.pop(1)

print(fruits)

# You can also use the remove method to remove an element from the list.
# remove(value) Removes the first item with the specified value

fruits.insert(0, "apple")

print(fruits)

fruits.remove("apple")

print(fruits)

# index(value) - returns index of first instance of element
indexOfBanana = fruits.index("banana")

print("indexOfBanana", indexOfBanana)


squares = [1, 4, 9, 16, 25]
length = len(squares)

secondToFourthItem = squares[1:4] # slice from index 1 (inclusive) to index 4 (exclusive)
lastThree = squares[-3:]  # slicing returns a new list
print("lastThree: ", lastThree) # [9, 16, 25]


lastItem = squares[-1] # 25 - use negative indices to indicate to begin counting from the right
accessLastItem = squares[length - 1]

print("lastItemAccess: ", {
    "lastItem": lastItem,
    "accessLastItem": accessLastItem
})

secondToLastItem = squares[-2] # 16
print("secondToLastItem: ", secondToLastItem)

shallowCopyOfSquares = squares[:] # [1, 4, 9, 16, 25]

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# replace some values
letters[2:5] = ['C', 'D', 'E']
print("Assignment to slices", letters) # ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# now remove them
letters[2:5] = []
print("remove values with assignment via slice", letters) #['a', 'b', 'f', 'g']

# clear list entirely
letters[:] = [] # OR letters.clear()
print("clear list", letters)


# concatenation
squares = squares + [36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("concatenation", squares)
