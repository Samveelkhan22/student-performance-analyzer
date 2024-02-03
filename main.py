from grades import all_As, calc_average, get_grade, letter_grade

# THERE ARE NO ERRORS IN THE MAIN
# YOU DO NOT NEED TO CHANGE THE MAIN
#-----main-----
print("Enter 3 test scores:")
first_test = get_grade()
second_test = get_grade()
third_test = get_grade()

print()
all_As(first_test, second_test, third_test)
average = calc_average(first_test, second_test, third_test)
print("Your test average is", average)
letter_grade(average)