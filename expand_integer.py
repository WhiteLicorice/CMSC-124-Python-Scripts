##  Integer Expansion implemented by RA Jocsing for CMSC 124 LEC Term Paper S.Y. 2022-2023
##  This transforms an integer into expanded form
##  e.g. 69420 => 60000 + 9000 + 400 + 20 + 0 or 0 + 20 + 400 + 9000 + 60000

import math

##  An implementation of Integer Expansion using string manipulation in Python
def exp_str(n = 69420):
    temp = str(n) [::-1] #  Fancy way of reversing a number cast to a string
    base = 10
    i = 0

    ##  Iterate through the string, printing digits out according to place value
    for digit in (temp):
        print(int(digit) * pow(base, i), end = "")
        if i != (len(temp) - 1):
            print(" + ", end = "")
        i += 1

##  A more traditional implementation of Integer Expansion using arithmetic
def exp_mod(n = 69420):

    ##  Edge case for handling the case when n = 0
    if (n == 0):
        print("0")
        return
    
    ##  Store a local copy of the parameter n to avoid mutation
    temp = n
    base = 10
    count_digit = 0
    
    ##  Counts the number of digits in a positive integer by dividing it by 10 until it reaches 0
    while temp != 0:
        temp = int(temp) / 10
        if temp != 0:
            count_digit += 1

    ##  Retrieve another local copy of the parameter n
    temp = n
    ##  Adhere to 0-indexed conventions by subtracting 1 from counter
    count_digit -= 1

    ##  Iteratively apply a reduction mask to n -> decompose into expanded notation
    while count_digit >= 0: 
        power = math.pow(base, count_digit)
        factor = int(int(temp / power) * power)
        print (factor, end = "")
        if count_digit != 0:   
            print(" + ", end = "")
        temp -= factor
        count_digit -= 1
