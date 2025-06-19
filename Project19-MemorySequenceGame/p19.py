import random
import time
import os


def clearscreen():
    os.system("cls")


print("****Memory Sequence Game****")
print("Rules:\n",
      "Watch as numbers appear one by one\n",
      "After the sequence is shown, type it back in order\n",
      "Each round adds one more number to remember\n"
      "How far can you go?")

n = 1
while True:
    list_numbers = []
    for i in range(n):
        list_numbers.append(random.randint(1, 20))

    print(f"====Round{n}====")
    for i in range(len(list_numbers)):
        print(list_numbers[i])

    time.sleep(2)
    clearscreen()
    print("====Enter your Answer====")
    answer_list = []
    for i in range(n):
        ans = int(input(f"Enter the {i+1} number : "))
        answer_list.append(ans)

    if answer_list == list_numbers:
        print(f"Round {n} completed")
    else:
        print(f"Cometetion Ended")
        print("The answer is : ", list_numbers)
        print(f"Round{n-1} is your highest round cleared")
        break
    n += 1
