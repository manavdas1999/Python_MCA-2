# Q22. Write a Python program to sort a dictionary by value.

example_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grapes': 3}

print("Before Sorting by values:", example_dict)

items = list(example_dict.items())

for i in range(len(items)):
    for j in range(i+1, len(items)):
        if(items[i][1] > items[j][1]):
            items[i], items[j] = items[j], items[i] # swapping

# converting list of tuples to dict
sorted_dict = dict(items)
print("After Sorting by values:", sorted_dict)
