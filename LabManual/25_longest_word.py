# Q25. Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_word(words):
    longest = words[0]
    for word in words:
        if len(longest) < len(word):
            longest = word
    
    return longest

words = ['apple', 'banana', 'orange', 'grapes', 'pear', 'kiwi', 'pineapple', 'strawberry', 'watermelon', 'melon']

print("longest word in given list:", find_longest_word(words))
