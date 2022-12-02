"""
Generators are iterators, but you can only iterate over them once.
It’s because they do not store all the values in memory, they generate the values on the fly.

Generators save memory

Generators are best for calculating large sets of results (particularly calculations involving loops themselves)
where you don’t want to allocate the memory for all results at the same time.
"""


# generator version fibonaci iterative
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b  # a is assigned the value of b. b is assigned the value of a + b


for x in fibon(8):
    print('fibon a', x)


# Not a great usecase but demonstrates very basic functionality
def generator_function():
    for i in range(10):
        yield i


for item in generator_function():
    print(item)

# Output: 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9