# Curly braces or the set() function can be used to create sets.
# Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed

{'orange', 'banana', 'pear', 'apple'}
print('orange' in basket)  # True


set_of_fruits = set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])

print(set_of_fruits)