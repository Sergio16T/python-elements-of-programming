# Initialize tuple two different ways
mytuple = ("apple", "banana", "cherry")
tupleDeclaration = "apple", "strawberry"

print(mytuple)
print(tupleDeclaration)

t = 12345, 54321, 'hello!'
t[0]  # 12345

t  # (12345, 54321, 'hello!')

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)  # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
# t[0] = 88888
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v[0][0] = 2

print(v)  # ([2, 2, 3], [3, 2, 1])
