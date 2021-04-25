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
        OPT2()
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
    print("This program solves for the unknown coefficient when converting a scientific number to a new magnitude. \nExample: For 5.00*10^2 = ?*10^0, ? = 500")
    a = float(input("Enter the number you wish to convert (in the form of 'xEy' e.g. 5E2):"))
    b = float(input("Enter the magnitude of the target exponent (in the form of '1Ez' e.g. 1E-3):"))
    x = a/b
    print(f'Your unknown coefficient (x) is = {x}') 
    doneCOMP()
    
def OPT2():
    print("Work in progress")
    doneCOMP()

def OPT3():
    print("Work in progress")
    doneCOMP()
    
#Main Code
menu()
    
    


