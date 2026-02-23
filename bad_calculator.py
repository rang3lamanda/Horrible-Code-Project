last_result = None


def add_numbers():
    # Does input, conversion, calculation, and printing all at once
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a + b
    print("Result:", result)
    print("Result again:", result)  # unnecessary duplicate (DRY violation)


def subtract_numbers():
    # Repeats similar input logic (DRY violation)
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a - b
    print("Result:", result)


def run_calculator():
    # Handles menu, logic, looping — too many responsibilities (SRP violation)
    global last_result

    print("This is the BAD calculator.")

    while True:
        print("\nOptions: add, subtract, quit")
        choice = input("Choose an option: ")

        if choice == "add":
            add_numbers()

        elif choice == "subtract":
            subtract_numbers()

        elif choice == "quit":
            print("Exiting calculator.")
            break

        else:
            print("Invalid option.")

        # Unnecessary global modification
        last_result = "something happened"


def main():
    run_calculator()


if __name__ == "__main__":
    main()