#Christo Dragnev
#4/2/18
#quiz4.py

def count(a):
    i = 1
    while i<a:
        print(i)
        i+=1

def excitedPrint(a):
    print(a.upper()+'!!!')

def firstLetter(a):
    for ch in a:
        if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            return str(a)-(str(a)-str(ch))
def repeats(a,b,c):
    if a==b or a==c or b==c:
        return True
    else:
        return False

count(10)
excitedPrint('I <3 Programming')
firstLetter("Smedinghoff")
print(repeats(5,6,5))
    