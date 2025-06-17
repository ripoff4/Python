total_steps = int(input("Enter no.of steps you want? "))
print(f"Total no.of steps to be taken in a day are {total_steps}")
current_steps = int(input("Total steps taken already? "))

steps_remaining = total_steps-current_steps
if steps_remaining < 0:
    print(f"You have exceeded the amount by {-steps_remaining} steps")
elif steps_remaining == 0:
    print(f"You have satisfied the amount of steps")
else:
    print(f"You have {steps_remaining} steps remaining")
