# Student Grading System

# This program will calculate the grade of a student based on their score
# It will use conditional statements to determine the grade and print it.

# Function to determine grade based on score
def determine_grade(score):
    """
    Determines the grade based on the score.
    
    Args:
    score (int): The score of the student.
    
    Returns:
    str: The grade of the student.
    """
    # Check if the score is greater than or equal to 90
    if score >= 90:
        return 'A'
    # Check if the score is between 80 and 89
    elif score >= 80:
        return 'B'
    # Check if the score is between 70 and 79
    elif score >= 70:
        return 'C'
    # Check if the score is between 60 and 69
    elif score >= 60:
        return 'D'
    # If the score is below 60
    else:
        return 'F'

# Main function
def main():
    """
    Main function to run the Student Grading System.
    It will prompt the user for their score and display their grade.
    """
    # Prompt the user to enter their score
    score = int(input("Enter your score (0-100): "))
    
    # Validate the input score
    if score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
    else:
        # Determine the grade using the function
        grade = determine_grade(score)
        # Print the result
        print(f"Your grade is: {grade}")

# Execute the main function if this script is run
if __name__ == "__main__":
    main()
