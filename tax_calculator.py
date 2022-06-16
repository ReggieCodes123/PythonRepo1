# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 18:24:05 2022

@author: johns
"""

income = float(input("Enter the annual income: "))

if income<=85528 :
    tax= (income*.18)-556.02
    if tax<0:
        tax = 0.0
    
    
elif income>85528:
    tax=14839.02+.32*(income %85528)


tax = round(tax, 0)
print("The tax is:", tax, "thalers")