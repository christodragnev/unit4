#Christo Dragnev
#3/9/18
#functionDemo.py - how to write your own functions

def hw():
    print('Hello, world')
    
    
def double(thingToDouble):
    print(thingToDouble * 2)
    

def bigger(a,b):
    if a>b:
        print(a)
    else:
        print(b)
        
def slope(x1, y1, x2, y2):
    print((y2-y1)/(x2-x1))

slope(1,1,2,2)
        
#bigger(3,4)
#bigger(4,4)
#bigger('Smedinghoff','Sam')
#bigger(True,False)
    
#double(12) #test of the double function
#double('w') #test of double with a string input
#double(False) #test of double with a boolean
#hw() #test of our function
#hw() #another