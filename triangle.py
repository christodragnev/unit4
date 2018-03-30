#Christo Dragnev
#3/29/18
#triangle.py

def distance(x1,y1,x2,y2):
    dist = (((x2-x1)**2)+((y2-y1)**2))**.5
    return dist
x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))
x3 = float(input('Enter x3: '))
y3 = float(input('Enter y3: '))
a = distance(x1,y1,x2,y2)
b = distance(x1,y1,x3,y3)
c = distance(x2,y2,x3,y3)
s = 1/2*(a+b+c)
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(area)
