import random

def Play():
    l1 = ['Rock', 'Paper', 'Scissors'] # List of different rps options

    get_computer_choice = random.choice(l1) # Randomized computer choice
    get_user_choice = input("Rock, Paper or Scissors: ") # User's choice

    def get_Winner(get_computer_choice, get_user_choice):
        winner = ''
        # Conditions for the User to be the winner
        if (get_computer_choice == 'Rock' and get_user_choice == 'Paper') or (get_computer_choice == 'Paper' and get_user_choice == 'Scissors') or (get_computer_choice == 'Scissors' and get_user_choice == 'Rock'):
            winner = 'User'
            return winner
        # Conditions for the Computer to be the winner
        elif (get_computer_choice == 'Paper' and get_user_choice == 'Rock') or (get_computer_choice == 'Scissors' and get_user_choice == 'Paper') or (get_computer_choice == 'Rock' and get_user_choice == 'Scissors'):
            winner = 'Computer'
            return winner
        # Conditions for a draw
        else:
            winner = 'Draw'
            return winner

    # Prints if either the User or Computer wins
    if get_Winner(get_computer_choice, get_user_choice) == 'User' or get_Winner(get_computer_choice, get_user_choice) == 'Computer':
        print('Computer:', get_computer_choice)
        print('User:', get_user_choice)
        print('The winner is', get_Winner(get_computer_choice, get_user_choice))
    # Prints if the game was a draw
    else:
        print('Computer:', get_computer_choice)
        print('User:', get_user_choice)
        print('It was a', get_Winner(get_computer_choice, get_user_choice))

Play()