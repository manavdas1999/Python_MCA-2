# Q24. Write a Python program to do the following: 
# A. To Sort a dictionary by key. 
# B. To get the maximum and minimum value in a dictionary. 
# C. To remove duplicates values from Dictionary. 

# A. To Sort a dictionary by key. 
def key_sorted(target):
    sorted_key_list = sorted(target)
    sorted_dict = {key : target[key] for key in sorted_key_list}
    return sorted_dict

# B. To get the maximum and minimum value in a dictionary. 
def max_min_value(target):
    return max(target.values()), min(target.values())
    
# C.To remove duplicates values from Dictionary. 
def remove_duplicate_values(target):   
    unique_dict = {}
    for key, value in target.items():
        if value not in unique_dict.values():
            unique_dict[key] = value
    return unique_dict
    
    
example_dict1 = {7: "seven", 2: "two", 5: "five", 11: "eleven"}
print("Before sorting by keys:", example_dict1)
example_dict1 = key_sorted(example_dict1)
print("After sorting by keys:", example_dict1)

print()

example_dict2 = {"seven":7, "two": 2, "five": 5, "eleven": 11}
print(f"Max and min values:", max_min_value(example_dict2))

print()

example_dict3 = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1, 'f': 3}
print('Original dictionary:', example_dict3)
example_dict3 = remove_duplicate_values(example_dict3)
print('After removing duplicate values:', example_dict3)
