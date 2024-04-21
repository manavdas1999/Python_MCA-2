# Q30. Write a python program to know the current working directory and to print all contents of the current directory. 
# What changes we need to make in the program if we wish to display the contents of only 'mysub' directory available in current directory? 

import os

# Function to print contents of a directory
def print_directory_contents(directory):
    print(f"Contents of directory '{directory}':")
    for item in os.listdir(directory):
        print(item)

# Print current working directory
print("Current working directory:", os.getcwd())

# Print contents of current directory
print_directory_contents(os.getcwd())

# To display contents of only 'mysub' directory, change the directory path
subdirectory = 'mysub'
print_directory_contents(subdirectory)


