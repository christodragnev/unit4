#Christo Dragnev
#3/29/18
#triangle.py

def Area(x1,y1,x2,y2,x3,y3):
    a = (((x2-x1)**2)+((y2-y1)**2))**.5
    c = (((x3-x1)**2)+((y3-y1)**2))**.5
    b = (((x3-x2)**2)+((y3-y2)**2))**.5
    s = 1/2*(a+b+c)
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area
print(Area(3,4,-5,2,-7,1))
