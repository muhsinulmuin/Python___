# age checker 
## date of birth input -> age

day = int(input("Enter your day of birth: "))
month = int(input("Enter your month of birth: "))
year = int(input("Enter your year of birth: "))

if year > 2026:
    print("Invalid year")    
else: 
    primary_age = 2026 - year
    if month < 4:
        print("Your age is", primary_age)
    elif month == 4 and day <= 22:
        print("Your age is", primary_age)
    elif month > 4 or (month == 4 and day > 22):
        final_age = primary_age - 1
        print("Your age is", final_age)

'''
2030 -> invalid 
2009 -> 17
1971
08-06-2013
'''