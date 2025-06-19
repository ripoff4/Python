print("****Calculator****")

while True:
    print("Select Operation")
    print(
        " 1. + addition\n",
        "2. - subtraction\n",
        "3. * multiplication\n",
        "4. / division",
    )
    choice = int(input("Enter operation (1-4) : "))
    first = int(input("Enter first number : "))
    second = int(input("Enter second number : "))
    if choice == 1:
        print(f"Answer is {first+second}")
    elif choice == 2:
        print(f"Answer is {first-second}")
    elif choice == 3:
        print(f"Answer is {first*second}")
    elif choice == 4:
        print(f"Answer is {first/second}")
    else:
        print("Enter a valid operation")
    again = input("Try again? (yes/no) ")
    if again == 'no':
        break
