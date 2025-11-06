# Example of a function that calls other function.
# The structure of this will have this main function that
# calls the other functions at the end called 'main'.
# The other functions it calls will be defined first,
# then the main function will call these other functions
# when and if they are needed.

def chocolate():
    print("You chose chocolate. \n")
    type_of_chocolate = input(
        "But do you like \nwhite chocolate, or \nmilk chocolate 🍫\n")

    print(f"Good choice, you like {type_of_chocolate}.")


def ice_cream():
    print("You chose ice cream. \n")
    ice_cream_flavour = input("But what is your favourite flavour? \n")

    print(f"Good choice, I like {ice_cream_flavour} too. 🍨")


def main():
    # Ask a question that determines which function gets run.
    preferred_food = input(
        "Which would you rather eat? \n1. chocolate \n2. ice cream \nType in 1 or 2. \n")

    if preferred_food == "1":
        # Call the chocolate function.
        chocolate()
    elif preferred_food == "2":
        # Call the chocolate function.
        ice_cream()


main()
