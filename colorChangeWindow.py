#Christo Dragnev
#3/9/18
#colorChangeWindow.py

from ggame import *
from  random import randint

black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)

def mouseClick(event):
    num = randint(1,3)
    if num==1:
        redRectangle = RectangleAsset(800,800,blackOutline,red)
        Sprite(redRectangle)
    elif num==2:
        greenRectangle = RectangleAsset(800,800,blackOutline,green)
        Sprite(greenRectangle)
    else:
        blueRectangle = RectangleAsset(800,800,blackOutline,blue)
        Sprite(blueRectangle)

App().listenMouseEvent('click',mouseClick)
App().run()
