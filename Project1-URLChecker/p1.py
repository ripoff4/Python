print("Check your URL is valid or not")
url = input("Enter your URL : ")

if 'http://' in url:
    print("It is Http. means not secured")
elif 'https://' in url:
    print("It is Https. means secured")
else:
    print("Not valid URL")
