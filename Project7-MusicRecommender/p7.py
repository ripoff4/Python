import random
print("Music Recommender")

music_choices = {'rock': ["White Rabbit", "Don't Stop Believin", 'Another Brick in the Wall, Part 2'],
                 'pop': ['Happy', 'Running Up That Hill (A Deal With God)', 'Party in the U.S.A.'],
                 }

choice = input("Enter the music genre you like (rock,pop) : ")
if choice in music_choices.keys():
    music = random.choice(music_choices[choice])
    print("Here is the music recommended to you : ", music)
else:
    print("No such category is in my domain")
