s = 'hi'
print(s[1])  # i
print(len(s))  # 2
print(s + ' there')  # hi there

string = 'Python'

length = len(string)

print(length)

lastCharacter = string[length - 1]
lastCharacterWithNegative = string[-1]  # OR use negative indices to indicate to begin counting from the right

print("lastCharacter: ", lastCharacter)
print("lastCharacterWithNegative: ", lastCharacterWithNegative)

#  *** STRING SLICING ***

print("""
    *** STRING SLICING ***
""")

sliceFirstTwo = string[0:2]  # characters from index 0 (included) to 2 (excluded)

print("sliceFirstTwo: ", sliceFirstTwo)  # 'Py'

thirdLetterToFifthLetter = string[2:5]  # characters from index 2 (included) to 5 (excluded)
print("thirdLetterToFourthLetter: ", thirdLetterToFifthLetter)  # tho

firstTwo = string[:2]  # character from the beginning to index 2 (excluded)
# 'Py'
fourthToLast = string[4:]  # characters from index 4 (included) to the end
#  'on'

lastTwo = string[-2:]

print("lastTwo:", lastTwo)

# *** MULTI LINE STRINGS ***

print("""
    *** MULTI LINE STRINGS ***
""")

multi = """It was the best of times.
It was the worst of times."""

# It was the best of times.
#   It was the worst of times.
print(multi)

multi2 = 'First line.\nSecond line.'  # \n means newline - without print(), \n is included in the output

print(multi2)
# First line.
# Second line.

# MultiLine Strings - 3 quotes - can span multiple lines
#  End of lines are included by default to prevent this behavior include a \
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# *** SINGLE VS DOUBLE QUOTES ***

print("""
     *** SINGLE VS DOUBLE QUOTES ***
""")

singleQuotes = 'spam eggs'  # single quotes

escapeSingleQuotes = 'doesn\'t'  # use \' to escape the single quote...
# "doesn't"

doubleQuotes = "doesn't"  # ...or use double quotes instead
print(doubleQuotes)
# "doesn't"

doubleQuotesWithin = '"Yes," they said.'
print("doubleQuotesWithin", doubleQuotesWithin)  # "Yes," they said.

nestedDoubleQuotes = "\"Yes,\" they said."

print(nestedDoubleQuotes)  # "Yes," they said.

st = '"Isn\'t," they said.'
print(st)  # "Isn't," they said.

# *** Converting other types to string form ***

pi = 3.14
#  text = 'The value of pi is ' + pi
# NO, does not work: '+' does not automatically convert numbers or other types to string form
text = 'The value of pi is ' + str(pi)  # yes

print(text)
