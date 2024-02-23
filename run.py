import gspread
from google.oauth2.service_account import Credentials
import time
import random
import os

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

def input_name():
    name = input("Please enter your name: \n")
    return name

def option1():
    print("This is your introduction for the game Simon says. I will show you different colors starting with one color. You need to name them in the same order as I did. Each successful round increases the difficulty by one color. You can choose the easy difficulty by pressing '2' and the hard difficulty by pressing '3'. Try to beat the Highscore and have good luck trying!")

def dynamic_seq(length, interval):
    sequence = []
    # Generate a random sequence of colors for Simon to say
    for _ in range(length):
        color = random.choice(colors)
        sequence.append(color)
        print(f"Simon says: {color}")
        time.sleep(interval)
        clear_screen()
    print('Next sequence')

def simon_says():
    print("Welcome to Simon Says!")
    time.sleep(1)

    user_name = input_name()

    length = 1
    while True:
        dynamic_seq(length, 1)
        length += 1

        # Get the player's Sequence
        player_sequence = []
        for _ in range(length):
            user_input = input("Your turn: ").lower()
            clear_screen()

            if user_input != sequence[_]:
                print("Wrong sequence! Game over.")
                return
            else:
                print("Correct!")

            player_sequence.append(user_input)

        print("Congratulations! You completed the sequence.")

def option2():
    print("Welcome to the easy mode. Good luck!")
    simon_says()

def option3():
    print("Welcome to the hard mode. Good luck!")
    simon_says()

def main():
    while True:
        print("\nMenu:")
        print("1. Introduction to the Game")
        print("2. Difficulty: Easy")
        print("3. Difficulty: Hard")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
