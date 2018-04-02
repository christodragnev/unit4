#Christo Dragnev
#4/2/18
#quiz4.py

def count(a):
    i = 1
    while i<a:
        print(i)
        i+=1
count(10)

def excitedPrint(a):
    print(a.upper()+'!!!')
excitedPrint('I <3 Programming')

def firstLetter(a):
    for ch in a:
        if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print(ch.upper())
firstLetter("Smedinghoff")

def repeats(a,b,c):
    if a==b or a==c or b==c:
        return True
    else:
        return False

print(repeats(5,6,5))
    