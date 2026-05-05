import math

def show_menu():
    print("\n====== CALCULATOR MENU ======")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Modulus (%)")
    print("0. Exit")
    print("=============================")

while True:
    show_menu()

    choice = input("Enter your choice (0-7): ")

    if choice == "0":
        print("Calculator closed. 👋")
        break

    try:
        if choice == "6":  # Square root
            num = float(input("Enter number: "))
            if num >= 0:
                print("Result:", math.sqrt(num))
            else:
                print("Cannot take square root of negative number")

        elif choice in ["1", "2", "3", "4", "5", "7"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", num1 + num2)

            elif choice == "2":
                print("Result:", num1 - num2)

            elif choice == "3":
                print("Result:", num1 * num2)

            elif choice == "4":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Cannot divide by zero")

            elif choice == "5":
                print("Result:", num1 ** num2)

            elif choice == "7":
                print("Result:", num1 % num2)

        else:
            print("Invalid choice. Please select from menu.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")