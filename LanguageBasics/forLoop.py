# range(start, stop, step)
# start inclusive, stop exclusive
# step An integer number specifying the incrementation. Default is 1
# start is optional, stop is required and step is optional

range1 = range(2, 6, 2)
for n in range1:
    print(n)

# one argument only will be the stop 'exclusive'.
range2 = range(5)

for n in range2:
    print(n)  # print numbers 0 - 4


for index, value in enumerate(['tic', 'tac', 'toe']):
    print(index, value)
