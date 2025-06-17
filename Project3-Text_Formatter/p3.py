print("Text Formatter")
sentence = input("Enter the Sentence? ")
print("Choose one option\n"
      "1.UpperCase\n"
      "2.LowerCase\n"
      "3.TitleCase\n"
      "4.SentenceCase")
choice = int(input("What choice do you make :"))
if (choice == 1):
    print(sentence.upper())
elif choice == 2:
    print(sentence.lower())
elif choice == 3:
    print(sentence.title())
elif choice == 4:
    print(sentence.capitalize())
else:
    print("Enter a Valid Number")
