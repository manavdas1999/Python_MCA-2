# Q18. Write a Python program which will return the sum of the numbers in the array, returning 0 for an empty array. 
# Except the number 13 is very unlucky, so it does not count and number that come immediately after 13 also do not count. 
# Example : [1, 2, 3, 4] = 10 , [1, 2, 3, 4, 13] = 10 , [13, 1, 2, 3, 13] = 5 

def count_sum(lst):
    if len(lst) == 0:
        return 0
    
    list_sum = 0
    i = 0
    while i < len(lst):
        if lst[i] == 13:
            i+=2
            continue
        else:
            list_sum += lst[i]
        i+=1
    
    return list_sum

nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 3, 4, 13]
nums3 = [13, 1, 2, 3, 13]

print(f"{nums1} = {count_sum(nums1)}")
print(f"{nums2} = {count_sum(nums2)}")
print(f"{nums3} = {count_sum(nums3)}")

