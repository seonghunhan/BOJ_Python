import sys
from collections import deque

a = int(sys.stdin.readline())
graph = []
visited = []

def dfs(x,y) :
    que = deque()
    que.append((x,y))
    visited[x][y] = True

    dx= [-2,-1,1,2,2,1,-1,-2]
    dy= [1,2,2,1,-1,-2,-2,-1]

    while que :
        x,y = que.popleft()

        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if not visited[nx][ny] and graph[nx][ny] == 0 :
                    que.append((nx,ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1

for i in range (a) :
    n = int(sys.stdin.readline())
    graph = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]    
    start_y, start_x = map(int, sys.stdin.readline().split())
    final_y, fainal_x = map(int, sys.stdin.readline().split())

    dfs(start_x, start_y)

    print(graph[fainal_x][final_y])
