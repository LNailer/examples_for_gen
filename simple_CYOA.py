def start_game():
    print("Welcome to Your Adventure!")
    first_choice()

def first_choice():
    print("\nYou find yourself at a crossroads.")
    print("1. Take the left path")
    print("2. Take the right path")
    
    choice = input("Enter your choice (1/2): ").strip()
    
    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        print("Invalid choice. Try again.")
        first_choice()

def left_path():
    print("\nYou've chosen the left path...")
    # Continue story branch
    print("1. Continue exploring")
    print("2. Turn back")
    
    choice = input("Enter your choice (1/2): ").strip()
    
    if choice == '1':
        # Next story segment
        pass
    elif choice == '2':
        first_choice()

def right_path():
    print("\nYou've chosen the right path...")
    # Continue story branch
    pass

def game_over():
    print("\nGame Over. Would you like to play again?")
    play_again = input("Enter 'yes' or 'no': ").lower().strip()
    
    if play_again == 'yes':
        start_game()
    else:
        print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    start_game()
