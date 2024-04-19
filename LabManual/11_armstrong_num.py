# Q11. Write a Python program to check whether the given no is Armstrong or not 

num = int(input("Enter your number:"))
originalNum = num
cubeSum = 0
isArmStrong = False

while(num > 0):
    cubeSum += (num % 10)**3  # cube the unit values
    num = num // 10  

if(cubeSum == originalNum):
    isArmStrong = True

print(f"Is given number {originalNum} an Armstrong number? {isArmStrong}")

