import random
import math
import time

print("****Related Word Game****")

dict = {
    'tree': ["leaf", "root", "stem", "flowers", "fruits"],
    'school': ["students", "teachers", "playground", "principal"],
    'home': ["rooms", "living area", "bathroom"]
}

list_keys = []
for word in dict.keys():
    list_keys.append(word)

score = 0
time_passed = 0
while True:
    random_word = random.choice(list_keys)
    print("Find Related word to the word : ", {random_word})
    session_score = 0
    session_time_passed = 0
    while True:
        start_time = time.time()
        ans = input("Enter your answer : ")
        if ans in dict[random_word]:
            response_time = time.time() - start_time
            current_score = 5 - math.floor(response_time)
            print("You guessed correct in ", {response_time})
            if current_score <= 1:
                score += 1
                session_score += 1
            else:
                score += current_score
                session_score += current_score
            time_passed = time_passed+5
            session_time_passed = session_time_passed+5
            print(
                f"Your current score is {session_score}/{session_time_passed}")
            break
        elif ans == "quit":
            break
        else:
            print("You guessed wrong")
    try_again = input("Try again ? (yes/no) ")
    if try_again == 'no':
        print(f"Your final score is {score}/{time_passed}")
        break
