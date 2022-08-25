# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 21:42:10 2022

@author: Isabela Cristina
"""

"""This program get two numbers x and y from input and prints x raised to 
the power y and log (base 2) of x"""

import math

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))

z = x
x = x**y
print("X**y =", x)

z = int(math.log(z, 2))
print("log (x) =", z)