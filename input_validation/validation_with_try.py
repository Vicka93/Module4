"""
Author:Viktoriia Denys
Program:validation_with_try.py
program validation_with_try.py reads in one person's names, first and last, their age and three scores out of 100.
Taking the three scores and finding the average, storing into a variable.with added input validation using try/except
"""

AMT_OF_SCORES = 3


def average(score1, score2, score3):
    # method average prompting for grades and calculating average score
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError()
    return float((score1 + score2 + score3) / AMT_OF_SCORES)


if __name__ == '__main__':
    # Prompting the user for name and age
    last_name = input("Enter your last name:")
    first_name = input("Enter your first name:")
    age = input("Enter your age:")
    # Declaring a variable to store the answer to the function
    first_score = input("Enter your your first score:")
    second_score = input("Enter your your second score:")
    third_score = input("Enter your your third score:")
    try:
        average_scores = average (int(first_score),int(second_score),int(third_score))

    except ValueError:
        print("\nPlease enter only positive values for scores")

    else:
        print("{}, {} age: {}  average grade: {:0.2f}".format(last_name.capitalize(), first_name.capitalize(),
                                                         age, average_scores))
