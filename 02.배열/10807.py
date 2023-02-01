import sys
a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
c = int(sys.stdin.readline())

d = b.count(c)
print(d)