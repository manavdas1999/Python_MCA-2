# Q27. Write a Python program to find reverse of given number using user defined function. 

def num_reverse(num):
    rev = 0
    while(num > 0):
        rev = rev*10 + num % 10
        num = num // 10
    return rev
    
num = int(input("Enter a number:"))
reversed_num = num_reverse(num)
print(reversed_num)    
