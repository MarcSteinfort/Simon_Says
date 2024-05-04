import gspread
from google.oauth2.service_account import Credentials
import time
import random
import os
from colorama import just_fix_windows_console
just_fix_windows_console()
from colorama import Fore, Back, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Simon_says_Highscores')

scores = SHEET.worksheet('Highscores')

colors = ['red', 'blue', 'green', 'yellow']
color_dict = {"red": Fore.RED, "green":Fore.GREEN, "yellow":Fore.YELLOW, "blue":Fore.BLUE}

#Function for the Name of the player. Will be the name which is displayed in the Highscores.git 
def input_name():
    name = input("Please enter your name: \n")
    return name

def dynamic_seq(length, interval, sequence):
    # Generate a random sequence of colors for Simon to say
    for _ in range(length):
        color = random.choice(colors)
        sequence.append(color)
        print(f"Simon says: {color_dict[color]} colors {Style.RESET_ALL}")
        time.sleep(interval)
        clear_screen()
    print('Next sequence')
    return sequence

# function to increase the Sequnce by one
def simon_says(sequence, interval):
    
    length = 1
    while True:
        sequence=dynamic_seq(1, interval, sequence)
        

        # for loop to get the player's Sequence
        for _ in range(length):
            user_input = input("Your turn: ").lower()
            clear_screen()

            if user_input != sequence[_]:
                print("Wrong sequence! Game over.")
                return
            else:
                print("Correct!")

            
        length += 1

        print("Congratulations! You completed the sequence.")

#Functions for the different difficulties and the Introduciton

#Introduction to the game
def option1():
    print("This is your introduction for the game Simon says. I will show you different colors starting with one color. You need to name them in the same order as I did. Each successful round increases the difficulty by one color. You can choose the easy difficulty by pressing '2' and the hard difficulty by pressing '4'. If you want a mediocre challenge you can choose the medium difficulty by pressing '3'. Try to beat the Highscore and have good luck trying!")

def option2(sequence):
    print("Welcome to the easymode. Good luck!")
    interval=2
    simon_says(sequence, interval)

def option3(sequence):
    print("Welcome to the normalmode. Good luck!")
    interval=1
    simon_says(sequence, interval)

def option4(sequence):
    print("Welcome to the hardmode. Good luck!")
    interval=0.5
    simon_says(sequence, interval)

#function the Main Menu
def main():
    while True:
        print("Welcome to Simon Says!")
        time.sleep(1)

        user_name = input_name()

        sequence =[]
        print("\nMenu:")
        print("1. Introduction to the Game")
        print("2. Difficulty: Easy")
        print("3. Difficulty: Medium")
        print("4. Difficulty: Hard")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            option1()
        elif choice == '2':
            option2(sequence)
        elif choice == '3':
            option3(sequence)
        elif choice =='4':
            option4(sequence)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        user_choice=input("enter y/Y to continue: ")
        if user_choice.lower()!="y":
            break

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
