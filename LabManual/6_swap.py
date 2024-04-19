# Q6. Write a Python program to swap values of Two Variables without using third variable. 

num1 = 121
num2 = 345

print(f"Before swapping: num1={num1} num2={num2}")

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After swapping: num1={num1} num2={num2}")
