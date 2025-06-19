import random
print("****Guess The Number****")
attempts = int(input("Enter the no.of attempts needed : "))
random_number = random.randint(1, 100)

i = 0
while i < attempts:

    guess = int(input(f"Attempt {i+1}/{attempts} : Guess your number : "))
    if guess > random_number:
        print("Your guess is higher than random_number.Lower your guess")
    elif guess < random_number:
        print("Your guess is lower than random_number.Make Higher Prediction")
    else:
        print("You guessed correct!")
        break
    i = i+1

if i == attempts:
    print(f"The random number is {random_number}")
