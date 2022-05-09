import sys

room = [0]*21

for i in range(21) :
    room[i] = i


temp1 = []
temp2 = []

for i in range (10) :
    a, b = map(int, sys.stdin.readline().split())
    temp1 = room[a:b+1]
    temp2 = reversed(temp1)
    room[a:b+1] = temp2

for i in range(1,21) :
    print(room[i], end=' ')