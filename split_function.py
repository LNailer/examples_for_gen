# Example of a function that calls other function.
# The structure of this will have this main function that
# calls the other functions at the end called 'main'.
# The other functions it calls will be defined first,
# then the main function will call these other functions
# when and if they are needed.


def main():
    # Ask a question that determines which function gets run.
    preferred_food = input(
        "\n \nWhich would you rather eat? \n1. chocolate \n2. ice cream \nType in 1 or 2. \n")

    if preferred_food == "1":
        print("You chose chocolate.")
    elif preferred_food == "2":
        print("You chose ice cream.")


main()
