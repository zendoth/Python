#Author Zendoth
#Website https://github.com/zendoth/Python
#Date 09 September 2019
#This Program takes in the users choice of calculation and returns back the calculated value using an
#implementation of switch and case statements using dictionaries within functions
import math

def invalidChoice():
    print("Invalid choice")

def circumferenceOfCircle():
    radius= float(input("What is the radius of the circle?\n"))
    circumference= 2*math.pi*radius
    return circumference

def areaOfCircle():
    radius= float(input("What is the radius of the circle?\n"))
    area= radius**2*math.pi
    return area

def perimeterOfRectangle():
    length= float(input("What is the length?\n"))
    breadth= float(input("What is the breadth?\n"))
    perimeter= length*2+breadth*2
    return perimeter

def areaOfRectangle():
    length= float(input("What is the length?\n"))
    breadth= float(input("What is the breadth\n"))
    area=length*breadth
    return area

#Dictionary implementation of case statement
def calculate(choice):
    choiceSelect= {
            "A" : circumferenceOfCircle,
            "a" : circumferenceOfCircle,
            "B": areaOfCircle,
            "b": areaOfCircle,
            "C": perimeterOfRectangle,
            "c": perimeterOfRectangle,
            "D": areaOfRectangle,
            "d": areaOfRectangle
            }
    func= choiceSelect.get(choice,invalidChoice)
    return func

def printAnswer(choice,answer):
    prints={
        "A": "The circumference of the circle is",
        "a": "The circumference of the circle is",
        "B": "The area of the circle is",
        "b": "The area of the circle is",
        "C": "The perimeter of the rectangle is",
        "c": "The perimeter of the rectangle is",
        "D": "The area of the rectangle is",
        "d": "The area of the rectangle is"
    }
    print(prints.get(choice),answer)
 
#Main code
print("Please input your choice below \n",\
      "A. Circumference of circle\n",\
      "B. Area of circle\n",\
      "C. Perimeter of a rectangle\n",\
      "D. Area of a rectangle")
choice= str(input())

answer= calculate(choice)()
if(answer is not None):    
    printAnswer(choice,answer)
