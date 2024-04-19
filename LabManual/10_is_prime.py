# Q10. Write a Python Program to Check Prime Number 

num = int(input("Enter your number:"))
isPrime = True

# num is not a multiple of 2 
if(num % 2 != 0):
    # initial divisor set to 3 (1 is divisor of all hence not considered and 2 is already checked)
    divisor = 3
    while divisor * divisor < num:
        if(num % divisor == 0):
            isPrime = False
            break
        divisor += 2  # move divisor by 2 skipping even values
else:
    isPrime = False

print(f"Is the given number {num} prime? {isPrime}")
