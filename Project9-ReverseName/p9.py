print("Reverse A Name")

while True:
    name = input("Enter a name? ")
    name_list = list(name)
    print(f"Reversed name of name {name} is {"".join(name_list[::-1])}")

    cont = input("Try another name? (y/n) ")
    if cont == 'n':
        break
