import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

graph = []
visited = []
max_result = 0
fail_result = 0
que = deque()

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs() :
    
    while que :
        z,x,y = que.popleft()

        for i in range(6) :

            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m :
                if not visited[nz][nx][ny] and graph[nz][nx][ny] == 0 :
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    visited[nz][nx][ny] = True
                    que.append((nz,nx,ny))

for i in range(h) :
    temp = [list(map(int, sys.stdin.readline().split())) for _ in range (n)]
    temp2 = [[False]*m for _ in range (n)]

    graph.append(temp)
    visited.append(temp2)
    

for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if graph[i][j][k] == 1 :
                que.append((i,j,k))
                visited[i][j][k] = True

bfs()

for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if graph[i][j][k] == 0 :
                fail_result = -1
                
            else : 
                max_result = max(max_result, graph[i][j][k])


if fail_result == -1 :
    print(-1)
else :
    print(max_result-1)

