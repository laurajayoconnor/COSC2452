def eggsample():

    egg_collection = ["Little Egg", "Big Egg", "Easter Egg"]

    the_basket = [eggs for eggs in egg_collection]

    print(the_basket)

    egg_collection = ["Little Egg", "Big Egg", "Easter Egg"]

    the_basket = []

    for eggs in egg_collection:
        the_basket.append(eggs)

    print(the_basket)

def yeehawgaol():

    message = "You're trapped here unless you know the password. What is the password?\n"

    while user_input := input(message).lower() != "howdy":
        print("No escape for you!")

    message = "You're trapped here unless you know the password. What is the password?\n"

    user_input2 = input(message)
    while user_input2 != "howdy":
        print("No escape for you!")
        user_input2 = input(message)

eggsample()
yeehawgaol()