status_types = ['NEW', "WORKING", 'RESOLVED']
sample_types = ['new', 'working', 'new', 'resolved', 'New', 'Working']


# The main difference between generator expressions and list comprehensions is that the former don't
# create the list in memory.
supported_types = all(str.upper(status) in status_types for status in sample_types)
# print(supported_types) -- True
