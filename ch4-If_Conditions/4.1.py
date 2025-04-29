age = 25
has_license = False
if age > 20 and has_license:
    print("You can drive")
elif age > 20 and not has_license:
    print("You can drive but you need to get a license")
else:
    print("You cannot drive")

status = "major" if age >= 18 else "minor"
print("You are a", status)
