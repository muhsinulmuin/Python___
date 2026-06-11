# smart student life management system 
# Module 5 assignment - covers Modules 1-4 concepts 

# global varisbles to store session data 
student_name = ''
student_id = ''
daily_study_hours = 0.0
monthly_pocket_money = 0.0

attendance_percentage = None 
last_expense = 0.0
total_expense = 0.0

# step 2 program introduction & student info collection
def collect_student_info():
    global student_name, student_id, daily_study_hours, monthly_pocket_money
    
    print("=" * 50)
    print("  Welcome to smart student life management system")
    print("=" * 50)
    print()
    
    student_name = input("Enter student Name        : ").strip()
    student_id   = input("Enter Student ID          : ").strip()
    
    
    # type conversion practice - str -> float 
    daily_study_hours           = float(input("Enter daily study hours :  "))
    monthly_pocket_money        = float(input("Enter Monthly Pocket Money: "))
    
    print()
    print(f"Hello, {student_name}! Your profile has been saved.")
    print()
    
# step 4 - calss attendance tracker 
def attendance_tracker():
    global attendance_percentage 
    
    print("\n --- class attendance tracker ---")
    
    total_classes = int(input("Enter Total Classes : "))
    attended_classes = int(input("Enter attended classes: "))
    
    # fuard against dicision by zero 
    if total_classes == 0:
        print("total classes cannot be zero.")
        return
    
    attendance_percentage = (attended__classes / total_classes) * 100
    
    print(f"\nattendance percentage : {attendance_percentage:.2f}%")
    if attendenace_percentage >= 75:
        print("status                   : eligible for exam")
    else:
        print("status                   : not eligible for exam")
        print("                           minimum required: 75%")
        
# step 5 - study session manager 

def study_session_manager():
    print("\n--- study session manager ---")
    
    subject = input("enter subject name           : ").strip()
    sessions = int(input("enter number of study sessions: "))
    print()
    
    # for loop pracice 
    for i in range (1, sessions + 1):
        print(f" study session {i} comlete - {subject}")
        
        print()
        response = input("did you complete all session? (yes/no): ").strip().lower()
        
        if response == "yes":
            print("great consistency!")
        else:
            print("try to improve tommorrow.")
            
# step 6 - exam result checker 

def exam_result_checker():
    global last_grade
    
    print("\n--- exam result checker ---")
    
    python_makers = float(input("enter marks in python      (out of 100): "))
    python_makers = float(input("enter marks in mathematics      (out of 100): "))
    python_makers = float(input("enter marks in english      (out of 100): "))
    
    total   = python_marks + math_marks + english_marks
    average = total / 3
    
    print(f"\ntotal marks : {toral:.1f}")
    print(f"average marks : {aberage:.2f}")
    
    # grade system with nested conditions
    if average >=90:
        last_grade = "A+"
        remark = "outstanding!"
    elif average >= 80:
        last_grade = "A"
        remark = "excellent!"
    elif average >= 70:
        last_grade >= "B"
        remark = "good work."
    elif average >= 60:
        last_grade = "C"
        remark = "keep it up."
    elif average >= 50:
        last_grade = "D"
        remark = "need improvement."
    else: 
        last_grade = "F"
        remark =" better luck next time."
    
    print(f"grade           : {last_grade}  - {remark}")
    
# step 7 - monthly expense tracker 

def expense_tracker():
    global total_expense
    
    print("\n--- monthly expense tracker ---")
    
    food = float(input("food expense  : "))
    internet = float(input("inter expense: "))
    transport = float (input("transport expense: "))
    other = float(input("other expense: "))   
    
    total_expense = food + internet + transport + other 
    remaining_balance = monthly_pocket_money - total_expense 
    
    print(f"\n total expense : {total_expense:.2f}")
    print(f"monthl;y pocker money : {monthly_pocket_money:.2f}")
    print(f"remaining balance : {remaining_balace:.2f}")
    
    
    if total_expense > monthly_pocket_money:
        print(" budget limit crossed!")
    else: 
        print(" you maneged your expenses well.")
        
# step 8 - daily problem sol;ver (sub-menu)

def even_or_odd():
    n= int(input("Enter a number: "))
    if n % 2 == 0:
        print(f"{n} is an even number: ")
    else: 
        print(f"{n} is an odd number.")
        
def largest_number():
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    c = float(input("enter third number: "))
    
    if a >= b and a >= c:
        largest = a 
    elif b >= a and b >= c:
        largest = b
    else: 
        largest = c 
        
    print(f"the largest number is: {largest}")
    
def simple_sum():
    x = float(input("enter first number: "))
    y = float(input("enter second number: "))
    print(f"sum {x + y}")
    
def daily_problem_solver():
    print("\n--- daily problem solver ---")
    
    while True: 
        print()
        print(" 1. even or odd cheker")
        print(" 2. largest number finder")
        print(" 3. simple sum calculator")
        print(" 4. Back to main menu")
        
        sub_choice = input("\nselect option ").strip()
        
        if sub_choice == "1":
            even_or_odd()
        elif sub_choice == "2":
            largest_number()
        elif sub_choice == "3":
            simple_sum()
        elif sub_choice == "4":
            break
        else:
            print("invalid option, please try again.")
            
# step 9 - coundown timer (while loop practice)

def coundown_timer():
    print("\n--- countdown timer ----")
    count = int(input("enter a countdown number: ")) 
    
    print()
    
    while count > 0:
        print(count)
        count -= 1 
    print("\nsession finished successfully.")

#step 10 - final summary 

def final_summay():
    remaining = monthly_pocket_money - total_expense
    
    print()
    print("=" * 40)
    print("  FINAL SUMMARY")
    print("=" * 40)
    print(f"student name : {student_name}")
    print(f"student id : {student_id}")
    print(f"daily study Hrs : {daily_study_hours}")
    
    if attendance_percentage is not None:
        print(f"last gade : {last_grade}")
    else:
        print(("last grade : Not checker"))
        
    print(f"Monthly Expence : {total_expense:.2f}")
    print(f"remaining balance: {remaining:.2f}")
    print("=" * 40)
    print("\nthank you for using the system.")
    print()
    
# STEP 3 – Main Menu (loop-driven)
# ============================================================
def main_menu():
    while True:
        print()
        print("=" * 30)
        print("       MAIN MENU")
        print("=" * 30)
        print("1. Class Attendance Tracker")
        print("2. Study Session Manager")
        print("3. Exam Result Checker")
        print("4. Monthly Expense Tracker")
        print("5. Daily Problem Solver")
        print("6. Countdown Timer")
        print("7. Exit")
        print("=" * 30)

        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            attendance_tracker()
        elif choice == "2":
            study_session_manager()
        elif choice == "3":
            exam_result_checker()
        elif choice == "4":
            expense_tracker()
        elif choice == "5":
            daily_problem_solver()
        elif choice == "6":
            countdown_timer()
        elif choice == "7":
            final_summary()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    collect_student_info()
    main_menu()