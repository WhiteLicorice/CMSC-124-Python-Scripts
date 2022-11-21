## Simple iterative factorial algorithm implemented by RA Jocsing for CMSC 124 LEC Term Paper S.Y. 2022-2023
## This program finds the factorial of a user-input
## Intuitively, we know that factorials only exist for non-negative integers

def factorial(n = 10):
    ##  Check for possible type errors
    if (n < 0) or (str(n).isdigit() != True):
        raise Exception("Input must be a non-negative integer.")
    
    ##  Handle edge case where n = 0
    if n == 0:
        print("0! = 1")
        return

    ##  Find the factorial of n iteratively, i.e. product = 1 * 2 * 3 * 4 * ... * n
    product = 1
    for factor in range(1, n + 1):
        product = product * factor

    ##  Print out the result
    print (f"{n}! = {product}")
