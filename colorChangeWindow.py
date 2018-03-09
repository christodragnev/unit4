#Christo Dragnev
#3/9/18
#colorChangeWindow.py

from ggame import *
from  random import randint

1 = Color(0xFF0000,1) #this is the color red
2 = Color(0x00FF00,1)
3 = Color(0x0000FF,1)

def listenMouseEvent(a):
    print(a)
listenMouseEvent(randint(0,3))

App().listenMouseEvent('click',mouseClick)
App.run()
