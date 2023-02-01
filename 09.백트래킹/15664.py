import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
visited = [False] * N

temp = []

def dfs(x) :

    if len(temp) == M :

        print(' '.join(map(str, temp)))
        return

    y = 0

    for i in range(x, N) :

        if not visited[i] and y != arr[i] :
            
            visited[i] = True
            temp.append(arr[i])
            y = arr[i]
            dfs(i)
            visited[i] = False
            temp.pop()

dfs(0)