import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False]*n for _ in range (n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

count = 0
max_count = 0


def bfs(x,y,k) :
    que = deque()
    que.append((x,y))
    
    while que :
        x,y = que.popleft()

        for i in range(4) :
            
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if not visited and graph[nx][ny] <= k :
                    que.append((nx,ny))
                    visited[nx][ny] = True

    
                    

for i in range (1,10) :
    for j in range (n) :
        for k in range (n) :
            
            if graph[j][k] <= i :
                count += 1
                visited[j][k] = True
                bfs(j,k,i)
    
    max_count = max(max_count, count)
            

print(max_count)


