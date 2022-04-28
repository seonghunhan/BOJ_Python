import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
que = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
#start_point_list = []
result = False

# for i in range(n) :
#     if 1 in graph[i] :
#         x = i
#         y = graph[i].index(1)

#         start_point_list.append([x,y])

# for i in range(len(start_point_list)) :
#     que.append((start_point_list[i]))

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            que.append([i,j])

while que :
    x,y = que.popleft()

    for i in range (4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m :
            if graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx,ny))

max_result = max(map(max, graph))

for i in range(n) :
    if 0 in graph[i] :
        result = True

if result :
    print(-1)
elif max_result == 1 :
    print(0)
else :
    print(max_result-1)


    
    