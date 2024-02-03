def all_As(score1, score2, score3):
    if score1 == 100 and score2 == 100 and score3 == 100:
        print("You scored all As")
    else:
        print("You did not score all As")

def calc_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

def get_grade():
    return int(input("Enter test score: "))

def letter_grade(average):
    if average >= 90:
        print("Your letter grade is A")
    elif average >= 80:
        print("Your letter grade is B")
    elif average >= 70:
        print("Your letter grade is C")
    elif average >= 60:
        print("Your letter grade is D")
    else:
        print("Your letter grade is F")


# Test Case: 100, 100, 100
# Purpose: Verify that the program correctly recognizes and handles the scenario when all test scores are perfect (100).
# Why: This test case is essential to ensure that the program accurately detects and responds to a situation where a student scores the highest possible grade in each test. It validates the "You scored all As" message.

# Test Case: 75, 80, 90
# Purpose: Confirm that the program calculates the average accurately and assigns the correct letter grade for a varied set of scores.
# Why: This test case is designed to check the mathematical correctness of the average calculation and the appropriate assignment of letter grades. It helps ensure the program functions correctly with diverse input.

# Test Case: 60, 70, 80
# Purpose: Test the lower boundaries for different letter grades, ensuring the program handles scores near grade thresholds.
# Why: Examining cases near the grade thresholds is crucial to verify the program's accuracy in assigning letter grades. This test case ensures that the program responds appropriately to scores on the verge of different grade categories.