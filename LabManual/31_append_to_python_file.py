# Q31. Write a python program to append data to an existing file 'python.py'.
# Read data to be appended from the user. Then display the contents of entire file. 

# Function to append data to a file
def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data)

# Function to read and display the contents of a file
def display_file_contents(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        print("Contents of '{}':".format(filename))
        print(contents)

# File to append data to
filename = 'python.py'

# Read data to append from the user
data_to_append = input("Enter data to append to the file: ")

# Append data to the file
append_to_file(filename, data_to_append)

# Display the contents of the entire file
display_file_contents(filename)
