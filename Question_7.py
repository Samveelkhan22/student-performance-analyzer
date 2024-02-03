def letter_grade(average):
    if average >= 90:
        print("Your letter grade is A")
    elif 80 <= average < 90:
        print("Your letter grade is B")
    elif 70 <= average < 80:
        print("Your letter grade is C")
    elif 60 <= average < 70:
        print("Your letter grade is D")
    elif average < 60:
        print("Your letter grade is F")