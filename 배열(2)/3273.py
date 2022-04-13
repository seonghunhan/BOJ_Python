import sys

a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
c = int(sys.stdin.readline())
d = 0
b.sort()
left = 0
right = a-1

while left < right :
    if b[left] + b[right] == c :
        d += 1
        right -= 1
        continue
    elif b[left] + b[right] != c :
        left += 1

print(d)

