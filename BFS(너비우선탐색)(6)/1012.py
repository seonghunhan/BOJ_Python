import sys
from collections import deque

r = int(sys.stdin.readline())
res = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]


for i in range (r) :
    m, n, p = map(int, sys.stdin.readline().split())

    graph = [[0]*m for _ in range(n)]
    temp = [[False]*m for _ in range(n)]

    for j in range (p) :
        y,x = map(int, sys.stdin.readline().split())

        graph[x][y] = 1

    

    que = deque()

    for j in range(n) :
        for k in range(m) :
            if graph[j][k] == 1 :
                que.append((j,k))

                while que :
                    x,y = que.popleft()
                    temp[x][y] = True
                    for w in range(4) :
                        nx = x + dx[w]
                        ny = y + dy[w]

                        if 0 <= nx < n and 0 <= ny < m :
                            if graph[nx][ny] == 1  and temp[nx][ny] == False :
                                que.append((nx,ny))
                                graph[nx][ny] = graph[x][y] + 1
                                temp[nx][ny] = True

    for i in range (n) :
        for j in range (m) :
            if graph[i][j] == 1 :
                res += 1

    print(res)
    res = 0
