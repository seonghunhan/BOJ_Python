# import sys
# from collections import deque

# n, m = map(int, sys.stdin.readline().split())

# graph = []
# result = []
# fire = []
# jihun = []


# for i in range (n) :
#     graph.append(list(map(str, input())))

# for i in range (n) :
#     for j in range (m) :
#         if graph[i][j] == '.' :
#             graph[i][j] = 0
#             result.append((i,j))
#         elif graph[i][j] == 'J' :
#             graph[i][j] = 1
#             jihun.append((i,j))
#         elif graph[i][j] == 'F' :
#             graph[i][j] = 2
#             fire.append((i,j))

# def jihun_bfs(jx,jy) :
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     que = deque()
#     que.append((jx,jy))

#     while que :
#         x,y = que.popleft()

#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny < m :
#                 if graph[nx][ny] == 0 :
#                     graph[nx][ny] = graph[x][y] + 1
#                     que.append((nx,ny))

#     return max(map(max, graph))

# def fire_bfs(fx,fy) :
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     que = deque()
#     que.append((fx,fy))

#     while que :
#         x,y = que.popleft()

#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny < m :
#                 if graph[nx][ny] == 0 :
#                     graph[nx][ny] = graph[x][y] + 1
#                     que.append((nx,ny))

#     return max(map(max, graph)) -2

# jx,jy = jihun[0]
# fx,fy = fire[0]


# if jihun_bfs(jx,jy) > fire_bfs(fx,fy) :
#     print("지훈이가 탈출한다")
# elif jihun_bfs(jx,jy) < fire_bfs(fx,fy) :
#     print("지훈이가 죽는다")


# in range case
 
import sys
from collections import deque
input = sys.stdin.readline
 
def bfs():
    while f_queue:    # fire BFS
        x, y = f_queue.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < R and 0 <= ny < C:
                if not f_visited[nx][ny] and graph[nx][ny] != '#':
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_queue.append((nx, ny))
 
    while j_queue:    # jihoon BFS
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < R and 0 <= ny < C:
                if not j_visited[nx][ny] and graph[nx][ny] != '#':
                    if not f_visited[nx][ny] or f_visited[nx][ny] > j_visited[x][y] + 1:    # important code
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_queue.append((nx, ny))
            else:
                return j_visited[x][y] + 1    # escape map
 
    return 'IMPOSSIBLE'    # not escape map
 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
 
R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
f_queue, j_queue = deque(), deque()    # declare fire, jihoon queue
f_visited, j_visited = [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]    # declare fire, jihoon visited
 
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            f_queue.append((i, j))
        elif graph[i][j] == 'J':
            j_queue.append((i, j))
print(bfs())