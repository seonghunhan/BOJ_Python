import sys

N, M = map(int, sys.stdin.readline().split())

dicts = {}

for i in range(N) :
    id, password = map(str, input().split())

    dicts[id] = password



for i in range(M) :
    x = sys.stdin.readline().rstrip()
    print(dicts[x])
    
# for i in range(M) :
#     print(dicts[arr[i]])