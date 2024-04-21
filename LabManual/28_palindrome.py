# Q28. Write a python program to implement is Palindrome () function to check given string is palindrome or no. 

def palindrome(string):
    low, high = 0, len(string)-1
    while(low <= high):
        if(string[low] != string[high]):
            return False
        low += 1
        high -= 1
    return True
    

userInput = input("Enter string:")

print("Is the given string palindrome? ", palindrome(userInput))
