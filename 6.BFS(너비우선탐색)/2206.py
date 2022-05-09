# import sys
# from collections import deque

# n, m = map(int, sys.stdin.readline().split())

# graph=[list(map(int, input())) for _ in range(n)]
# temp_graph = graph.copy()
# visited = [[False]*m for _ in range(n)]
# min_distance = []
# temp1 = 0

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def bfs(x,y) :

#     que = deque()
#     que.append((x,y))
#     visited[0][0] = True

#     while que :
#         x,y = que.popleft()
        
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny < m :
#                 if not visited[nx][ny] and graph[nx][ny] == 0 :
#                     que.append((nx,ny))
#                     graph[nx][ny] = graph[x][y] + 1
#                     visited[nx][ny] = True
#     if graph[n-1][m-1] == 0 :
#         return -1
#     else :
#         return graph[n-1][m-1] + 1


# temp1 = bfs(0,0) 
# #print("1번째 temp1 : "+str(temp1))  
# if temp1 != -1 :
#     min_distance.append(temp1)


# graph = temp_graph.copy()
# for i in range(n) :
#     for j in range(m) :
#         if graph[i][j] == 1 :
#             graph = temp_graph.copy()
#             graph[i][j] = 0
#             visited = [[False]*m for _ in range(n)]
#             temp = bfs(0,0)
#             #print("temp : " + str(temp))
#             #print("min_distance : " + str(min_distance))

#             if temp != -1 :
#                 min_distance.append(temp)

# if len(min_distance) == 0 :
#     print(-1)
# else :
#     print(min(min_distance))

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, input())) for _ in range (n)]

visited = [[[0]*2 for _ in range (m)] for _ in range (n)]
visited[0][0][0] = 1

dx, dy = [1,-1,0,0], [0,0,1,-1]

def bfs(x,y,c) :

    que = deque()
    que.append((x,y,c))

    while que :
        x,y,c = que.popleft()

        if x == n-1 and y == m-1 :
            return visited[x][y][c]

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                # 벽이 없고, 아직 방문하지 않은 곳
                if graph[nx][ny] == 0 and visited[nx][ny][c] == 0 :
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    que.append((nx,ny,c))
                # 벽이 있고, 기회를 안쓴경우
                elif graph[nx][ny] == 1 and c == 0 :
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    que.append((nx,ny,1))
    return -1

print(bfs(0,0,0))