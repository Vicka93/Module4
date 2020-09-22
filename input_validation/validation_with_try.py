"""
Author:Viktoriia Denys
Program:validation_with_try.py
program validation_with_try.py reads in one person's names, first and last, their age and three scores out of 100.
Taking the three scores and finding the average, storing into a variable.
"""

AMT_OF_SCORES = 3


def average(score1,score2,score3):
    # method average prompting for grades and calculating average score

    return float((score1 + score2 + score3) / AMT_OF_SCORES)


if __name__ == '__main__':
    # Prompting the user for name and age
    last_name = input("Enter your last name:")
    first_name = input("Enter your first name:")
    age = input("Enter your age:")
    # Declaring a variable to store the answer to the function call
    average_scores = average(10,90,100)

    print("{}, {} age: {}  average grade: {}".format(last_name.capitalize(),
          first_name.capitalize(), age, average_scores))
