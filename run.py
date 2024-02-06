import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Simon_says_Highscores')

scores = SHEET.worksheet('Highscores')

data = scores.get_all_values()

def simon_says():
    colors = ['red', 'blue', 'green', 'yellow']
    sequence = []

    print("Welcome to Simon Says!")
    time.sleep(1)

        for color in sequence:
        print(f"Simon says: {color}")
        time.sleep(1)
        # Clear the console or screen
        clear_screen()

