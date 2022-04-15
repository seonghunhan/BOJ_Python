import sys

a = list(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline())
d = []


for i in range(b) :
    c = list(sys.stdin.readline().rstrip().split())

    if c[0] == 'L' :
        if a :    
            d.append(a.pop())
    elif c[0] == 'D' :
        if d :
            a.append(d.pop())
    elif c[0] == 'B' :
        if a :
            a.pop()
    else : 
        a.append(c[1])
        
a.extend(reversed(d))

print(''.join(a))
