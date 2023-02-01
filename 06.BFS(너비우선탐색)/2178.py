import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n) :
    graph.append(list(map(int, input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y) :
    que = deque()
    que.append((x,y))

    while que :
        x,y = que.popleft()
        for i in range(4) :
            
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if graph[nx][ny] == 1 :
                    graph[nx][ny] = (graph[x][y] + 1)
                    #graph[0][0] = 0
                    que.append((nx,ny))
                    continue
                
    return graph[n-1][m-1]

print(dfs(0,0))
                
