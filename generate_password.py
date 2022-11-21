##  Password Generator implemented by RA Jocsing for CMSC 124 LEC Term Paper S.Y. 2022-2023
##  This generates passwords of user-defined length and user-defined amount

import secrets 
import time

def gen_pass(length = 30, amount = 10):  

    start = time.time()
    passwords = []                               ## Maintain a list of passwords generated in-session. 
    i = 1
    
    print ("\n")
    print ("Now generating ", amount, " password(s) of length ", length, "...", sep = '')
    print ("\n")
    
    while i <= amount:                           ## Generate times number of unique passwords.
        password = secrets.token_urlsafe(length) ## Get password.

        ## Check if password has already been generated. Repeat iteration if true.
        if password in passwords:
            continue
        
        passwords.append(password)               ## Add generated password to list. 
        print (password)                         ## Print generated password.
        i += 1                                   ## Increment counter.
        
    end = time.time()
    print ("\n")
    print (len(passwords), " password(s) of length ", length, " generated.", sep = '')
    print ("Execution time: ", end-start)
    

   
