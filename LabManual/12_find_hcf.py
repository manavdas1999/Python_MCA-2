# Q12. Write a Python Program to Find HCF.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
hcf = 1
smaller = num1 if num1 > num2 else num2
divisor = 2

while divisor < smaller:
    if(num1 % divisor == 0 and num2 % divisor == 0):
        hcf = divisor
    divisor+=1

print(f"HCF of {num1} and {num2} is {hcf}")
