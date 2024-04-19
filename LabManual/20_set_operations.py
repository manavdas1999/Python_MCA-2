# Q20. Write a Python program to Illustrate Different Set Operations. 

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1 | set2
print("Union of sets:", union_set)

# Intersection of sets
intersection_set = set1 & set2
print("Intersection of sets:", intersection_set)

# Difference of sets
difference_set1 = set1 - set2
print("Difference of set1 - set2:", difference_set1)
difference_set2 = set2 - set1
print("Difference of set2 - set1:", difference_set2)

# Symmetric difference of sets
symmetric_difference_set = set1 ^ set2
print("Symmetric difference of sets:", symmetric_difference_set)

# Check if one set is a subset of another
subset_check = set1.issubset(set2)
print("Is set1 a subset of set2?", subset_check)

# Check if one set is a superset of another
superset_check = set1.issuperset(set2)
print("Is set1 a superset of set2?", superset_check)
