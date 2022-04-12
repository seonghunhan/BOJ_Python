import sys
import math

N, A = map(int, sys.stdin.readline().split())

student = [[0]*2 for _ in range (6)]

for i in range(N) :
    B, G = map(int, sys.stdin.readline().split())
    student[G-1][B] += 1

temp = 0

for i in range(6) :
    for j in range(2) :
        temp += math.ceil(student[i][j]/A)

print(temp)