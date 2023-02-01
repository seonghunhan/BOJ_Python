import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

temp = []

def dfs (x) :

    if len(temp) == M :
        print(' '.join(map(str, temp)))
        return

    for i in range (x, N) :
        
        temp.append(arr[i])
        dfs(i)
        temp.pop()


dfs(0)