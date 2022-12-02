# Map, Filter and Reduce

# Map
# map(function_to_apply, list_of_inputs)

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))  # [2, 4, 6, 8]


# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))  # [5, 7, 9]


# Filter
# filter(function_to_apply, list_of_inputs)


# function that filters vowels
def remove_consonants(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if variable in letters:
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(remove_consonants, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)
# The filtered letters are:
# e
# e


# Reduce
# reduce(function_to_apply, list_of_inputs)


