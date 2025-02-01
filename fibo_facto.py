def fibo(n):
    t1 = 0
    t2 = 1 
    t3 = 0
    count = 2
    if(n<0):
        print ("Invalid")
        return
    elif(n==1):
        print("fibonacci sequence:", t1)
        return
    else:
        print ("fibonacci sequence:", t1, t2, end = " ")
    
    while(count<num):
        t3 = t1 + t2
        temp = t1
        t1 = t2
        t2 = t3
        count = count+1
       

        print(t3, end = " ") 

num = int(input("Enter the number of terms: "))
fibo(num)

def facto(a):
    if a < 0:
        print("Factorial is not defined for negative numbers.")
        return
    elif a == 0 or a == 1:
        print("Factorial =", 1)
        return
    
    result = 1
    for i in range(2, a + 1):
        result *= i
    
    print(f"Factorial of {a} = {result}")

# Taking input from the user
num2 = int(input("\nEnter a number: "))
facto(num2)
