''' 
05/02/24
Python class/lab
Q1. WAP to input three numbers from user and print sum of their squares.
Q2. WAP to input no. of days from user and convert it into month and days (assume 30days = 1 month).
Q3. WAP to take three number inputs from user and swap their value without using any extra variable.
Q4. WAP to input three numbers and find the largest one.

'''


# Q1. WAP to input three numbers from user and print sum of their squares.
num1 = int(input("Enter value 1:"));
num2 = int(input("Enter value 2:"));
num3 = int(input("Enter value 3:"));

sum_of_squares = num1**2 + num2**2 + num3**2

print("Sum of squares of given numbers: ", sum_of_squares);

# Q2. WAP to input no. of days from user and convert it into month and days (assume 30days = 1 month).
raw_day_count = int(input("Enter number of days:"))
month_count = raw_day_count // 30
day_count = raw_day_count % 30

print(month_count,"month and", day_count, "days.")


# Q3. WAP to take three number inputs from user and swap their value without using any extra variable.
num1 = int(input("Enter value 1:"))
num2 = int(input("Enter value 2:"))
num3 = int(input("Enter value 3:"))

print("Before: ", num1,num2,num3)

num1 = num1 + num2 + num3
num2 = num1 - num2 - num3
num3 = num1 - num2 - num3
num1 = num1 - num2 - num3

print("After: ", num1,num2,num3)


# Q4. WAP to input three numbers and find the largest one.
num1 = int(input("Enter value 1:"))
num2 = int(input("Enter value 2:"))
num3 = int(input("Enter value 3:"))

greatest = 0

if(num1 > num2 and num1 > num3):
    greatest = num1
else:
    if(num2 > num3):
        greatest = num2
    else:
        greatest = num3

print("Greatest:", greatest)
