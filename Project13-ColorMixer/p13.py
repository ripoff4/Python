print("****Color Mixer****")
color_mixes = {
    ("red", "blue"): "purple",
    ("white", "red"): "pink",
}

while True:
    first_color = input("Enter the first color : ")
    second_color = input("Enter the second color : ")
    if (first_color, second_color) in color_mixes.keys():
        print(
            f"Mixing {first_color} and {second_color} results in {color_mixes[(first_color, second_color)]}")
    elif (second_color, first_color) in color_mixes.keys():
        print(
            f"Mixing {first_color} and {second_color} results in {color_mixes[(second_color, first_color)]}")
    else:
        print("Color combination not in database")

    try_again = input("Try again? (yes/no) ")
    if try_again == 'no':
        break
