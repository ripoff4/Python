print("****Vowel Counter****")

sentence = input("Enter a Sentence : ")
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for word in sentence:
    for letter in word:
        if letter.lower() in vowels:
            count = count+1
print(f"Total Vowels in sentence is {count}")
