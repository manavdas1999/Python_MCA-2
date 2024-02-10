'''
07/02/24
Python class/lab
Q1. WAP to check whether the number is even or odd.
Q2. WAP to check whether the year is leap or not.
'''

# Q1. WAP to check whether the number is even or odd.
num = int(input("Enter a number:"))
isEven = False;
if(num%2 == 0): isEven=True
print("Given Number is: ", isEven)

# Q2. WAP to check whether the year is leap or not.
year = int(input("Enter the year:"))
isLeap = False
if(year%400 == 0): isLeap=True
else:
    if(year%4==0 and year%100 !=0): isLeap=True

print("Year is leap? ", isLeap)
