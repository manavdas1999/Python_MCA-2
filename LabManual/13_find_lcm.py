# Q13. Write a Python Program to Find LCM. 

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

greater = num1 if num1 > num2 else num2
lcm = 0

while(True):
    if((greater % num1==0) and (greater % num2==0)):
        lcm = greater
        break
    greater+=1

print(f"LCM of {num1} and {num2} is {lcm}")     
