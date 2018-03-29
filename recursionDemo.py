#Christo Dragnev
#3/29/18
#recursionDemo.py - recursive version of countdown

def countdownr(n):
    if n==0:     #official name: base case
        print('BOOM!')
    else: #recursive step
        print(n)
        countdownr(n-1)

countdownr(15)


