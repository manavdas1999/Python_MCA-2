# Q29. Write a program to compute the number of characters, words and lines in a file. 

def count(filePath):
    with open(filePath, "r") as file:
        # print(line)  # returns a IO wrapper object
        char_count = 0
        word_count = 0
        line_count = 0
        # iterates over each line in file
        for line in file:
            line_count += 1
            word_count += len(line.split(" "))
            for ch in line:
                if( ch != " "):
                    char_count += 1
        
    return char_count, word_count, line_count
    
filename = 'example.txt' 
chars, words, lines = count(filename)

print("Number of characters:", chars)
print("Number of words:", words)
print("Number of lines:", lines)

