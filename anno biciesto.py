# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 21:24:53 2022

@author: ramos
"""
year = 2032  #el año que queremos comprobar

if year % 4 != 0: #no divisible entre 4
	print("Falso")
elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("Verdadero")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("Falso")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
	print("Verdadero")
    