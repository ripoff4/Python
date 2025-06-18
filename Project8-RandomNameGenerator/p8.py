import random

names_list = ['Ethan', 'Sophia', 'Liam', 'Ava',
              'Noah', 'Isabella', 'Mateo', 'Mia', 'Kai', 'Zara']

try:
    n = int(input("Enter the no.of names you want : "))
    random_names = random.sample(names_list, n)  # Here we use random.sample
    for name in random_names:
        print(name)
except:
    print("Enter a valid number")
finally:
    print("GoodBye!")
