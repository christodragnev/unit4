#Christo Dragnev
#3/29/18
#stringIntersect.py

def stringIntersect(a,b):
    answer = ''
    for ch in a.lower():
        if ch in b.lower() and ch not in answer:
            answer+=ch
        
    return answer
print(stringIntersect('Mississippi','Pennsylvania'))
