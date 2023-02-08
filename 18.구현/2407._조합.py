import math

n, m = map(int,input().split())

x = math.factorial(n) // (math.factorial(n - m) * math.factorial(m))

print(int(x))