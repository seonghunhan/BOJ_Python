import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

temp = []

def dfs() :
    
    if len(temp) == M :
        print(' '.join(map(str, temp)))
        return

    for i in range(0, N) :
        temp.append(arr[i])
        dfs()
        temp.pop()

dfs()