# Q8. Write a Python Program for checking whether the given number is an even number or not 

userInput = int(input("Enter your number:"))

if(userInput % 2 == 0):
    print(f"Given number {userInput} is even")
else:
    print(f"Given number {userInput} is odd")
