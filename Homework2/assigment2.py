# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Shemar Glanville
# Assignment Number: Assignment 2
# Due Date: 06/19/2026
# Purpose: Read student scores from the given file then calculate each student's
# final average, and display the results in descending order by grade.
# Resources Used: Course notes and instructor material

# Create a list to store student names and averages
student_results = []

# Open and read the input file provided with student names and scores
with open("Assignment2input.txt", "r") as infile:
    for line in infile:
        parts = line.strip().split()

        # The first field is the student's name
        name = parts[0]

        # The remaining fields are scores
        scores = [float(score) for score in parts[1:]]

        # Average of score
        average = sum(scores) / len(scores)

        # Store the name and average in the list
        student_results.append((name, average))

# Sort student averages in descending order
student_results.sort(key=lambda x: x[1], reverse=True)

# Display the results
print("Student Averages (Highest to Lowest)")
for name, average in student_results:
    print(f"{name} {average:.2f}")
