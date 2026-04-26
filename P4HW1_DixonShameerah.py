# Shameerah Dixon
# April 26, 2026
# p4hw1.py
# Calculating scores

# Ask user for number of scores to enter
num_scores = int(input("How many scores do you want to enter? "))
    
# Empty list for scores
score_list = []

# Collect scores
for i in range(num_scores):
        # Ask for score with index display
        score = float(input(f"Enter score #{i + 1}: "))
        
        # Loop validation
        while score < 0 or score > 100:
            print("\nINVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            score = float(input(f"Enter score #{i + 1} again: "))
        
        # Append valid score to list
        score_list.append(score)

# Calculate results
lowest_score = min(score_list)
    
# Remove lowest score
score_list.remove(lowest_score)
    
# Calculate average of modified list
avg_score = sum(score_list) / len(score_list)

# Calculate averages
if avg_score >= 90:
        grade = 'A'
elif avg_score >= 80:
        grade = 'B'
elif avg_score >= 70:
        grade = 'C'
elif avg_score >= 60:
        grade = 'D'
else:
        grade = 'F'

# Display results
print("\n--------------Results-----------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {avg_score:.2f}")
print(f"Grade         : {grade}")
print("--------------------------------")

