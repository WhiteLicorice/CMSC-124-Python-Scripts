## Simple Prime Generation algorithm implemented by RA Jocsing for CMSC 124 LEC Term Paper S.Y. 2022-2023
## This generates a list of primes from low to high inclusive
## Intuitively, low and high must be both integers and low < high, else there will be logic errors

import math

def gen_primes(low = 1, high = 1000):
    ##  Check if low < high holds true, raise an exception if not
    if low > high:
        raise Exception("Low must be less than high.")
    ##  Iterate from low to high, find primes, and print them out
    for num in range(low, high + 1):
        is_prime = 1
        if num > 1:
            for i in range(2, math.isqrt(num) + 1):
                if (num % i) == 0:
                    is_prime = 0
                    break
            if is_prime == 1:
                print (num)
