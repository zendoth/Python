"""
@author Zendoth
Website https://github.com/zendoth/Python
Date Tue Sep 10 15:14:18 2019
"""
#Question's website https://practice.geeksforgeeks.org/problems/multiply-left-and-right-array-sum/0
#Task: Takes an array, seperates it into left and right arrays. Adds them up and then multiplies the 2 arrays

t=int(input()) #the number of test cases
dic= {} #a place to store the test cases in individual indexes for ease of organisation
for i in range(0,t):
    n=int(input())#number of elements in the ith array
    dic[i]=[]
    element= str(input())
    temp=""    
    count=1
    for j in element:
        if(j is not " "):
            temp=temp+j
        if(j is " " or count==len(element)):#need to add the or as it needs to read the last integer as well
            temp_num=int(temp)
            dic[i].append(temp_num)
            temp=""
        count+=1

for i in range(0,len(dic)):
    n=len(dic[i])
    value=0 #initializes the 2 integers to multiply to 0 at first
    value2=0
    for j in range(0,n):
        if(j<n//2):
            value+=dic[i].pop(0) #makes the list shorter by popping and hence only needs to pop index 0 each time
        elif(j>=n//2):
            value2+=dic[i].pop(0)
    print(value*value2)
    
