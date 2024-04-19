# Q17. Consider the list lst=[9,8,7,6,5,4,3]. Write the Python program which performs the following operation. 
#  A. Insert element 10 at beginning of the list. 
#  B. Insert element 2 at end of the list. 
#  C. Delete the element at index position 5. 
#  D. Print all elements in reverse order

lst = [9,8,7,6,5,4,3]
print(f"Before ops: {lst}")
# A.
lst.insert(0, 10)
print("Insert element 10 at beginning of the list: ",lst)

# B.
lst.append(2)
print("Insert element 2 at end of the list: ",lst)

# C.
lst.pop(5)
print("Delete the element at index position 5: ",lst)

# D.
lst.pop(5)
print("Print all elements in reverse order: ",lst[::-1])
