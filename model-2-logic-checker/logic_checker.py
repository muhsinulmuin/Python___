# Smart Eligibility & Performance Checker 
# Module 2 Assignnment - logic_checker.py

# step 2: Welcome Message 


print("Welcome to Samrt Eligibility & Performance Checker")
print("_" * 50)

# step 3: User Input Section


name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = float(input("Enter your exam score (0-100): ")) 
income = float(input("Enter your monthly income: "))

print("-" * 50)

# step 4: Age Eligibility Check 


if age < 18:
    print("You are not eligible due to age restrictions.")
    age_eligible = False
else:
    print("Age requirment passed.")
    age_eligible = True 

# step 5: Score Evaluation (elif ladde)


if score >= 90:
    grade ="A"
    print("Grade: A")
elif score >= 75:
    grade = "B"
    print("Grade: B")
elif score >= 60:
    grade ="C"
    print("Grade:C")
else:
    grade = "Fail"
    print("Grade: Fail")
    
# step 6: Financial Support / Scholarship Check 


if income < 20000 and score > 75:
    scholarship_status = "Eligible for scholarship support."
    print("Eligible for scholarship support.")
else: 
    scholarship_status = "Note eligible for scholarship."
    print("Not eligible for scholarship.")
    
# step 7: Nested Condition (Advanced)


if age_eligible:
    if score >= 60:
        print("You passed the program.")
    else: 
        print("You failed the program.")
else:
    print("Program access denied.")
    
# step 8: Final Summary Output


print("\n" + "=" * 50)
print("                     FINAL SUMMARY")
print("=" * 50)
print(f"    Name               :   {name}")
print(f"    Age                :   {age}")
print(f"    Score              :   {score}")
print(f"    Grade              :   {grade}")
print(f"    Scholarship Status :   {scholarship_status}")
print("=" * 50)

