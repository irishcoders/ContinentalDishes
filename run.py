import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style
from tabulate import tabulate

# Initialize Google Sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
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

# Convert the menu dictionary into a list of lists
table = [[key, value["item"], value["price"]] for key, value in menu.items()]

# Define the headers for the table
headers = ["Item Number", "Item Name", "Price"]


def display_menu():
    """
    This function displays the list of menu and prices to the user/customer
    """
    table = [[key, dish["item"], dish["price"]] for key, dish in menu.items()]
    headers = ["Item Number", "Item Name", "Price"]
    print(tabulate(table, headers, tablefmt="grid"))


def take_orders():
    """
    This function takes the customer order and handles the error message if the user enters an
    incorrect input
    """
    orders = []
    while True:
        try:
            order_number = int(input("Enter the item number you'd like to order (Enter 0 to finish): \n"))
            if order_number == 0:
                break
            elif order_number in menu:
                quantity = int(input(f"How many {menu[order_number]['item']} would you like to order? \n"))
                if quantity > 0:
                    orders.append({"item": menu[order_number]["item"], "quantity": quantity})
                    print(Fore.GREEN + "Added to your order." + Style.RESET_ALL)  # Print in green
                else:
                    print(Fore.RED + "Quantity must be greater than 0." + Style.RESET_ALL)  # Print in red
            else:
                print(Fore.RED + "Invalid item number. Please select a number within the menu list." + Style.RESET_ALL)  # Print in red
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter the valid item number for the item you want to order, then enter a quantity." + Style.RESET_ALL)  # Print in red
    return orders


def print_receipt(orders):
    """
    This function prints the receipt for the user order to the terminal
    """
    print("\nPlease wait while we generate your receipt...")
    print("Your order receipt has been generated! See details below:..\n")

    print("Receipt:")
    total = 0
    for order in orders:
        item_price = menu[next(key for key, value in menu.items() if value["item"] == order["item"])]["price"]
        total += item_price * order["quantity"]
        print(Fore.YELLOW + f"{order['quantity']} x {order['item']} - ${item_price} each" + Style.RESET_ALL)
    return total


# Main program
def main():
    """
    run all program function here
    """
    display_menu()
    orders = take_orders()
    total = print_receipt(orders)
    print(Fore.YELLOW + f"Total: ${total}" + Style.RESET_ALL)
    print(Fore.GREEN + "Thank you for your order! Please pay at the counter and enjoy your meal!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
