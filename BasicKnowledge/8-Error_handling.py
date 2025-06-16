# try except finally
number = 0
try:
    a = 10/number
    print(f"10/{number} is {a}")
except:
    print("Not a Valid Number")
finally:
    print("This piece always works")
