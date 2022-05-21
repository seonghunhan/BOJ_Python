#G번
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = [] # 통분한 분자리스트

x = 0
y = 1 # 분모

for i in arr :
    y *= i

for i in arr :
    arr2.append(y / i)

print((x/y) + 1)


# 조각케이크 문제인데 gg