"""
Module 11 Assignment - Smart File-Based Expense & Notes Manager

"""

import os
import random
from datetime import datetime

# File names
EXPENSE_FILE = "expenses.csv"
NOTES_FILE = "notes.txt"


def generate_unique_id():
    """Generates a random unique ID using random module."""
    return random.randint(1000, 9999)


def get_current_timestamp():
    """Generates current date and time formatted string using datetime module."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def add_expense():
    """Step 4 & 7: Writes expense records with unique ID and timestamp into expenses.csv."""
    title = input("Enter expense title: ").strip()
    amount_str = input("Enter expense amount: ").strip()

    try:
        amount = float(amount_str)
        record_id = generate_unique_id()
        timestamp = get_current_timestamp()

        # Step 4: File Writing (Expenses) - append mode 'a'
        
        
        with open(EXPENSE_FILE, mode="a", encoding="utf-8") as file:
            file.write(f"{record_id},{timestamp},{title},{amount}\n")

        print(f"Expense '{title}' (ID: {record_id}) added successfully!")

    except ValueError:
        print("Error: Invalid amount entered. Please enter a valid number.")


def view_expenses():
    """Step 5 & 8: Reads expenses.csv and displays records cleanly after checking existence."""
    # Step 8: Simple Validation
    if not os.path.exists(EXPENSE_FILE):
        print("No records found yet.")
        return

    print("\n--- ALL EXPENSES ---")
    print(f"{'ID':<8} | {'Date & Time':<20} | {'Title':<20} | {'Amount (BDT)':<10}")
    print("-" * 65)

    # Step 5: File Reading (Expenses)
    with open(EXPENSE_FILE, mode="r", encoding="utf-8") as file:
        lines = file.readlines()
        if not lines:
            print("File is empty. No records found yet.")
            return

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) == 4:
                    rec_id, timestamp, title, amount = parts
                    print(f"{rec_id:<8} | {timestamp:<20} | {title:<20} | {amount:<10}")


def add_note():
    """Step 6 & 7: Appends personal notes with unique ID and timestamp into notes.txt."""
    note_text = input("Enter your personal note: ").strip()

    if note_text:
        record_id = generate_unique_id()
        timestamp = get_current_timestamp()

        # Step 6: Notes File System - append mode 'a'
        
        
        with open(NOTES_FILE, mode="a", encoding="utf-8") as file:
            file.write(f"[{record_id}] [{timestamp}] {note_text}\n")

        print(f"Note (ID: {record_id}) saved successfully!")
    else:
        print("Error: Note cannot be empty.")


def view_notes():
    """Step 6 & 8: Reads notes.txt after validating file existence."""
    # Step 8: Simple Validation
    if not os.path.exists(NOTES_FILE):
        print("No records found yet.")
        return

    print("\n--- ALL NOTES ---")
    
    
    with open(NOTES_FILE, mode="r", encoding="utf-8") as file:
        lines = file.readlines()
        if not lines:
            print("File is empty. No notes found yet.")
            return

        for line in lines:
            print(line.strip())





def main():
    # Step 2: Program Introduction
    
    
   
    print(" Welcome to Smart File-Based Manager")
    print("========================================")

    # Step 3: Menu System Loop
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add new expense")
        print("2. View all expenses")
        print("3. Add new note")
        print("4. View all notes")
        print("5. Run Debugging Practice Demo")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            add_note()
        elif choice == "4":
            view_notes()
        elif choice == "5":
            run_debugging_demo()
        elif choice == "6":
            print("\nThank you for using Smart File-Based Manager. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()