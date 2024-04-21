# Q35. Write a python program to illustrate the exception handling. 

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error:", e)
        result = None
    else:
        print("Division successful!")
    finally:
        print("End of division function")
    
    return result

# Example usage
numerator = 10
denominator = 0

result = divide(numerator, denominator)
if result is not None:
    print("Result:", result)
else:
    print("Division by zero error occurred.")
