#1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements

# To get year (integer input) from the user
yr=int(input("Enter a year : "))

#For direct declaration of value we use assignment operator and a variable
'''yr=2024'''

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (yr%400==0 and yr%100==0):
    print("{0} is a leap year".format(yr))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (yr%4==0 and yr%100!=0):
    print("{0} is a leap year".format(yr))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(yr))