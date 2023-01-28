import sys
input = sys.stdin.readline

N, M = map(int,input().split())

unHeard = []
unSeen = []

for _ in range(N) :
    a = input().rstrip()
    unHeard.append(a)
    
for _ in range(M) :
    a = input().rstrip()
    unSeen.append(a)

a = list(set(unHeard) & set(unSeen))
a.sort()
#a = sorted(a, key = lambda x : x[0])
print(len(a))
print('\n'.join(a))