import sys

a = list(sys.stdin.readline())
b = list(sys.stdin.readline())

i = 0

while i < len(a) :
    if a[i] in b :
        x = a[i]
        a.remove(x)
        b.remove(x)
        
        i -= 1
    i+=1

print(len(a)+len(b))