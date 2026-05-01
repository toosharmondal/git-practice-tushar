def add(a, b):
    try:
        return a+b
    except:
        return "Error: Invalid input"
    

def subtract(a, b):
    try:
        return a-b
    except TypeError:
        return "Error: Invalid input"

def multiply(a, b):
    try:
        return a*b
    except TypeError:
        return "Error: Invalid input"
    
def divide(a, b):
    try:
        return a/b
    except TypeError:
        return "Error: Invalid input"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

