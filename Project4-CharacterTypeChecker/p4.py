sentence = input("Enter a Character : ")
char = sentence[0]
print(f"The first character is {char}")

if "a" <= char <= "z" or "A" <= char <= "Z":
    print("It is a Alphabet")
elif "0" <= char <= "9":
    print("It is Number")
else:
    print("It is Special Character")
