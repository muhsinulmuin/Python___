# step-2: Program Introduction 
print("=" * 45)
print("Welcom to Smart Task Repetition System")
print("=" * 45)

# step-3: Task Input
task_name = input("\nEnter task name (e.g. Study Python): ")
repetitions = int(input("How many times do you want to repeat this task today? "))

#step-4: for Loop
print(f"\n--- Repeating Task: '{task_name}' ---")
for x in range(1, repetitions + 1):
    print(f"Task({x}): {task_name} completed.")
    
#step-5: Countdown using while Loop
countdown_start = int(input("\nEnter a countdown number: "))
print("Countdown: ", end="")
current = countdown_start
while current > 0:
    print(current, end="")
    current -= 1
print()  # nerline after countdown 

#step6: Nested Loop - Daily Schedule
print("\n--- Daily Schedule ---")
sessions = ["Morning", "Evening"]
for session in sessions: 
    for task_num in range(1,4):
        print(f'{session} task {task_num}')
        
#step-7: Infinite Lppp demo (fixed with counter)
print("\n--- Infinited Loop Demo (fixed with counter) ---")

# BAD example (commented out - would run forever):
# whilw True:
# print ("this runs forever!")

# Fixed version using a counter 
counter = 1 
while True: 
    print(f" Loop iteration {counter}")
    counter += 1
    if counter > 3:    # <- exit condition stops the loop
        break 
print(" Loop exited safely using break.")

#step-8: Final Output Summary 
print("\n" + "=" * 45)
print("     FINAL SUMMARY")
print("=" * 45)
print(f"  Task Name        : {task_name}")
print(f"  Repetitions Done : {repetitions}")
print(f"  Task Name        : {countdown_start} -> 0 Finished")
print("=" * 45)

