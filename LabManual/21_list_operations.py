import math

def list_sum(lst):
    list_sum = 0
    for i in lst:
        list_sum += i
    
    return list_sum

def list_multiply(lst):
    list_multiply = 1
    for i in lst:
        list_sum *= i
    
    return list_multiply

def list_max(lst):
    max_item = lst[0]
    for item in lst:
        if(item > max_item) max_item = item
    return max_item
    
def list_min(lst):
    min_item = lst[0]
    for item in lst:
        if(item < min_item) min_item = item
        
    return min_item

def remove_duplicates(lst):
    checked = []
    for i in lst:
        if i not in checked:
            checked.append(i)
    
    lst = checked

def isEmpty(lst):
    return len(lst)==0


def select_random_item(lst):
    randomIndex = math.floor(math.random() * len(lst))
    return lst[randomIndex]
    
def copy_list(lst):
    copy = []
    for i in lst:
        copy.append(i)
    return copy

def second_max(lst):
    max_val = 0
    next_max_val = 0
    for i in lst:
        if(i > max_val):
            next_max_val = max_val
            max_val = i
            
        elif i > next_max_val and i != max_val:
            next_max_val = i
    
    return next_max_val

def second_min(lst):
    min_val = 0
    next_min_val = 0
    for i in lst:
        if(i < min_val):
            next_min_val = min_val
            min_val = i
            
        elif i < next_min_val and i != min_val:
            next_min_val = i
    
    return next_min_val     
    
def remove_item(lst, index):
    copy = []
    for i in range(len(lst)):
        if(i == index):
            continue
        copy.append(lst[i])
    print(copy)

def insert_item(lst, index, item):
    lst.append(0) # to increase space
    for i in range(index, len(lst)-1):
        lst[i+1] = lst[i]
    lst[index] = item


nums = [1, 2, 3, 4, 5, 6, 7, 8]
