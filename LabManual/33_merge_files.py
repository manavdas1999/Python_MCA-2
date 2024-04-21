# Q33. Write a python program to read line by line from a given files file1 & file2 and write into file3 

def merge_files(rFile1, rFile2, wFile):
    with open(rFile1, 'r') as file1, open(rFile2, 'r') as file2, open(wFile, 'w') as file3:
        # read from file1 and write to file3
        for line in file1:
            file3.write(line)
        # read from file2 and write to file3
        for line in file2:
            file3.write(line)
        
file1 = "file1.txt"
file2 = "file2.txt"
file3 = "file3.txt"
merge_files(file1, file2, file3)

print(f"Contents of '{file1}' and '{file2}' have been merged into '{file3}'.")
