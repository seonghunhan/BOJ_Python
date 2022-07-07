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

    x = 0 # 중복방지변수

    for i in range(0, N) :
        
        if not visited[i] and x != arr[i] :
            visited[i] = True
            temp.append(arr[i])
            x = arr[i]
            dfs()
            temp.pop()
            visited[i] = False

dfs()