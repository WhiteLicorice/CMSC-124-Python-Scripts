##  Prime Factor Tree Generator developed by RA Jocsing for CMSC124 LEC Term Paper S.Y. 2022-2023
##  This prints out the factor tree of a positive integer, stopping at its prime factors
##  Utilizes a recursive algorithm, does not actually return a formal binary tree

import math

##  Helper function for retrieving the current greatest factor of n
def find_factor(n):
    ##  Iterate backward from isqrt(n) down to 1 and return i if it divides n cleanly w/o remainder
    for i in range (math.isqrt(n), 0, -1):
        if (n % i) == 0:
            return i

##  Helper function used to verify if a number is a prime
def check_prime(n):
    is_prime = True     ##  Flag -> we assume that n is prime
    
    ##  Since we know that 2 and 3 are prime numbers, we can make a tiny optimization here by forgoing the check for 1-2-3
    ##  Also, for the purposes of this program, it's more convenient to consider 1 as prime
    if n > 3:
        ##  Check if the number is prime by iterating from 2 to isqrt(n) -> see if any number in range cleanly divides n w/o remainder
        for i in range (2, math.isqrt(n) + 1):
            if (n % i == 0):
                is_prime = False    ##  Flag -> since n is composite, we invalidate earlier assumption
                break
    return is_prime

##  Core function for finding the factor tree -> traces program execution by printing out current factors
def find_factor_tree(n, arr_prime_factors):
    new_factor1 = find_factor(n)            ##  Find the left factor
    new_factor2 = int(n/new_factor1)        ##  Find the right factor by dividing n with the left factor
    
    ##  Print out a simple representation of the current factor tree -> simply traces execution, can be commented out safely
    print(n)
    print(new_factor1, " * ", new_factor2)
    
    ##  Base Case: a prime factor has been found -> append current factors to prime factor storage array
    if check_prime(n) == True:
        arr_prime_factors.append(new_factor1)
        arr_prime_factors.append(new_factor2)
        return
    ##  Recursive Case: the current factor can still be decomposed into prime factors
    else:
        find_factor_tree(new_factor1, arr_prime_factors)    ##  Apply recursion to left factor
        find_factor_tree(new_factor2, arr_prime_factors)    ##  Apply recursion to right factor

##  Entry point for the program, used to check for edge cases before passing argument to core function
def main(n = 100):
    ##  Raise an exception for all n's that are less than or equal to zero and n's that are not integers
    if n <= 0 or isinstance(n, int) != True:
        raise Exception("Please input a positive integer.")

    ##  Storage array for the prime factors of n
    prime_factors = [ ]
    
    ##  If the positive integer is a prime, simply print it out, else find its factor tree
    if check_prime(n) == True:
        print(n)
    else:
        find_factor_tree(n, prime_factors)

    ##  Use list comprehension to remove all 1's from the prime factors container
    ##  The list can be wrapped in a sorted() function call if a sorted array of prime numbers is desired
    prime_factors = [number for number in prime_factors if number != 1]

    ##  Print out the prime factors of n
    print(f"The prime factors of {n} are: {prime_factors}")
        
