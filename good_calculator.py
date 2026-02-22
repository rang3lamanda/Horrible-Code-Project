"""
Good Calculator
This version shows good coding practices:
- KISS: Keep each function simple
- DRY: Avoid repeating logic
- Single Responsibility: Each function does one thing
"""

def add(a, b):
    """Return the sum of a and b"""
    return a + b

def subtract(a, b):
    """Return the difference of a and b"""
    return a - b

def multiply(a, b):
    """Return the product of a and b"""
    return a * b

def divide(a, b):
    """Return the quotient of a and b"""
    if b == 0:
        return None
    return a / b

def main():
    print("Hello this is the good calulator.")

    while True:
        print("Your Options: Add, Subtract, Multiply, Divide, quit")
        choice = input("Type in Option: ").lower()

        if choice == "quit":
            print("You chose to quit, see you next time :)")
            break
        if choice not in {"add", "subtract", "multiply", "Divide"}:
            print("Invalid Option: Please try again or type 'quit'")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter a number or a float. :) ")
            continue

        if choice == "add":
            results = add(num1,num2)
        elif choice == "subtract":
            results = subtract(num1,num2)
        elif choice == "multiply":
            results = multiply(num1,num2)
        elif choice == "divide":
            results = divide(num1,num2)
            if results is None:
                print("Sorry cannot divide by zero. :(")
                continue


        print(f"You chose to {choice} with {num1 } and {num2}, your result is {results} .")

if __name__ == "__main__":
    main()