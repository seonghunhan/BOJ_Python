import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
sharkSize = 2
preyOnFishCount = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]
x,y = 0,0

def bfs(x,y) :
    global sharkSize
    global preyOnFishCount
    que = deque()
    que.append([x,y])
    count = 0
    isTrue = False
    currentX = x
    currentY = y
    visited[x][y] = True
    #print("Asd " + str(x) + str(y))
    while que :
        x,y = que.popleft()
        
        for i in range(4) :
            nx = dx[i] + x
            ny = dy[i] + y
            print(board)
            print("x : " + str(x) + "  y : " + str(y))
            print("nx : " + str(nx) + "  ny : " + str(ny))
            
            if 0 <= nx < N and 0 <= ny < N :
                if visited[nx][ny] == False and sharkSize >= board[nx][ny] :
                    if board[nx][ny] != 0 and sharkSize > board[nx][ny] :
                        board[nx][ny] = 0
                        isTrue = True
                        preyOnFishCount += 1
                        if preyOnFishCount == sharkSize :
                            sharkSize += 1
                        currentX, currentY = nx, ny
                        break
                    
                    visited[nx][ny] = True
                    board[nx][ny] = 9
                    board[x][y] = 0
                    que.append([nx,ny])
                    count += 1    
                        
        break
    
    return count, isTrue, currentX, currentY
            
isTrue = True
result = 0
for i in range(N) :
    for j in range(N) :
        if board[i][j] == 9 :
            x,y = i, j      
while isTrue :
    visited = [[False] * N for _  in range(N)]
    
    count, isTrue, x, y = bfs(x,y)
    for i in range(N) :
        for j in range(N) :
            if board[i][j] == 9 :
                board[i][j] = 0
    board[x][y] = 9
    result += count
    
print(result)


#################################---------------------------------------------------------------------------------------------

# import sys
# from collections import deque

# input = sys.stdin.readline

# # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# # 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.

# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input().split())))


# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# cnt = 0
# x,y,size = 0,0,2
# #상어위치
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 9:
#             x = i
#             y = j

# def biteFish(x,y,shark_size):
#     distance = [[0] * n for _ in range(n)]
#     visited = [[0] * n for _ in range(n)]
#     # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다. (bfs사용)
#     q = deque()
#     q.append((x,y))
#     visited[x][y] = 1
#     temp = []
#     while q:
#         cur_x,cur_y = q.popleft()
#         for i in range(4):
#             nx = cur_x + dx[i]
#             ny = cur_y + dy[i]
#             if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 0:
#                 if graph[nx][ny] <= shark_size:
#                     q.append((nx,ny))
#                     visited[nx][ny] = 1
#                     distance[nx][ny] = distance[cur_x][cur_y] + 1
#                     if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
#                         temp.append((nx,ny,distance[nx][ny]))

# # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
#     return sorted(temp,key=lambda x: (-x[2],-x[0],-x[1]))


# cnt = 0
# result = 0
# while 1:
#     shark = biteFish(x,y,size)
#     # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
#     if len(shark) == 0:
#         break
#     # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
#     # 정렬한 결과를 반영해준다.
#     nx,ny,dist =shark.pop()
    
#     #움직이는 칸수가 곧 시간이 된다.
#     result += dist
#     graph[x][y],graph[nx][ny] = 0,0
#     #상어좌표를 먹은 물고기 좌표로 옮겨준다.
#     x,y = nx,ny
#     cnt += 1
#     if cnt == size:
#         size += 1
#         cnt = 0
# print(result)