import os
from colorama import init, Fore
from liaison import *

# Initialize colorama
init(autoreset=True)

# Define the menu function
def menu():
    # Clear the screen based on the OS
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # Print the menu options
    print('\nMenu: ')
    print(Fore.WHITE + '''
    [1] Delete Mail \t[2] Read Mail
    [3] Scrape Mail \t[4] Send Mail
    [5] Verify Email
    ''')
    print(Fore.RED + '\n    [99] Main menu  [00] Exit \n')

    # Ask the user for their option
    try:
        option = int(input('\nEnter option: '))
    except Exception:
        # Call menu function again if the input is invalid
        menu()

    # Create a while loop to keep displaying the menu until the user chooses to exit
    while option != 100:
        # Check the user's option and call the appropriate function
        if option in dict:
            dict[option]()
        elif option == 0:
            exit()
        else:
            print('Invalid option')

        # Clear the screen and display the menu again
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print('\nMenu: ')
        print(Fore.WHITE + '''
    [1] Delete Mail \t[2] Read Mail
    [3] Scrape Mail \t[4] Send Mail
    [5] Verify Email
    ''')
        print(Fore.RED + '\n    [99] Main menu  [00] Exit \n')

        # Ask the user for their option again
        try:
            option = int(input('\nEnter option: '))
        except Exception:
            # Call menu function again if the input is invalid
            menu()

# Call the menu function to start the program
menu()
