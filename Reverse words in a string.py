"""
@author Zendoth
Website https://github.com/zendoth/Python
Date Mon Sep  9 15:33:15 2019
"""
#Question's website https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0
#Task reverse the order of words in a string without reversing the alphabets within the word
#t= int(input("How many sentences would you like to reverse?\n"))
t=int(input())
while(t<1 or t>100):
    t= int(input())
    #t= int(input("Please give a t value greater than 0 and 100 or less \n"))
sentence={}
for i in range(0,t):
    #print("\nPlease input the ",i," sentence\n")
    sentence[i]= str(input())
    while(len(sentence[i])<1 or len(sentence[i])>2000):
        #sentence[i]= str(input("\nI need a sentence of length less than 2001!\n"))
        sentence[i]= str(input())

master_dict={}
#creates a dictionary of dictionaries where the inner dictionary holds the words and the outer dictionaries hold the sentence
for i in range(0,t):
    x= sentence[i]
    temp=""
    temp_dict={}
    k=0
    count=1
    for j in x:
        if(j is not "."):
            temp=temp+j
        if(j is "." or count==len(x)):
            temp_dict[k]=temp
            temp=""
            k+=1
        count+=1
    master_dict[i]=temp_dict

#reverses the order of inner dictionaries but doubles the length of the dictionary in the process
for i in range(0,len(master_dict)):
    length=len(master_dict[i])
    count=0
    for j in range(0,length):
        last=len(master_dict[i])
        master_dict[i][length+count]=master_dict[i][j]
        count+=1
    count=0
    for j in range(0,length):
        master_dict[i][length-count-1]=master_dict[i][length+count]
        count+=1

#deletes the extra dictionaries created
for i in range(0,len(master_dict)):
    length=len(master_dict[i])
    length=length//2
    length=int(length)
    count=0
    for j in range(0,length):
        x=length+count
        del master_dict[i][x]
        count+=1
 
#Below translates the dictionary back to a printed string         
length=len(master_dict)
for i in range(0,length):
    new_string=""
    for j in range(0,len(master_dict[i])):
        new_string=new_string+master_dict[i][j]+"."
    new_string=new_string[:-1]
    master_dict[i]=new_string
for i in range(0,length):
    print(master_dict[i])

