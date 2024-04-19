# Q16. Write a Python program which takes a list and returns a list with the elements "shifted left by one position" so [1, 2, 3] yields [2, 3, 1]. 
# Example: [1, 2, 3] → [2, 3, 1] & [11, 12, 13] → [12, 13, 11] 

nums = [11, 12, 13]

print("Before left shifting: ", nums)

firstIndexValue = nums[0]
for i in range(len(nums)-1):
    nums[i] = nums[i+1]
    
nums[-1] = firstIndexValue

print("After left shifting: ", nums)
