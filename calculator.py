#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:58:21 2019

@author: sahilsood
"""

import math

def basic():

# =============================================================================
#     +     for addition
#     -     for subtraction
#     /     for division
#     *     for multiplication
# =============================================================================
    
    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')
    
    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))
    

    if op == '+':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    elif op == '-':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    elif op == '*':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    elif op == '/':
        if b == 0:
            return('Error: Cannot be divided by 0')
        else:
            return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))
    else:
        return("Incorrect operator! Please select from the given options!") 
        
def scientific():
        
# =============================================================================
#     IMPLEMENT THE FOLLOWING OPERATIONS IN THE CALCULATOR
#    
#    ^     for power
#    r     for root
#    %     for modulus
#    !     for factorial 
#    sin   for sin (trig)
#    cos   for cos (trig)
#    tan   for tan (trig)
#    ln    for ln (natural log)
# =============================================================================
   
    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "^, r, %, !, sin, cos, tan, ln" : ')
    if op in '^r%':
        a = int(input('Please type the first number: '))
        b = int(input('Please type the second number: '))
    elif op in '!sincostanln':
        a = int(input('Please type the number: '))

    if op == "^":
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a ** b))
    elif op == "r":
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a ** (1 / b)))
    elif op == "%":
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a % b))
    elif op == "!":
        return(str(a)+'! = '+ str(math.factorial(a)))
    elif op == "sin":
        return ('sin(' + str(a) + ') = ' + str(math.sin(a)))
    elif op == "cos":
        return ('cos(' + str(a) +') = ' + str(math.cos(a)))
    elif op == "tan":
        return ('tan(' + str(a) + ') = ' + str(math.tan(a)))
    elif op == "ln":
        return ('ln(' + str(a) + ') = ' + str(math.log(a)))
    else:
        return("Incorrect operator! Please select from the given options!") 
        

def main():  # Wrapper function

    print("""Choose a calculator
    1. Basic Calculator
    2. Scientific Calculator""")
    choice = int(input('Please choose as 1 or 2: '))

    if choice == 1:
        print(basic())
    elif choice == 2:
        print(scientific())
    else:
        print('Invalid choice! Please select between 1 and 2:')

if __name__ == '__main__':
    main()