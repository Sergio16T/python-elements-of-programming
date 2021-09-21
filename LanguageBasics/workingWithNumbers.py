import math

add = 2 + 2
# 4
multipleOperations = 50 - 5*6
# 20
pemdas =(50 - 5*6) / 4
# 5.0
division = 8 / 5  # division always returns a floating point number
# 1.6

#  In Python, the “//” operator works as a floor division for integer and float arguments.
# However, the operator / returns a float value if one of the arguments is a float
quotientOf15And3 = 15 / 3
quotientOf15And2 = 15 / 2
floorDivisionOf15And2 = 15 // 2

print("quotientOf15And3: ", quotientOf15And3) # 5.0
print("quotientOf15And2: ", quotientOf15And2) # 7.5


print("math.floor -> quotientOf15And2: ", math.floor(quotientOf15And2)) # 7
print("floorDivisionOf15And2: ", floorDivisionOf15And2) # 7


remainder = 17 % 3 # the % operator returns the remainder of the division left over when one operand is divided by a second operand.
# 2

fiveSquared = 5 ** 2  # 5 squared
# 25

twoToThePowerOfSeven = 2 ** 7  # 2 to the power of 7
# 128

floatingNum = 43.212333333

# Before f-strings were introduced Python used format method
formattedFloat = float("{:.2f}".format(43.212333333))

# f strings
fFloat = float(f"{floatingNum:.2f}")
fFloat2 = f"{float(floatingNum):.2f}"



print("formattedFloat: ", formattedFloat)
print("fFloat: ", fFloat)
print("fFloat2: ", fFloat2)