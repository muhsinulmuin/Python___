# daily life problem solver toolkit 

def print_divider():
    print("\n" + "=" * 40)
    
def calculate_sum():
    #step 4: sum calculator
    print_divider()
    Print("SUM CALCULATOR")
    num1 = float(input("1st number: "))
    num2 = float(input(" 2nd number: "))
    result = num1 + num2 
    print(f"\n Result: {num1} + {num2} = {result}")
    
def check_even_odd():
    #step 5: Even or odd Checker 
    print_divider()
    print("EVEN OR ODD CHECKER")
    print_divider()
    num = int(input(" enter a number: "))
    if num % 2 == 0:
        print(f"\n Result: {num} is the EVEN number")
    else: 
        print(f"\n Result: {num} is the ODD number")

def find_macimum():
    #step 6: Maximum Finder
    print_divider()
    print(" MAXIMUM NUMBER FINDER")
    print_divider()
    num1 = float(input(" enter 1st number: "))
    num2 = float(input(" enter 2nd number: "))
    num3 = float(input(" enter 3rd number: "))
    
    if num1 >= num2 and num1 >= num3:
        largest = num1 
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3 
        
    print(f"\n Result: The largest number is {latgest}")
    
def show_menu():
    #step 3: Menu System
    print_divider()
    print(" MAIN MENU")
    print_divider()
    print("1. Calculate sum of tow numbers")
    print("2. Check even or odd")
    print("3. Find macimum of three numbers")
    print_divider()
    
def main():    
    #step 7: Repeat program using loop
    while True:
        show_menu()
        choice = input(" write your choice (1/2/3): ").strip()
        
        if choice == "1":
            calculate_sum()
        elif choice == "2":
            check_even_odd()
        elif choice == "3":
            find_maximum()
        else:
            print("\n worng choice! please write 1/2/3")
            
        print_divider()
        again = input("Do you want to solve another problem? (yes/no): ").strip().lower()
        if again !="yes":
            print_divider()
            print(" thanks! ")
            print_divider()
            break
        
if __name__ == "__main__":
    main()