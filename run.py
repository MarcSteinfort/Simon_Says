import gspread
from google.oauth2.service_account import Credentials
import time
import random
import os
from colorama import Fore, Back, Style
from colorama import just_fix_windows_console
just_fix_windows_console()

"""
This was copied from the Love Sandwiches Tutorial.
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Simon_says_Highscores')

colors = ['red', 'blue', 'green', 'yellow']
"""
I managed the different Colorsettings for the different difficulties
with the help of a Friend, who is a professional.
"""
color_dict = {"red": Fore.RED, "green": Fore.GREEN, "yellow": Fore.YELLOW, "blue": Fore.BLUE}
color_dict_back = {"red": Back.RED, "green": Back.GREEN, "yellow": Back.YELLOW, "blue": Back.BLUE}


def input_name():
    """Function for the name of the player. Shown name in the Highscores.
    """
    name = input("Please enter your name: \n")
    return name


def dynamic_seq(length, interval, sequence, difficulty):
    """
    Generate a random sequence of colors for Simon to say.
    Via Stackflow I got support for the print statements
    """
    for _ in range(length):
        color = random.choice(colors)
        sequence.append(color)
        if difficulty == "easy":
            print(f"Simon says: {color_dict[color]}{color}{Style.RESET_ALL}")
        elif difficulty == "medium":
            print(f"Simon says: {color_dict_back[color]}{color}{Style.RESET_ALL}")
        elif difficulty == "hard":
            key, value = random.choice(list(color_dict.items()))
            print(f"Simon says: {value}{color}{Style.RESET_ALL}")
        time.sleep(interval)
        clear_screen()
    print('Next round!')
    return sequence


def simon_says(sequence, interval, difficulty):
    """Function to increase the Sequence by one
    """
    length = 1
    while True:
        sequence = dynamic_seq(1, interval, sequence, difficulty)

        # for loop to get the player's Sequence
        for _ in range(length):
            user_input = input("Your turn: \n").lower()
            clear_screen()

            if user_input != sequence[_]:
                print("Wrong sequence! Game over.")
                print(len(sequence)-1, "succesful rounds.")
                return
            else:
                print("Correct!")

        length += 1

        print("Congratulations! You completed the sequence.")


def send_data(highscore, name, difficulty):
    """Function to send data to worksheet
    """
    try:
        highscore_sheet = SHEET.worksheet(f"Highscores_{difficulty}")
        highscore_sheet.append_row([name, highscore])
        """
        Tuple (first element Column index second order).
        The Try/except Method got I from Stackflow.
        The sort method I got from gspread.org.
        """
        highscore_sheet.sort((2, "des"))
        print(f"The Score was saved in Highscores_{difficulty}")
    except Exception as e:
        print("Failed to send data to the Worksheet!")


def get_data(difficulty):
    """
    Function to retrieve data from Worksheet.
    The Try/except Method got I from Stackflow.
    """
    try:
        highscore_list = SHEET.worksheet(f"Highscores_{difficulty}").get_all_values()
        return highscore_list
    except Exception as e:
        print("Failed to retrieve data from the Worksheet!")
        return None


def print_highscore_list(highscore_list):
    """Function for printing the Highscore into the Terminal.
    """
    for element in highscore_list:
        print(element)


def option1():
    """Function for the Introduction and difficulties of the game.
    """
    print("This is your introduction for the game Simon says.")
    print("I will show you different colors starting with one color.")
    print("You need to name them in the same order as I did. Each successful round increases the difficulty by one color.")
    print("You can choose the easy difficulty by pressing '2' and the hard difficulty by pressing '4'.")
    print("If you want a mediocre challenge you can choose the medium difficulty by pressing '3'.")
    print("Remember you need to type all previous called colors, in the right order.")
    print("You need to type them seperately and you can confirm your decision with enter.")
    print("If you want to check the Highscore you can press '5' to choose the Highscores you want to see.")
    print("Try to beat the Highscore and have good luck trying!")


def option2(sequence):
    print("Welcome to the easymode. Good luck!")
    interval = 1
    simon_says(sequence, interval, "easy")


def option3(sequence):
    print("Welcome to the normalmode. Good luck!")
    interval = 1
    simon_says(sequence, interval, "medium")


def option4(sequence):
    print("Welcome to the hardmode. Good luck!")
    interval = 0.5
    simon_says(sequence, interval, "hard")


def main():
    """Function for the Main Menu
    """
    while True:
        print("Welcome to Simon Says!")
        time.sleep(1)

        sequence = []
        print("\nMainmenu:")
        print("1. Introduction to the Game")
        print("2. Difficulty: Easy")
        print("3. Difficulty: Medium")
        print("4. Difficulty: Hard")
        print("5. Give me the Highscores")
        print("6. Exit")
        choice = input("Enter your choice: \n")

        if choice == '1':
            option1()
            continue
        elif choice == '2':
            option2(sequence)
            difficulty = "easy"
        elif choice == '3':
            option3(sequence)
            difficulty = "medium"
        elif choice == '4':
            option4(sequence)
            difficulty = "hard"
        elif choice == '5':
            while True:
                print("\nHigscore Menu:")
                print("1. Highscores easy:")
                print("2. Highscores medium")
                print("3. Highscores hard")
                print("4. Return to Mainmenu")
                highscore_choice = input("Enter your choice: \n")
                if highscore_choice == '1':
                    print("Here is you Highscore for the easy difficulty \n")
                    highscore_list = get_data("easy")
                elif highscore_choice == '2':
                    print("Here is you Highscore for the medium difficulty \n")
                    highscore_list = get_data("medium")
                elif highscore_choice == '3':
                    print("Here is you Highscore for the medium difficulty \n")
                    highscore_list = get_data("hard")
                elif highscore_choice == '4':
                    print("Return to Main menu...")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
                    continue

                clear_screen()
                if highscore_list is not None:
                    print_highscore_list(highscore_list)
                    input("Press enter to continue: \n")

            continue
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue
        user_name = input_name()
        send_data(len(sequence)-1, user_name, difficulty)
        user_choice = input("enter y/Y to continue: \n")
        if user_choice.lower() != "y":
            clear_screen()
            break


def clear_screen():
    """
    Function to clear the screen.
    I had help from an AI for this function.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
