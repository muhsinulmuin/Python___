"""
Module 10 Assignment - Smart Utility Function Toolkit

"""

# Step 5: Global Variable 


APP_NAME = "Smart Utility Toolkit v1.0"


def show_app_scope():
    """Prints global variable to demonstrate global vs local scope behavior."""
    print(f"\n[Global Scope Demo] Running Application: {APP_NAME}")


# Step 3: Calculator Functions 


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def main():
    
    # Step 2: Program Introduction
    
    
   
    print("Welcome to Smart Utility Function Toolkit")
    print("========================================")

    # Demonstrate Scope
    
    
    show_app_scope()

    # Step 4: User Input Menu & Calculator Execution
    
    
    
    print("\n--- CALCULATOR MENU ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Select an option (1-4): ").strip()

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")

        except ValueError:
            print("Error: Invalid numeric input.")
    else:
        print("Invalid choice selected.")

    # Step 6: Lambda Practice 
    
    
    print("\n--- LAMBDA PRACTICE ---")
    square = lambda x: x ** 2

    try:
        user_num = float(input("Enter a number to square: "))
        print(f"Square of {user_num} is: {square(user_num)}")
    except ValueError:
        print("Error: Invalid number entered.")

    # Step 7: Map Function Usage
    
    
    print("\n--- MAP FUNCTION PRACTICE ---")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original List: {numbers}")

    doubled_numbers = list(map(lambda x: x * 2, numbers))
    print(f"Doubled List (using map): {doubled_numbers}")

    # Step 8: Filter Function Usage
    
    
    
    print("\n--- FILTER FUNCTION PRACTICE ---")
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Filtered Even Numbers (using filter): {even_numbers}")

   
    

if __name__ == "__main__":
    main()