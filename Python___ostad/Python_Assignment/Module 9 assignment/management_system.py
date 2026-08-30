#module 9



def main():
    #  menu navigation
    student_names = []
    student_scores = []
    contacts = {}
    categories = set()
    votes = []

    print("==========================================================")
    print(" Welcome to Smart School Management & Voting Analysis System")
    print("==========================================================")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add Student Scores & Run Analysis")
        print("2. Manage Contacts (Dictionary CRUD)")
        print("3. Manage Unique Categories (Set Operations)")
        print("4. Run Voting System & Winner Detection")
        print("5. Search Records")
        print("6. Run Advanced Student Marks Analysis (Nested Loops)")
        print("7. Run Debugging Practice Demo")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        # Step 3 & Step 4:  (DSA Logic)
        if choice == "1":
            try:
                count = int(input("\nHow many students to enter? "))
                student_names.clear()
                student_scores.clear()

                for i in range(count):
                    name = input(f"Enter name for student #{i + 1}: ").strip()
                    score = float(input(f"Enter score for {name}: "))
                    student_names.append(name)
                    student_scores.append(score)

                # Step 3: Display students, scores, and convert to Tuple
                print("\n--- Student Records ---")
                for i in range(len(student_names)):
                    print(f"{student_names[i]}: {student_scores[i]}")

                scores_tuple = tuple(student_scores)
                print(f"Scores as Tuple: {scores_tuple}")

                # Step 4: Score Analysis without built-in max(), min(), or sum()
                if student_scores:
                    highest = student_scores[0]
                    lowest = student_scores[0]
                    total = 0.0

                    for score in student_scores:
                        if score > highest:
                            highest = score
                        if score < lowest:
                            lowest = score
                        total += score

                    average = total / len(student_scores)

                    print("\n--- Score Analysis ---")
                    print(f"Highest Score: {highest}")
                    print(f"Lowest Score : {lowest}")
                    print(f"Average Score: {average:.2f}")

            except ValueError:
                print("Error: Please enter valid numbers for student counts and scores.")

        # Step 5: Contact Book
        
        elif choice == "2":
            while True:
                print("\n--- CONTACT BOOK MENU ---")
                print("a. Add Contact")
                print("b. Update Contact")
                print("c. Delete Contact")
                print("d. View All Contacts")
                print("e. Back to Main Menu")
                c_choice = input("Select an option (a-e): ").strip().lower()

                if c_choice == "a":
                    c_name = input("Enter Contact Name: ").strip()
                    c_phone = input("Enter Phone Number: ").strip()
                    contacts[c_name] = c_phone
                    print(f"Contact '{c_name}' added successfully.")

                elif c_choice == "b":
                    c_name = input("Enter Contact Name to Update: ").strip()
                    if c_name in contacts:
                        c_phone = input("Enter New Phone Number: ").strip()
                        contacts[c_name] = c_phone
                        print(f"Contact '{c_name}' updated.")
                    else:
                        print("Contact not found.")

                elif c_choice == "c":
                    c_name = input("Enter Contact Name to Delete: ").strip()
                    if c_name in contacts:
                        del contacts[c_name]
                        print(f"Contact '{c_name}' deleted.")
                    else:
                        print("Contact not found.")

                elif c_choice == "d":
                    print("\n--- All Contacts ---")
                    if not contacts:
                        print("No contacts stored yet.")
                    else:
                        for name, phone in contacts.items():
                            print(f"Name: {name} | Phone: {phone}")

                elif c_choice == "e":
                    break
                else:
                    print("Invalid option. Try again.")

        # Step 6: Unique Category Management 
        elif choice == "3":
            print("\n--- UNIQUE CATEGORY MANAGEMENT ---")
            cat_input = input("Enter product categories separated by commas: ")
            new_cats = [c.strip() for c in cat_input.split(",") if c.strip()]
            
            for c in new_cats:
                categories.add(c)

            print(f"\nCurrent Unique Categories Set: {categories}")

            # Set Operations
            set_a = categories.copy()
            set_b = {"Electronics", "Books", "Stationery", "Sports"}

            print(f"\nSet A (User Categories): {set_a}")
            print(f"Set B (Predefined Categories): {set_b}")

            union_set = set_a.union(set_b)
            diff_set = set_a.difference(set_b)

            print(f"Union (A ∪ B): {union_set}")
            print(f"Difference (A - B): {diff_set}")

        # Step 7 & Step 8: Voting System & Winner Detection
        elif choice == "4":
            try:
                voter_count = int(input("\nHow many voters? "))
                votes.clear()

                for i in range(voter_count):
                    candidate = input(f"Voter #{i + 1} - Enter candidate name: ").strip().title()
                    if candidate:
                        votes.append(candidate)

                # Frequency counting logic using a dictionary
                vote_counts = {}
                for candidate in votes:
                    if candidate in vote_counts:
                        vote_counts[candidate] += 1
                    else:
                        vote_counts[candidate] = 1

                print("\n--- Voting Results ---")
                for candidate, count in vote_counts.items():
                    print(f"Candidate '{candidate}': {count} vote(s)")

                # Step 8: Winner Detection using loops
                winner = None
                max_votes = -1

                for candidate, count in vote_counts.items():
                    if count > max_votes:
                        max_votes = count
                        winner = candidate

                if winner:
                    print(f"\n Winner is Candidate '{winner}' with {max_votes} vote(s)!")
                else:
                    print("No votes recorded.")

            except ValueError:
                print("Error: Voter count must be an integer.")

        # Step 9: Searching Feature
        elif choice == "5":
            print("\n--- GLOBAL SEARCH ---")
            query = input("Enter Name to Search (Student / Contact / Candidate): ").strip()

            found = False

            # Search in Students
            for i in range(len(student_names)):
                if student_names[i].lower() == query.lower():
                    print(f"[FOUND in Students] {student_names[i]} - Score: {student_scores[i]}")
                    found = True

            # Search in Contacts
            for name, phone in contacts.items():
                if name.lower() == query.lower():
                    print(f"[FOUND in Contacts] {name} - Phone: {phone}")
                    found = True

            # Search in Voting Candidate List
            if query.title() in votes:
                count = votes.count(query.title())
                print(f"[FOUND in Voting] Candidate '{query.title()}' has {count} vote(s)")
                found = True

            if not found:
                print("Record not found.")

        # Step 10: Advanced Challenge (Nested Loops)
        elif choice == "6":
            print("\n--- ADVANCED STUDENT MARKS ANALYSIS ---")
            student_marks = {
                "John": [80, 75, 90],
                "Alex": [70, 85, 88],
                "Maria": [95, 92, 98]
            }

            for student, scores in student_marks.items():
                print(f"\nStudent: {student}")
                total_score = 0

                # Inner loop to process subject scores
                for idx, score in enumerate(scores, start=1):
                    print(f"  Subject {idx} Score: {score}")
                    total_score += score

                print(f"  Total Score: {total_score}")


        # Step 2 / Step 8: Exit program
        elif choice == "8":
            print("\nThank you for using Smart School Management & Voting Analysis System. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose a number between 1 and 8.")


if __name__ == "__main__":
    main()