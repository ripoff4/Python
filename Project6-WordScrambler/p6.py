import random

while True:
    word = input("Enter a word (or press 'quit') : ")
    if word.lower() == 'quit':
        break

    n = len(word)
    letters = []
    for i in range(n):
        letters.append(word[i])

    random.shuffle(letters)
    print("Shuffled Word is ", "".join(letters))
