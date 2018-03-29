#Christo Dragnev
#3/29/18
#warmup12.py - function that returns the GCF of two numbers

def gcf(a,b):
    i=b
    while i>0:
        if a%i==0 and b%i==0:
            return i
        i-=1
print(gcf(12,15))


