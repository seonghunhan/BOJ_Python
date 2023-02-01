import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
visited = [False] * N
temp = []

def dfs() :
    
    if len(temp) == M :
        print(' '.join(map(str, temp)))
        return

    for i in range(N) :
        if not visited[i] :
            temp.append(arr[i])
            visited[i] = True
            dfs()
            temp.pop()
            visited[i] = False        

dfs()