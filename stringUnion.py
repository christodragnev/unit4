#Christo Dragnev
#3/28/18
#stringUnion.py

def stringUnion(a,b):
    answer = ''
    for ch in a and ch in b:
        if ch != answer:
            answer+=str(ch)
            
stringUnion('Mississippi','Pennsylvania')
