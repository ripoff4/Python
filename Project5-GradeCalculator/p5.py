score = int(input("Enter the Score : "))

try:
    if 90 < score <= 100:
        print("It is A Grade")
    elif 80 < score <= 90:
        print("It is B Grade")
    elif 70 < score <= 80:
        print("It is C Grade")
    elif 60 < score <= 70:
        print("It is D Grade")
    else:
        print("You are Failed")
except:
    print("There is a problem")
finally:
    print("Completed The Project")
