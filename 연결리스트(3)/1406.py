import sys

a = list(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline())
d = []


for i in range(b) :
    c = list(sys.stdin.readline().rstrip().split())

    if c[0] == 'L' :
        d.append(a.pop())
    elif c[0] == 'D' :
        a.append(d.pop())
    elif c[0] == 'B' :
        a.pop()
    else : 
        a.append(c[1])
        
a.extend(reversed(d))

print(''.join(a))
