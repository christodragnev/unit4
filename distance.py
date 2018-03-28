#Christo Dragnev
#3/26/18
#distance.py

def distance(x1,y1,x2,y2):
    dist = (((x2-x1)**2)+((y2-y1)**2))**.5
    return dist
    
print(distance(3,4,-5,2))
