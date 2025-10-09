def subtract(a, b):
    return a - b

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b    

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '%': modulus
}

def calculator():
    num1 = float(input("Enter first number: "))
    should_continue = True

    while should_continue:
        print("Available operations:", " ".join(operations.keys()))
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter second number: "))
        
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ")
        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            print("\n" + "*" * 20)
            print("Starting a new calculation...\n")
            calculator()

calculator()
