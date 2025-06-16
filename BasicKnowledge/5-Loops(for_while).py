# Basic For and While Loops
for i in range(1, 6):
    print(i)
a = 5
while a > 0:
    print(a)
    a = a-1

# Reversed For and While Loops
for i in range(1, 6, -1):
    print(i)
a = 5
i = 0
while i <= a:
    print(i)
    i = i+1

# Skipping numbers
for i in range(1, 6, 2):
    print(i)
a = 5
while a > 0:
    print(a)
    a = a-2

# Looping in lists
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# reversed loopin in list
for fruit in reversed(fruits):
    print(fruit)

# using enumeration function
for iterator, fruit in enumerate(fruits):
    print(f"{fruit} indexed to {iterator}")

# using zip function
color = ["red", "yellow", "green"]
for fruit, color in zip(fruits, color):
    print(f"{fruit}:{color}")

# For dictionary purpose
dict = {'fruit': 'apple', 'color': 'red', 'price': '10'}
for key, value in dict.items():
    print(f"{key}:{value}")
