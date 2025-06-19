import random
import time
import os
print("*****Rock,Paper and Scissors*****")

print("Rules\n:"
      "- Rock crushes Scissors\n"
      "- Scissors cuts Paper\n"
      "- Paper covers Rock\n"
      "- First to win 3 rounds is the champion!\n")

rps = ['rock', 'paper', 'scissors']

dict = {
    ('scissors', 'rock'): [0, 1],
    ('scissors', 'paper'): [1, 0],
    ('rock', 'paper'): [0, 1],
    ('rock', 'scissors'): [1, 0],
    ('paper', 'scissors'): [0, 1],
    ('paper', 'rock'): [1, 0],
    ('paper', 'paper'): [0, 0],
    ('rock', 'rock'): [0, 0],
    ('scissors', 'scissors'): [0, 0],
}

time.sleep(2)
os.system("cls")

computer_score = 0
human_score = 0
while True:
    while True:
        os.system("cls")
        print("Score : Human vs Computer")
        print(f"        {human_score} : {computer_score} ")
        human_input = input("Choose 1 (Rock/Paper/Scissors) : ")
        if human_input.lower() != 'rock' and human_input.lower() != 'scissors' and human_input.lower() != 'paper':
            print("Try again with actual value")
            time.sleep(1)
        else:
            break
    computer_input = random.choice(rps)
    set_outcome = (human_input.lower(), computer_input)
    answer_list = dict[set_outcome]
    human_score_present = answer_list[0]
    computer_score_present = answer_list[1]
    if human_score_present > computer_score_present:
        print("Human wins this round!")
        time.sleep(2)
    else:
        print("Computer wins this round!")
        time.sleep(2)
    human_score += answer_list[0]
    computer_score += answer_list[1]
    if human_score == 3:
        print("Human wins the set!")
        break
    if computer_score == 3:
        print("Computer wins the set!")
        break
