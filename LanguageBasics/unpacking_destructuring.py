# equivelant to spread operator in JavaScript

list(range(3, 6))  # normal call with separate arguments
# [3, 4, 5]
args = [3, 6]
list(range(*args))  # call with arguments unpacked from a list
# [3, 4, 5]

unpacked = [*args]
print(unpacked)  # [3, 6]


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

# Destructuring/Unpacking values from Dictionary - Equivelant to Object Destructuring Assignment in JavaScript
parrot(**d)

dictExample = {'x': 1, 'y': 2}
x, y = dictExample.values()
a, b = dictExample.values()

print('Unpacking values from Dictionary using .values() with destructuring assignment: ', {
    'x': x,
    'y': y,
    # demonstrate that we can assign values to any key
    'a': a,
    'b': b,
})

# Tuples
people = [
    ("Bob", 42, "Mechanic"),
    ("James", 24, "Artist"),
    ("Harry", 32, "Lecturer")
]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Using _ as a placeholder if we only want to assign the first and third item in tuple
person = ("Bob", 42, "Builder")
name, _, profession = person

print(name, profession)  # Bob Builder

# Using * to Collect Values
print("Using * to Collect Values")
first, second, *tail = [1, 2, 3, 4, 5]

print(first)  # 1
print(second)  # 2
print(tail)  # [3, 4, 5]

*head2, tail2 = [1, 2, 3, 4, 5]

print(head2)  # [1, 2, 3, 4]
print(tail2)  # 5

head, *middle, tail = [1, 2, 3, 4, 5]

print(head)  # 1
print(middle)  # [2, 3, 4]
print(tail)  # 5


# A sample program to demonstrate unpacking of
# dictionary items using **
def fun(_a, _b, _c):
    print(_a, _b, _c)


# A call with unpacking of dictionary
d = {'_a': 2, '_b': 4, '_c': 10}
fun(**d)

print({**d})
