import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().split())
graph = [[0]*m for _ in range(n)]
result = []
global res
res = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y) :
    
    que = deque()
    que.append((x,y))
    global res

    while que :
        x,y = que.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if graph[nx][ny] == 0 :
                    que.append((nx,ny))
                    graph[nx][ny] = 1
                    res += 1        

    return result.append(res)

for i in range(k) :
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
# 2차원 배열 [n][m]에 맞게 문제에서의 y를 n으로 x를 m으로
    for j in range(y1,y2) :
        for k in range(x1,x2) :
            graph[j][k] = 1

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            graph[i][j] = 1
            res += 1
            bfs(i,j)
            res = 0
print(len(result))
print(*sorted(result))


    


