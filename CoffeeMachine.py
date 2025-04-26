# separate dictionary of ingredients
# What would you like
# report
# function for latte, cappuccino, espresso
# money
stock = {
    "Water":500,
    "Coffee":500,
    "Milk":500,
    "Money":0,
}
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# def Latte():
#     stock['Water'] -= menu['latte']['ingredients']['water']
#     stock['Coffee'] -= menu['latte']['ingredients']['coffee']
#     stock['Milk'] -= menu['latte']['ingredients']['milk']
#     stock['Money'] -= menu['latte']['cost']
#
# def Espresso():
#     stock['Water'] -= menu['espresso']['ingredients']['water']
#     stock['Coffee'] -= menu['espresso']['ingredients']['coffee']
#     stock['Milk'] -= menu['espresso']['ingredients']['milk']
#     stock['Money'] -= menu['espresso']['cost']
#
# def Cappuccino():
#     stock['Water'] -= menu['cappuccino']['ingredients']['water']
#     stock['Coffee'] -= menu['cappuccino']['ingredients']['coffee']
#     stock['Milk'] -= menu['cappuccino']['ingredients']['milk']
#     stock['Money'] -= menu['cappuccino']['cost']
#
# x = 'latte'
# print(menu[x]['ingredients']['water'])


def report():
    print(f"Water: {stock['Water']}ml")
    print(f"Coffee: {stock['Coffee']}g")
    print(f"Milk: {stock['Milk']}ml")
    print(f"Money: ${stock['Money']}")
def CoffeeType(coffee):
    stock['Water'] -= menu[coffee]['ingredients']['water']
    stock['Coffee'] -= menu[coffee]['ingredients']['coffee']
    stock['Milk'] -= menu[coffee]['ingredients']['milk']
    stock['Money'] -= menu[coffee]['cost']
    print(f"here is ${round(stock['Money'],2)} in change")
    stock['Money'] = 0
    print(f"Here is your {coffee} 🍵 Enjoy!")
    CoffeeMachine()

# coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
# if coffee == "off":
#     exit()
#
# if coffee == "report":
#     report()
#     coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
#     if coffee == "off":
#         exit()
#
# print("Please insert coins")
# quarters = int(input("How many quarters?: "))
# dimes = int(input("How many dimes?: "))
# nickles = int(input("How many nickles?: "))
# pennies = int(input("How many pennies?: "))
#
# balance = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
# stock['Money'] += balance
#
#
# required = menu[coffee]['ingredients']
# missing = []
#
# # Check each required ingredient
# if stock['Water'] < required['water']:
#     missing.append("water")
# if stock['Coffee'] < required['coffee']:
#     missing.append("coffee")
# if stock['Milk'] < required['milk']:
#     missing.append("milk")
# if stock['Money'] < menu[coffee]['cost']:
#     missing.append("balance. Money refunded")
#
# # If anything is missing, notify and exit
# # In Python, any non-empty list is True, and an empty list is False.
# if missing:
#     print(f"Sorry, not enough: {', '.join(missing)}.")
#     exit()
# else:
#     CoffeeType(coffee)


def CoffeeMachine():
    coffee = input("What would you like? (Espresso $1.5/ Latte %2.5/ Cappuccino $3):").lower()
    if coffee == "off":
        exit()

    if coffee == "report":
        report()
        coffee = input("What would you like? (Espresso $1.5/ Latte %2.5/ Cappuccino $3):").lower()
        if coffee == "off":
            exit()

    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    balance = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    stock['Money'] += balance

    required = menu[coffee]['ingredients']
    missing = []

    # Check each required ingredient
    if stock['Water'] < required['water']:
        missing.append("water")
    if stock['Coffee'] < required['coffee']:
        missing.append("coffee")
    if stock['Milk'] < required['milk']:
        missing.append("milk")
    if stock['Money'] < menu[coffee]['cost']:
        missing.append("balance")

    # If anything is missing, notify and exit
    # In Python, any non-empty list is True, and an empty list is False.
    if missing:
        print(f"Sorry, not enough: {', '.join(missing)}. Money refunded")
        exit()
    else:
        CoffeeType(coffee)

CoffeeMachine()


