#Christo Dragnev
#3/29/18
#multiply.py

from random import randint

def encouragingMessage():
    randint(1,3)
    if randint(1,3)==1:
        print('Watch out world, here comes the next great multiplier')
    elif randint(1,3)==2:
        print('Next Einstein?')
    else:
        print('You are incredible!')
    
    
i=0
while i<5:
    a = randint(1,12)
    b = randint(1,12)
    answer = int(input('What is '+str(a)+ '*'+str(b)+ '?'))
    if answer == a*b:
        i+=1
    else:
        print('Sorry, incorrect')
    if i==5:
        encouragingMessage()

            
    
        
    
