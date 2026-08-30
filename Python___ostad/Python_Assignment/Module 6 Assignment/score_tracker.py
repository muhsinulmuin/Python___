
# Module 6 Assignment - Student Score Tracker System



def main():
    # Step 2: Program Introduction
    
    
    print("========================================")
    print("Welcome to Student Score Tracker System")
    print("========================================\n")

    # Step 3: Student Data Input
    
    
    student_names = []
    student_scores = []

    try:
        num_students = int(input("How many students do you want to enter? "))

        for i in range(num_students):
            name = input(f"Enter name for student #{i + 1}: ").strip()
            score = float(input(f"Enter score for {name}: "))
            student_names.append(name)
            student_scores.append(score)

        if not student_scores:
            print("No student data entered. Exiting program.")
            return

        # Step 4: Display All Scores
        
        
        print("\n--- Student Scores List ---")
        for i in range(len(student_names)):
            print(f"{student_names[i]} – {student_scores[i]}")

        # Step 5: Highest and Lowest Score 
        
        
        
        
        highest_score = student_scores[0]
        lowest_score = student_scores[0]

        for score in student_scores:
            if score > highest_score:
                highest_score = score
            if score < lowest_score:
                lowest_score = score

        print("\n--- Score Summary ---")
        print(f"Highest Score: {highest_score}")
        print(f"Lowest Score : {lowest_score}")

        # Step 6: Convert Scores to Tuple
        
        
        scores_tuple = tuple(student_scores)
        print("\n--- Scores as Tuple (Immutable Data) ---")
        print(f"Tuple Data: {scores_tuple}")

        # Step 7: Tuple Unpacking 
        
        
        
        print("\n--- Tuple Unpacking Practice ---")
        if len(scores_tuple) >= 3:
            s1, s2, s3 = scores_tuple[:3]
            print(f"First 3 Scores Unpacked: Score 1 = {s1}, Score 2 = {s2}, Score 3 = {s3}")
        else:
            print(f"Total scores entered ({len(scores_tuple)}) is less than 3, cannot unpack 3 variables.")

        # Step 8: Average Score Calculation
        
        
        total_sum = 0.0
        for score in student_scores:
            total_sum += score

        average_score = total_sum / len(student_scores)
        print(f"\nAverage Score: {average_score:.2f}")



    except ValueError:
        print("Error: Please enter a valid number for count and scores.")


if __name__ == "__main__":
    main()