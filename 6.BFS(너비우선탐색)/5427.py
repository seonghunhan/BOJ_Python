import sys
from collections import deque

def bfs() :

    while f_que :
        
        x,y = f_que.popleft()

        for i in range (4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if not f_visited[nx][ny] and graph[nx][ny] != '#' and f_graph[nx][ny] == 0 :
                    f_que.append((nx,ny))
                    f_graph[nx][ny] = f_graph[x][y] + 1
                    f_visited[nx][ny] = True

    while j_que :

        x,y = j_que.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if not j_visited[nx][ny] and graph[nx][ny] != '#' and j_graph[nx][ny] == 0 :
                    if f_graph[nx][ny] > j_graph[x][y] + 1 or f_visited[nx][ny] == False :
                        j_que.append((nx,ny))
                        j_graph[nx][ny] = j_graph[x][y] + 1
                        j_visited[nx][ny] = True

            else :
                return j_graph[x][y] + 1                    
    
    return "IMPOSSIBLE"


Num = int(sys.stdin.readline())

for k in range (Num) :
    m, n = map(int, sys.stdin.readline().split())

    graph = [list(sys.stdin.readline().rstrip()) for _ in range (n)]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    j_graph = [[0]*m for _ in range (n)]
    f_graph = [[0]*m for _ in range (n)]

    j_visited = [[False]*m for _ in range (n)]
    f_visited = [[False]*m for _ in range (n)]

    j_que, f_que = deque(), deque()

    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == '*' :
                f_que.append((i,j))
                f_visited[i][j] = True
            elif graph[i][j] == '@' :
                j_que.append((i,j))
                j_visited[i][j] = True

    print(bfs())