MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 150,  # ₹150
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 250,  # ₹250
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 300,  # ₹300
    }
}


def is_resource_sufficient(order_ingredients):
    """Check if there are enough resources to make the drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Return the total amount inserted by the user."""
    print("Please insert Indian coins/notes.")
    total = int(input("How many ₹1 coins?: ")) * 1
    total += int(input("How many ₹2 coins?: ")) * 2
    total += int(input("How many ₹5 coins?: ")) * 5
    total += int(input("How many ₹10 coins?: ")) * 10
    total += int(input("How many ₹20 notes?: ")) * 20
    total += int(input("How many ₹50 notes?: ")) * 50
    total += int(input("How many ₹100 notes?: ")) * 100
    total += int(input("How many ₹200 notes?: ")) * 200
    total += int(input("How many ₹500 notes?: ")) * 500
    return total


def is_transaction_successful(money_received, drink_cost):
    """Check if payment is enough and give change if needed."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ₹{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct resources and make the coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


profit = 0
resources = {
    "water": 3000,
    "coffee": 100,
    "milk": 1000
}

is_on = True
while is_on:
    choice = input("What would you like? (expresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{profit}")
    elif choice in MENU:
        drink = MENU[choice]
        print(f"The price of {choice} is ₹{drink['cost']}.")  # 👈 shows rate first
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. Please select expresso, latte, or cappuccino.")
