# Q23. A) Write a Python program to add a key to a dictionary. 
# Sample Dictionary: {0: 100, 1: 200} 
# Expected Result: {0: 100, 1: 200, 2: 300} 

def dict_append(target, key, value):
    target[key] = value

example_dict = {0: 100, 1: 200}
print("Before adding: ", example_dict)
dict_append(example_dict, 2, 300)
print("After adding: ", example_dict)

print("##################################")

# Q23. B) Write a Python program to print a dictionary where the keys are numbers between 1 and 5 (both included) and the values are square of keys. 
# Sample Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 

sample_dict = {i : i**2 for i in range(1,6)}
print(sample_dict)
