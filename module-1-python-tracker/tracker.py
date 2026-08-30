# Daily Life Tracker Program -Module 1

#step 2: welcome message 
print("---------------------------------------------");
print ("    Welcome to Daily Life Tracker Program   ");
print("---------------------------------------------");
print();

#step 3: user information
print("----User Information----");
name = input("Enter your name: ");
available_hours = float(input("Enter your total available hours for today: "));
daily_budget = float(input("Enter your daily budget (BDT): "));
print();

#step 4: daily activity input
print("---- Daily Activity Input ----");
study_hours = float(input("How many hours will you spend studying Python? "));
coding_hours = float(input("How many hours will you spend practicing coding? "));
other_hours = float(input("how many hours for other Activities? "));
 
total_planned_hours = study_hours + coding_hours + other_hours
print();
 
#step 5: expense input 
print("---- Daily Expense Input ----");
food_expense = float(input("Enter Food Expense (BDT):  "));
transport_expense = float(input("Enter Transportation Expense (BDT): "));
other_expense = float(input("Enter Other Expense (BDT) "));
 
total_expense = food_expense + transport_expense + other_expense
print();
 
#step 6: time planning check 
print("---- Time Planning Check ----");
if total_planned_hours > available_hours:
     print("You have planned more hours than available.");
else: 
     print("Your daily plan is realistic.");
print();
    
#step 7: buget check
print("---- Budget Check ----");
if total_expense > daily_budget:
    print("You have exceeded yout daily budget.");
else:
    print("You are within yoiur daily budget.");
print();

#step 8: final summary output
remaining_budget = daily_budget - total_expense 

print("-----------------------------------------------");
print("             DAILY SUMMARY REPORT              ");
print("-----------------------------------------------");
print(f"Hello, {name}!");
print(f"Total Planned Hours : {total_planned_hours} hours");
print(f"Abailable Hours     : {available_hours} hours");
print(f"Total Expense       : {total_expense} BDT");
print(f"Daily Budget        : {daily_budget} BDT");
print(f"Remainging Budget   : {remaining_budget} BDT");
print("-----------------------------------------------");
print("             Thank you for using the Tracker!              ");
print("-----------------------------------------------");
