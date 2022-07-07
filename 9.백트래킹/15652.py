import sys

N, M = map(int, sys.stdin.readline().split())

arr = []

def dfs(x) :

    if len(arr) == M :
        print(' '.join(map(str, arr)))
        return

    for i in range(x, N+1) :

        arr.append(i)
        dfs(i)
        arr.pop()


dfs(1)