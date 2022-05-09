import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
graph2 = [[0]*n for _ in range(n)]
res = 0

def bfs(x,y) :
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    que = deque()
    que.append((x,y))
    graph2[x][y] = res
    while que :
        x,y = que.popleft()

        for i in range (4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if graph2[nx][ny] == 0 and graph[nx][ny] == graph[x][y] :
                    que.append((nx,ny))
                    graph2[nx][ny] = 1
            
for i in range(n) :
    for j in range(n) :
        if graph2[i][j] == 0 :
            res += 1
            bfs(i,j)

graph2 = [[0]*n for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 'R' :
            graph[i][j] = 'G'
res2 = 0

for i in range(n) :
    for j in range(n) :
        if graph2[i][j] == 0 :
            res2 += 1
            bfs(i,j)

print(res, end=' ')
print(res2, end='')
