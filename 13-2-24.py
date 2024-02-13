'''
Python class/lab
Q1. WAP to input n numbers from user to find even sum and odd sum respectively.
Q2. WAP to print pattern:
1
12
123
1234

1
22
333
444
'''

# Q1. WAP to input n numbers from user to find even sum and odd sum respectively.
no_of_inputs = int(input("Enter no. of numbers: "))
even_sum =0;
odd_sum =0;
while(no_of_inputs >0):
    user_in = int(input("Enter value: "))
    if(user_in % 2 == 0): even_sum += user_in
    else: odd_sum += user_in
    no_of_inputs -= 1

print("Even Sum:",even_sum)
print("Odd Sum:",odd_sum)
