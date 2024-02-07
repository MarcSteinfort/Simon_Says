import gspread
from google.oauth2.service_account import Credentials
import time
import random

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

data = scores.get_all_values()
colors = ['red', 'blue', 'green', 'yellow']
def dynamic_seq(length):
    
    sequence = []
     # Generate a random sequence of colors for Simon to say
    for _ in range(length):  # Adjust the range as needed
        color = random.choice(colors)
        sequence.append(color)
        print(f"Simon says: {color}")
        time.sleep(1)
    clear_screen()
    print('next sequence')
    time.sleep(interval)

def simon_says():
    # colors = ['red', 'blue', 'green', 'yellow']
    # sequence = []

    print("Welcome to Simon Says!")
    time.sleep(1)

    # Generate a random sequence of colors for Simon to say
    # for _ in range(5):  # Adjust the range as needed
    #     color = random.choice(colors)
    #     sequence.append(color)
    #     print(f"Simon says: {color}")
    #     time.sleep(2)
    #     clear_screen()
    length = 1
    while True:
        dynamic_seq(length)
        length += 1


    player_sequence = []
    #Get the player´s Sequence
    for color in sequence:
        user_input = input("Your turn: ").lower()
        clear_screen()

        if user_input != color:
            print("Wrong sequence! Game over.")
            break
        else:
            print("Correct!")

        player_sequence.append(user_input)

    else:
        print("Congratulations! You completed the sequence.")

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    simon_says()