status_types = ['NEW', "WORKING", 'RESOLVED']
sample_types = ['new', 'working', 'new', 'resolved', 'New', 'Working']


# The main difference between generator expressions and list comprehensions is that the former don't
# create the list in memory.
# The syntax of Generator Expression is similar to List Comprehension except
# it uses parentheses ( ) instead of square brackets [ ].
supported_types = all(str.upper(status) in status_types for status in sample_types)
# print(supported_types) -- True
