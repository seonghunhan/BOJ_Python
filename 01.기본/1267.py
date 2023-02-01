import sys
a = int(sys.stdin.readline())
b = list(map(int, input().split()))

c = sum(b)
y = 0
m = 0

for i in range(len(b)) :
    y += (b[i] // 30) * 10 + 10

for i in range(len(b)) :
    m += (b[i] // 60) * 15 + 15

if y < m :
    print("Y "+str(y))
elif y > m :
    print("M "+str(m))
else : 
    print("Y M "+str(y))