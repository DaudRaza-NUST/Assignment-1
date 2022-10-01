# Defining a function for factorial. Had to understand and lookup recursion for
# this example. Could not solve it manually. 
a = int(input("Enter the Number for Factorial: "))
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
print(factorial(a))