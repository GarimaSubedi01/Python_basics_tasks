#defining functions for required arithmetic operations

def add(a, b):
    result = a + b
    return result

def sub(a, b):
    result = a - b
    return result

def mul(a, b):
    result = a*b
    return result

def div(a, b):
    result = a / b
    return result

#Operations choices
while True:

    print("\nThe operations are: ")
    print("+. Addition ")
    print("-. Subtraction ")
    print("*. Multiplication ")
    print("/. Division ")
    print("E. THE END ")


    operation = input("\nEnter the operator for the operation you want to perform: ")

    

    if operation == '+':
        try: 
             a = float(input("Enter the first operand: "))
             b = float(input("Enter the second operand: "))
             print(f"The sum of {a} and {b} is {add(a,b)}")
        except ValueError:
             print("Enter a valid number")
             continue


    elif operation == '-':
        try: 
             a = float(input("Enter the first operand: "))
             b = float(input("Enter the second operand: "))
             print(f"The difference of {a} and {b} is {sub(a,b)}")
        except ValueError:
             print("Enter a valid number")
             continue
    elif operation == '*':
        try:
             a = float(input("Enter the first operand: "))
             b = float(input("Enter the second operand: "))
             print(f"The product of {a} and {b} is {mul(a,b)}")
        except ValueError:
             print("Enter a valid number")
             continue
    elif operation == '/':
        try: 
             a = float(input("Enter the first operand: "))
             b = float(input("Enter the second operand: "))
             print(f"The result of division of {a} and {b} is {div(a,b)}")

        except ZeroDivisionError:
             print("cannot divide by zero")
             
        except ValueError:
             print("Enter a valid number")
             continue
    elif operation == 'E':
        print("You've ended the program")
        quit()

    