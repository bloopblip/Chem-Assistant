# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:58:38 2021

@author: ellis
"""
import sys

def menu():
    print("Chemistry Assistant Program\nBy Ellison Tong\nThis program has a collection of different chemistry tools to aid in chemistry courses. To begin, enter in a number corresponding to the tool you wish to use.")
    print("1. Scientific Notation Magnitude Conversion Calculator \n2. Temperature Conversion Calculator \n3. Unit Conversion Calculator")
    mainCHOICE = input()
    if mainCHOICE == "1":
        sciNUM()
    if mainCHOICE == "2":
        tempCONVERT()
    if mainCHOICE == "3":
        OPT3()
    if mainCHOICE == "x":
        sys.exit()

def doneCOMP(): #after running a function, directs user to menu or exit
    print("The computation has been completed. Enter 'x' to exit program or 'm' for main menu")
    doneCOMPchoice = input()
    if doneCOMPchoice == "x":
        sys.exit
    if doneCOMPchoice == "m":
        menu()
        
def sciNUM(): #scientific notation magnitude conversion calculator
    print("This tool solves for the unknown coefficient when converting a scientific number to a new magnitude. \nExample: For 5.00*10^2 = ?*10^0, ? = 500")
    a = float(input("Enter the number you wish to convert (in the form of 'xEy' e.g. 5E2):"))
    b = float(input("Enter the magnitude of the target exponent (in the form of '1Ez' e.g. 1E-3):"))
    x = a/b
    print(f'Your unknown coefficient (x) is = {x}') 
    doneCOMP()
    
def tempCONVERT(): #converts a temperature to a different temperature scale
    print("This tool converts a given temperature to different temperature scales. Avaliable scales are celsius, fahrenheit, and kelvin.")
    tempMAG = float(input("Enter in the magnitude of your temperature:"))
    print("Enter in the unit of your temperature (F = fahrenheit, C = celsius, K = kelvin)")
    tempUNITstart = input()
    print("Enter in the unit of your target temperature (F = fahrenheit, C = celsius, K = kelvin)")
    tempUNITend = input()
    #NOTE: switch statements are not avaliable in python
    if tempUNITstart == "C":
        if tempUNITend == "F":
            CEL2FAH = (tempMAG/(5/9))+32
            print(f'Your temperature is equal to {CEL2FAH}')
        if tempUNITend == "K":
            CEL2KEL = tempMAG+273.15
            print(f'Your temperature is equal to {CEL2KEL}')
    if tempUNITstart == "F":
        if tempUNITend == "C":
            FAH2CEL = (tempMAG-32)*(5/9)
            print(f'Your temperature is equal to {FAH2CEL}')
        if tempUNITend == "K":
            FAH2KEL = (tempMAG-32)*(5/9)+273.15
            print(f'Your temperature is equal to {FAH2KEL}')
    if tempUNITstart == "K":
        if tempUNITend == "C":
            KEL2CEL = tempMAG-273.15
            print(f'Your temperature is equal to {KEL2CEL}')
        if tempUNITend == "F":
            KEL2FAH = ((tempMAG-273.15)/(5/9))+32
            print(f'Your temperature is equal to {KEL2FAH}')
    doneCOMP()

def OPT3():
    print("Work in progress")
    doneCOMP()
    
#Main Code
menu()
    
    


