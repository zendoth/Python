"""
@author Zendoth
Website https://github.com/zendoth/Python
Date Thu Jan  2 20:03:36 2020
"""

#Question's website https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0
#Task Given an unsorted array arr[] of size N, rotate it by D elements (clockwise)

def rotate(x,d):
    for i in range(0,d):
        x.append(x[i])    
    x=x[d:]
    return x
t=int(input())
z=[]
for i in range(0,t):
    b,d=input().split()
    b=int(b)
    d=int(d)
    x=[]
    x.append(input())
    x=x[0].split()
    z.append(rotate(x,d))
for i in z:
    for j in i:
        print(j, end=' ')
    print()