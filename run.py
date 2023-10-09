import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('cred.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('continental_dishes')

customer_orders = SHEET.worksheet('customer_orders')

# This is the list of menu and prices to be displayed to the user/customer
menu = {
    1: {"item": "Jollof Rice", "price": 40},
    2: {"item": "Beef Pepper-soup", "price": 35},
    3: {"item": "Prawn Cocktail", "price": 25},
    4: {"item": "Spaghetti Carbonara", "price": 30},
    5: {"item": "French fries", "price": 15},
    6: {"item": "Buffalo Wings", "price": 22},
    7: {"item": "Macaroni and Cheese", "price": 28},
    8: {"item": "Coca-Cola", "price": 10},
    9: {"item": "Fanta", "price": 10},
    10: {"item": "Bottled Water", "price": 7}
}
