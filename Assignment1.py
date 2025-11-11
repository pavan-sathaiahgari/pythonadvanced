# Write a program to for the below:
# a. The program should take inputs for Five Subjects. English, French, Mathematics, Physics, Chemistry
# b. Maximum Marks is 500 (100 Per Subject)
# c. Calculate the Percentage Scored

# 70Subject_marks = float(input('Enter English marks =' + 'Enter French marks =' + 'Enter Mathemaatics marks =' + 'Enter Physics marks =' + 'Enter Chemistry marks ='))

english = float(input("Enter marks for English (out of 100): "))
french = float(input("Enter marks for french (out of 100): "))
maths = float(input("Enter marks for maths (out of 100): "))
physics = float(input("Enter marks for physics (out of 100): "))
chemistry = float(input("Enter marks for chemistry (out of 100): "))

total_marks = english + french + maths + physics + chemistry
max_marks = 500
percentage = total_marks / max_marks * (100) 
print('percentage of all subjects =' , percentage)