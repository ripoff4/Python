import time
print("****Countdown Timer****")

timer = int(input("Enter the Countdown time : "))
while timer > 0:
    print(f"⏰ {timer} seconds remaining ...")
    time.sleep(1)
    timer -= 1
print("Countdown Completed!")
