# Q19. Write a Python program to Check Whether a String is Palindrome or Not 

userInput = input("Enter a string: ").lower()
isPalindrome = userInput == userInput[::-1]
print(f"Is given string '{userInput}' palindrome? {isPalindrome}")
