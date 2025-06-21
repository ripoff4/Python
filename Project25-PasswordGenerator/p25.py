import string
import re
import random


def yes_or_no(text):
    ans = input(f"{text} (yes/no) :")
    if ans.startswith('y'):
        return True
    else:
        return False


def characters_included(include_lowercase, include_uppercase, include_digits, include_special):
    chars = ""
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_special:
        chars += string.punctuation
    return chars


def strength(password):
    len_score = min(len(password)/16, 1.0)
    char_score = 0
    if re.search(r're[a-z]', password):
        char_score += 1
    if re.search(r're[A-Z]', password):
        char_score += 1
    if re.search(r're[0-9]', password):
        char_score += 1
    str = ""
    str += string.punctuation
    score = 0
    for char in str:
        if char in password:
            score += 1
    if score >= 1:
        char_score += 1
    strength_password = (len_score*0.6)+((char_score/4)*0.4)
    if strength_password > 0.8:
        print("Super Strong password")
    elif 0.6 < strength_password <= 0.8:
        print("Strong password")
    else:
        print("weak password")


def generate_password():
    while True:
        print("====Password Generator====")
        length = int(input("Enter password length (8-20) : "))
        print("Let's Customize your password")
        include_lowercase = yes_or_no("Include lowercase (a-z)")
        include_uppercase = yes_or_no("Include Uppercase (A-Z)")
        include_digits = yes_or_no("Include Digits (0-9)")
        include_special = yes_or_no("Include Special Characters (!,.,?)")
        chars = characters_included(
            include_lowercase, include_uppercase, include_digits, include_special)
        password = ""
        for _ in range(length):
            password += random.choice(chars)
        print("Generating your password ...")
        print(f"====NEW password====")
        print(f"New Password : {password}")
        score = strength(password)
        print("====Password Generation Completed====")

        try_again = input("Try another Password? (yes/no) :")
        if try_again.startswith('n'):
            break


generate_password()
