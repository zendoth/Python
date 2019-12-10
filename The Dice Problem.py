# -*- coding: utf-8 -*-
"""
@author Zendoth
Website https://github.com/zendoth/Python
Date Tue Dec 10 22:25:15 2019
"""
#Question's website https://practice.geeksforgeeks.org/problems/the-dice-problem/0
#Task: Return the opposite face of a 6 sided dice

class face:
    def __init__(self,number):
        self.number=number
        
    def getOpp(self):
        if(self.number==6):
            return int(1)
        elif(self.number==5):
            return int(2)
        elif(self.number==4):
            return int(3)
        elif(self.number==3):
            return int(4)
        elif(self.number==2):
            return int(5)
        else:
            return int(6)
#print("How many test cases do you want?: ")    
inputs=[]
t=int(input())
for i in range(0,t,1):
    #print("What is the face?")
    f= face(int(input()))
    inputs.append(f)
for i in range(0,t,1):
    #print("The opposite side is: ")
    print(inputs[i].getOpp())