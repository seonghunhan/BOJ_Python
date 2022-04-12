import sys

A = int(sys.stdin.readline())

for i in range(A) :
    str1, str2 = map(str, sys.stdin.readline().strip().split())
    
    print('Possible' if sorted(str1)==sorted(str2) else 'Impossible')
