# List Comprehensions provide a concise way to create lists

# Create list of squares Without List Comprehensions
squares = []
for x in range(10):
    squares.append(x ** 2)

squares  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squaresUsingMap = list(map(lambda n: n ** 2, range(10)))

# A list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses.
conciseWithLC = [x ** 2 for x in range(10)]

listComp = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))  # append a tuple of integers to list

print(combs)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

print([(a, b) for a in [1, 2] for b in [2, 3] if a < b])

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x * 2 for x in vec]  # [-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]  # [0, 2, 4]

# apply a function to all the elements
[abs(x) for x in vec]  # [4, 2, 0, 2, 4]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
stripped = [str.strip() for str in freshfruit]
print(stripped)  # ['banana', 'loganberry', 'passion fruit']

# create a list of 2-tuples like (number, square)
tupleWithExpression = [(x, x ** 2) for x in range(6)]

print("tupleWithExpression:", tupleWithExpression)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# flatten a list using a listcomp with two 'for'
listWithLists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_v1 = [num for list_of_nums in listWithLists for num in list_of_nums]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('flattened_v1', flattened_v1)


# flatten without using listComprehension
flattened = []
for listItem in listWithLists:
    for number in listItem:
        flattened.append(number)

print("flattened: " + str(flattened))

# Nested List Comprehensions

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

transposed2 = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed2_row = []
    for row in matrix:
        transposed2_row.append(row[i])
    transposed2.append(transposed2_row)

transposed2
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


usingZip = list(zip(*matrix))
print(usingZip)  # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
