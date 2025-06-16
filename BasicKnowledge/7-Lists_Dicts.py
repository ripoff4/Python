# List Dict
list = ['apple', 'grape', 'banana']
for fruit in list:
    print(fruit)

dict = {'name': 'Apple', 'color': 'Red'}

print(dict.keys())
print(dict.values())

# Set - Duplicates not allowed

set = {'apple', 'banana', 'apple'}
print(set)  # shows {'apple','banana'}

# Tuple - Can't change values

tuple = (10.75, 11.5)

tuple[0] = 8.75  # error
