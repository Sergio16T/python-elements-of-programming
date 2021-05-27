cars = ["Ford", "Volvo", "BMW"]
print(cars[0])

# loop through array
for car in cars:
    print(car)

# modify each element in array
for i, car in enumerate(cars):
    cars[i] = car + " "

#print modified cars
print(cars)

# modify via iterating through range in array
for n in range(len(cars)):
    cars[n] += "car"

#print modified cars
print(cars)

# add element to array
# You can use the append() method to add an element to an array.

cars.append("Honda")

print(cars)


fruits = ["apple", "banana", "cherry"]

# insert(index, element) inserts element at index
fruits.insert(1, "orange")

print(fruits)

# pop(index) Removes the element at the specified position
fruits.pop(1)

print(fruits)

# You can also use the remove method to remove an element from the array.
# remove(value) Removes the first item with the specified value

fruits.insert(0, "apple")

print(fruits)

fruits.remove("apple")

print(fruits)

# index(value) - returns index of first instance of element
indexOfBanana = fruits.index("banana")

print("indexOfBanana", indexOfBanana)