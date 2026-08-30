# Module 8 Assignment - smart Voting & Student managemnet system

# step -2
# program introduction

print("=" * 60)
print("Welcome to Smart Voting & Student Management System")
print("=" * 60)
print()


# step-3 
# Vting Data Input
print("--- VOTING SYSTEM ---")
num_voters = int(input("HOW MANY VOTERS WILL VOTE? "))

#List to store votes
votes = []

# Collect votes from each voter

for i in range(num_voters):
    candidate = input(f"Voter {i+1}: Enter candidate name: ").strip()
    votes.append(candidate)
    
print(f"\nVotes collected: {votes}")
print()

#step-4
#Frequency counter using dictinary
print("--- COUNTUNG VOTES ---")

# Create an empty dictionary to count votes 
vote_count ={}

# Loop through votes list and count each candidate 
for candidate in votes:
    if candidate in vote_count:
        vote_count[candidate] = vote_count[candidate] +1 
    else:
        vote_count[candidate] = 1
        
print("Vote Count Dictinary :", vote_count)
print()

#step5 
#display vote results 
print("--- VOTE RESULTS ---")
for candidate, count in vote_count.items():
    print(f"{candidate} : {count}")
print() 

#step6
#winner detection
print("--- WINNER DETECTION ---")

#find the candidate with macimum votes 
max_votes = 0
winner = None

for candidate, count in vote_count.items():
    if count > max_votes:
        max_votes = count
        winner = candidate # this line shoul be indented properly 

print(f"Winner is Candidate: {winner} with {max_votes} votes")
print()

while True:
    search_choice = input("Do you want search for a candidate? (yes/no): "). lower()
    
    if search_choice == 'no':
        break
    elif search_choice == 'yes':
        search_name = input("Enter candidate name to search: ").strip()
        
        # search through the dictionary 
        found = False
        for candidate, count in vote_count.items():
            print(f"Candidate '{candidate}' found!")
            print(f" Tota; votes: {count}")
            found = True
            break
        if not found:
            print(f" Candidate '{search_name}' not found in the votin system.")
            print()
        else:
            print("Invalid input! please enter 'yes' or 'no")
            print()
                
#summary 
print("=" * 60)
print("VOTING SYSTEM SUUMMARY")
print("=" * 60)
print(f"Total Voters: {len(votes)}")
print(f"Total Candidates: {len(vote_count)}")
print(f"Winner: {winner} ({max_votes} votes)")
print("=" * 60)
                