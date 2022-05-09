import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

cnt = 0
max_each_cnt = 0

visit_graph = [[False]*m for _ in range (n)]
graph = [list(map(int, sys.stdin.readline().split())) for _ in range (n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(x,y) :
    
    each_cnt = 1
    visit_graph[x][y] = True
    que = deque()
    que.append((x,y))

    while que :
        x, y = que.popleft()

        for i in range (4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if visit_graph[nx][ny] == False and graph[nx][ny] == 1 :
                    each_cnt += 1
                    visit_graph[nx][ny] = True
                    que.append((nx,ny))

    return each_cnt

for i in range (n) :
    for j in range (m) :

        if graph[i][j] == 1 and visit_graph[i][j] == False :
            cnt += 1
            max_each_cnt = max(max_each_cnt,bfs(i,j))

print(cnt)
print(max_each_cnt)
