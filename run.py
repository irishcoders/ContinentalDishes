 import gspread
from google.oauth2.service_account import Credentials

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


def display_menu():
    """
    This function displays the list of menu and prices to the user/customer
    """
    print("Welcome to Continental Dishes! Here's our menu:")
    for item_number, dish in menu.items():
        print(f"{item_number}. {dish['item']} - ${dish['price']}")


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
                    print("Added to your order.")
                else:
                    print("Quantity must be greater than 0.")
            else:
                print("Invalid item number. Please select a number within the menu list.")
        except ValueError:
            print("Invalid input. Please enter the valid item number for the item you want to order, then enter a quantity.")
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
        print(f"{order['quantity']} x {order['item']} - ${item_price} each")
    return total



# Main program
if  __name__ == "__main__":
    display_menu()
    orders = take_orders()
    total = print_receipt(orders)
    print(f"Total: ${total}")
    print("Thank you for your order! Please pay at the counter and enjoy your meal!")