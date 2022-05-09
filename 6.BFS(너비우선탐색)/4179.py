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

def dfs() :
    
    while f_que :
        x,y = f_que.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if not graph[nx][ny] == '#' and f_visited[nx][ny] == 0 :
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_que.append((nx,ny))
    
    while j_que :
        x,y = j_que.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if not j_visited[nx][ny] and graph[nx][ny] != '#' :
                    if f_visited[nx][ny] == 0 or f_visited[nx][ny] > j_visited[x][y] + 1 :
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_que.append((nx,ny))

            else : 
                return j_visited[x][y] + 1

    return "IMPOSSIBLE"

n,m = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

f_que = deque()
j_que = deque()

f_visited = [[0]*m for _ in range(n)]
j_visited = [[0]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n) :
    for j in range (m) :
        if graph[i][j] == 'J' :
            j_que.append((i,j))
        if graph[i][j] == 'F' :
            f_que.append((i,j))

print(dfs())