import random
print("****Coin Flip Game****")

while True:
    choice = input("Choose Heads/Tails : ")
    predicted = random.choice(["heads", "tails"])
    if choice.lower() == predicted:
        print("Congrats you win!")
    else:
        print("Sorry,try next time")
    playagain = input("Want to play again? (yes/no) ")
    if playagain == 'no':
        break
