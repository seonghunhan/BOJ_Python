import sys
from collections import deque

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs(z,x,y,goal_z, goal_x, goal_y) :
    que = deque()
    que.append((x,y,z))
    visited[z][x][y] = True

    while que :
        x,y,z = que.popleft()

        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < L :
                if graph[nz][nx][ny] == '.' and visited[nz][nx][ny] == False :
                    que.append((nx,ny,nz))
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    visited[nz][nx][ny] = True

    if graph[goal_z][goal_x][goal_y] == '.' :
        return print("Trapped!")
    else :
        return print("Escaped in %d minute(s)." % graph[goal_z][goal_x][goal_y])
while True :
    
    L, n, m = map(int, sys.stdin.readline().split())
    graph = []
    visited = []
    if L == 0 and n == 0 and m == 0 :
        break

    for i in range (L) :
        temp = [list(sys.stdin.readline().strip()) for _ in range (n)]
        temp2 = [[False]* m for _ in range (n)]
        graph.append(temp)
        visited.append(temp2)
        input()

    for i in range (L) :
        for j in range (n) :
            for k in range (m) :
                if graph[i][j][k] == 'S' :
                    start_z, start_x, start_y = i,j,k
                    graph[i][j][k] = 0
                elif graph[i][j][k] == 'E' :
                    goal_z, goal_x, goal_y = i,j,k
                    graph[i][j][k] = '.'
    bfs(start_z, start_x, start_y, goal_z, goal_x, goal_y)

# from collections import deque
# import sys
# input = sys.stdin.readline
# dx = [1, -1, 0, 0, 0, 0]
# dy = [0, 0, -1, 1, 0, 0]
# dz = [0, 0, 0, 0, 1, -1]
# def bfs():
#     q = deque()
#     q.append([sz, sy, sx])
#     visit[sz][sy][sx] = 1
#     while q:
#         z, y, x = q.popleft()
#         for i in range(6):
#             nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
#             if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c and visit[nz][ny][nx] == 0:
#                 if s[nz][ny][nx] == "." or s[nz][ny][nx] == "E":
#                     dp[nz][ny][nx] = dp[z][y][x] + 1
#                     visit[nz][ny][nx] = 1
#                     q.append([nz, ny, nx])
# while True:
#     l, r, c = map(int, input().split())
#     if l == 0:
#         break
#     s = [[] * r for i in range(l)]
#     dp = [[[0] * c for i in range(r)] for i in range(l)]
#     visit = [[[0] * c for i in range(r)] for i in range(l)]
#     for i in range(l):
#         for j in range(r):
#             s[i].append(list(map(str, input())))
#         input()
#     for i in range(l):
#         for j in range(r):
#             for k in range(c):
#                 if s[i][j][k] == "S":
#                     sx, sy, sz = k, j, i
#                 elif s[i][j][k] == "E":
#                     ex, ey, ez = k, j, i
#     bfs()
#     if dp[ez][ey][ex] == 0:
#         print("Trapped!")
#     else:
#         print("Escaped in %d minute(s)." % dp[ez][ey][ex])