# Q9. Write a Python Program to check leap year 

year = int(input("Enter year:"))
isLeapYear = False

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            isLeapYear = True
    else:
        isLeapYear = True

print(f"Is year {year} leap? {isLeapYear}")
