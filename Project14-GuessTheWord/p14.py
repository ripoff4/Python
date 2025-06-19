import random
print("****Guess The Word****")
word_list = ["listen", "harry", "happy", "Charan", "eagle", "arjun"]

while True:
    name = random.choice(word_list)
    name_list = list(name)
    random.shuffle(name_list)
    print(f"The shuffled word is : {"".join(name_list)}")
    while True:
        inputword = input("What is your guess? ('quit' if needed) :")
        if inputword == name:
            print("You guessed correct")
            break
        elif inputword == 'quit':
            break
        else:
            print("Try again!")

    again = input("Want to try with another word? (yes/no)")
    if again == 'no':
        break
