__author__ = 'Aabir'

import random 
import string
import sys


        
def strng(lower, upper, number, specialc):    
    
    for i in range(10):
        print( ''.join(random.choice(upper) + random.choice(lower)) + \
              random.choice(number) + random.choice(specialc), end='' )
        
   
        ''' end = '' removes extra space or newline after a string
        choice function inside the random module provides a random character
        from a list of characters combined as a string''' 
        
def wk(pin):
    
    pwd2 = random.randrange(4)
    result = pin[pwd2]
        
    print(result)
    return
    
    
       

def main(): 
    ptype = input('How strong you want your password to be? ')
    low = string.ascii_lowercase
    upp = string.ascii_uppercase
    dig = string.digits
    sch = '!@#$%^&*()_+'
    
    weakp = ['password', 'pythonista', 'slacker', 'random']
    
    if ptype == 'strong':
        return strng(low, upp, dig, sch)
    
    elif ptype == 'weak':
        return wk(weakp)
        
        
    
    


if __name__ == '__main__': 
    main()
