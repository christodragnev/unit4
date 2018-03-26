#Christo Dragnev
#3/26/18
#printSquares.py

def printSquares(h,b):
    for i in range (h,b):
        print('+','- - + '*b)
        print('|     '*(b+1))
        i+=1
    print('+','- - + '*b)

printSquares(2,4)

