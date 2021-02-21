#!/bin/python3

import math
import os
import random
import re
import sys

# In case we need to make new restrictions
def validate(n):
    
    if 1<= n <= 100:
        return True
    else:
        return False
    
    

def task(n):
    
    if n % 2 != 0:
        
        print('Weird')
            
    else:
        
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n >= 20:
            print("Not Weird")

# def generate():
#     return random.randint(1,100)


if __name__ == '__main__':
    
    n = int(input().strip())
    # n = generate()
    run = validate(n) 
    if run:  task(n)
    