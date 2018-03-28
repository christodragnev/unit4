#Christo Dragnev
#3/28/18
#stringUnion.py

def stringUnion(a,b):
    answer = ''
    for ch in a.lower()+b.lower():
        if ch not in answer:
            answer+=ch
    return answer
print(stringUnion('Mississippi','Pennsylvania'))
