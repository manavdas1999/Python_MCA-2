# Q15. Write a Python program to generate list of Fibonacci number up to n Fibonacci numbers.

# using tail recursion

def fibo(n, terms=[0,1]):
    # only triggers if n is given 0
    if(n == 1): 
        return [0]
    # exit case of recursion
    if(n == 2): 
        return terms
    # recursive case
    # adding last term and second last term and appending the result in list
    terms.append(terms[-2] + terms[-1])
    return fibo(n-1, terms)
    
userNum = int(input("Enter terms of finonacci sequence:"))
print(fibo(userNum))
