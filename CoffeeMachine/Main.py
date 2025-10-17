MENU = {
    "espresso": {  # Fixed typo
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
            print(f"❌ Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Return the total amount inserted by the user."""
    print("\n💰 Please insert Indian coins/notes.")
    denominations = [
        ("₹1 coins", 1),
        ("₹2 coins", 2),
        ("₹5 coins", 5),
        ("₹10 coins", 10),
        ("₹20 notes", 20),
        ("₹50 notes", 50),
        ("₹100 notes", 100),
        ("₹200 notes", 200),
        ("₹500 notes", 500)
    ]
    
    total = 0
    for name, value in denominations:
        while True:
            try:
                count = int(input(f"How many {name}?: "))
                if count < 0:
                    print("Please enter a non-negative number.")
                    continue
                total += count * value
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    return total

def is_transaction_successful(money_received, drink_cost):
    """Check if payment is enough and give change if needed."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"💵 Here is ₹{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"❌ Sorry, not enough money. You inserted ₹{money_received} but need ₹{drink_cost}.")
        print("Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct resources and make the coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"✅ Here is your {drink_name} ☕️. Enjoy!")

def print_report():
    """Print the current resource levels and profit."""
    print("\n📊 === COFFEE MACHINE REPORT ===")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ₹{profit}")
    print("=" * 32 + "\n")

# Initialize global variables
profit = 0
resources = {
    "water": 3000,
    "coffee": 100,
    "milk": 1000
}

# Main program loop
is_on = True
print("☕️ Welcome to the Coffee Machine! ☕️")

while is_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        print("🔌 Turning off the coffee machine. Goodbye!")
        is_on = False
    
    elif choice == "report":
        print_report()
    
    elif choice in MENU:
        drink = MENU[choice]
        print(f"\n💵 The price of {choice} is ₹{drink['cost']}.")
        
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    
    else:
        print("❌ Invalid choice. Please select espresso, latte, or cappuccino.")
        print("   (Type 'report' to see resources or 'off' to turn off)")
