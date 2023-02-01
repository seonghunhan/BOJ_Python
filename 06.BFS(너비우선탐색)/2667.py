import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [list(map(int,input())) for _ in range(n)]


result = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y) :

    que = deque()
    que.append((x,y))
    each_cnt = 1
    graph[x][y] = 2
    
    while que :
        x,y = que.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if graph[nx][ny] == 1 :
                    each_cnt += 1
                    que.append((nx,ny))
                    graph[nx][ny] = 2

    return result.append(each_cnt)

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            bfs(i,j)

print(len(result))
result.sort()

for i in range(len(result)) :
    print(result[i])