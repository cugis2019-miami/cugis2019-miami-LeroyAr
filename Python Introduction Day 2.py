#print(53)
#53

#"Hello World"

#print(54)
#Print(54)

#(8/9) * 3

#print("The division of 5 by 3 is" , 5/3)

#Create function to sum any two numbers

def sum(a,b,c):
    sum = a + b + c
    print(sum)

sum(2,3,4)

def areaTriangle(b,h):
    areaTriangle = (1/2) * b * h
    print("The area of the triangle is:",areaTriangle)

areaTriangle (4,6)

def areaSquare(a):
    areaSquare = a ** 2
    print (areaSquare)
    
areaSquare(4)

#print("box",=5) wrong syntax

box = 5
box = box + 5
print("There are",box,"bars in the box")

#chocolate types
d = "dark"
m = "milk"
w = "white"

print(d,m,w)

#"D" = dark

def greeting(name):
    print("Good afternoon", name + ", it was very nice to meet you today")

greeting("Leroy")

import math
def areaOctagon(a):
    areaOctagon = 2*(1+math.sqrt(2))*(a**2)
    print (areaOctagon)
    
areaOctagon(4)

dir(math)

math.factorial(0)

math.remainder(5,3)
# math.remainder(5,0) Cannot divide by 0

def cube(x):
    cube = math.pow(x,(1/3))
    print("The cube root of",x,"is",cube)
    
cube(8)

print("Please enter a value for x")
x = 8
def cube(x):
    cube = math.pow(x,(1/3))
    print("The cube root of",x,"is",cube)

cube(x)

