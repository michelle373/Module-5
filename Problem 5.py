# Michelle Patlan
# 8/13/2022
#Search the internet for how to convert radians to degrees. Write a program to
#compute the conversion given a user input value. Print this value as well as the calculated value
#using the degrees function in the math module.

import math

#radian equation to degree
rad_input = float (input ("Please enter a radian: "))

def rad_input(x):
    x=math.degrees(x)
    return x

print("Value in Degree:",rad_input(1.5708))

rad_input = float (input ("Please enter a radian: "))

def rad_input(x):
    pi_value=math.pi
    degree=(x*180)/pi_value
    return degree
print("The degree of the given radian is :", rad_input(1.5708))
