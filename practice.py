def eggsample():

    # Typical way
    egg_collection = ["Little Egg", "Big Egg", "Easter Egg"]

    the_basket = []

    for eggs in egg_collection:
        the_basket.append(eggs)

    print(the_basket)

    egg_collection2 = ["Little Egg", "Big Egg", "Easter Egg"]

    the_basket2 = [eggs2 for eggs2 in egg_collection2]

    print(the_basket2)


def yeehawgaol():

    message = "You're trapped here unless you know the password. What is the password?\n"

    while user_input := input(message).lower() != "howdy":
        print("No escape for you!")

    print("Gah, you escaped!\n********")

    message2 = "You're trapped here unless you know the password. What is the password?\n"

    user_input2 = input(message2)
    while user_input2 != "howdy":
        print("No escape for you!")
        user_input2 = input(message2)

    print("Gah, you escaped!\n********")

eggsample()
yeehawgaol()