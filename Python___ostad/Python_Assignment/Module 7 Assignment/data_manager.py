"""
Module 7 Assignment - Smart Contact & Inventory Management System

"""


def main():
    # Step 2: Program Introduction
    
    
    print("=============================================")
    print("Welcome to Smart Contact & Inventory Manager")
    print("=============================================\n")

    # Step 3: Contact Book 
    
    
    contacts = {}
    try:
        num_contacts = int(input("How many contacts do you want to add? "))
        for i in range(num_contacts):
            name = input(f"Enter name for contact #{i + 1}: ").strip()
            phone = input(f"Enter phone number for {name}: ").strip()
            contacts[name] = phone

        # Step 4: Display All Contacts
        
        
        print("\n--- All Contacts ---")
        if not contacts:
            print("No contacts stored.")
        else:
            for name, phone in contacts.items():
                print(f"{name} – {phone}")

        # Step 5: Update and Delete Contact
        
        
        print("\n--- Update Contact ---")
        update_name = input("Enter contact name to update: ").strip()
        if update_name in contacts:
            new_phone = input(f"Enter new phone number for {update_name}: ").strip()
            contacts[update_name] = new_phone
            print(f"Updated: {update_name} – {contacts[update_name]}")
        else:
            print(f"Contact '{update_name}' not found.")

        print("\n--- Delete Contact ---")
        delete_name = input("Enter contact name to delete: ").strip()
        if delete_name in contacts:
            del contacts[delete_name]
            print(f"Contact '{delete_name}' deleted successfully.")
        else:
            print(f"Contact '{delete_name}' not found.")

        print("\n--- Updated Contacts List ---")
        for name, phone in contacts.items():
            print(f"{name} - {phone}")

    except ValueError:
        print("Error: Please enter a valid number for contact count.")

    # Step 6: Inventory Categories 
    
    
    print("\n--- Inventory Categories (Set) ---")
    user_categories = set()
    cat_input = input("Enter product categories separated by commas (e.g. electronics, food, clothes): ")
    for cat in cat_input.split(","):
        clean_cat = cat.strip().lower()
        if clean_cat:
            user_categories.add(clean_cat)

    print(f"Your Categories: {user_categories}")

    # Step 7: Set Operations
    
    
    print("\n--- Set Operations ---")
    sample_categories = {"electronics", "groceries", "furniture", "clothes"}
    print(f"Sample Categories Set: {sample_categories}")

    union_result = user_categories.union(sample_categories)
    diff_result = user_categories.difference(sample_categories)

    print(f"Union (All Unique Categories): {union_result}")
    print(f"Difference (Categories only in your list): {diff_result}")

    # Step 8: Nested Dictionary 
    
    
    
    print("\n--- Inventory Product Details (Nested Dictionary) ---")
    inventory = {
        "Laptop": {"price": 50000, "stock": 10},
        "Phone": {"price": 30000, "stock": 20},
        "Headphones": {"price": 2500, "stock": 50}
    }

    for item, details in inventory.items():
        print(f"Product: {item}")
        print(f"  Price: BDT {details['price']}")
        print(f"  Stock: {details['stock']} units")

    


if __name__ == "__main__":
    main()