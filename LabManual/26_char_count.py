# Q26. Write a Python program that counts the number of occurrences of the character in the given string using function. 
# Provide two implementations: recursive and iterative.

def count_occurrences_recursive(s, char):
    # Base case: if the string is empty, return 0
    if len(s) == 0:
        return 0
    # Recursive case: check the first character of the string
    # If it matches the target character, increment the count and recurse on the rest of the string
    elif s[0] == char:
        return 1 + count_occurrences_recursive(s[1:], char)
    # If it doesn't match, recurse on the rest of the string
    else:
        return count_occurrences_recursive(s[1:], char)

# Test the recursive function
s = "hello"
char = "l"
print("Recursive count:", count_occurrences_recursive(s, char))

def count_occurrences_iterative(s, char):
    count = 0
    # Iterate through each character in the string
    for c in s:
        # If the character matches the target character, increment the count
        if c == char:
            count += 1
    return count

# Test the iterative function
s = "hello"
char = "l"
print("Iterative count:", count_occurrences_iterative(s, char))
