# If Else statements

a = 18
if a >= 18:
    print("Age > 18")
else:
    print("Age < 18")

# If Elif Else  Along with truthy and false values

a = 18
drivers_license = False
if a > 18 and drivers_license:
    print("You can drive")
elif a > 18 and not drivers_license:
    print("You can get drivers license")
else:
    print("You can't drive")
