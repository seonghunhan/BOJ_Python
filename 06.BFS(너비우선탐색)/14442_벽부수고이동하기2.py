# import sys
# from collections import deque
# input = sys.stdin.readline

# N, M, K = map(int, input().split())
# dx = [0,1,0,-1] #동서남북 -> 동남서북
# dy = [1,0,-1,0]
# visited = [list(False for _ in range(M)) for _ in range(N)]
# board = []
# for i in range(N) :
#     temp = list(input().rstrip())
#     temp2 = []
#     for j in temp :
#         temp2.append([int(j), [0 for _ in range(K+1)]])
#     board.append(temp2)



# # board[0][0][1][K-1] = 1
# # print(board)
# def bfs(startX, startY) :
#     k=0
#     que = deque()
#     visited[0][0] = True
#     board[0][0][1][0] = 1
#     que.append([startX,startY,k])
    
#     while que :
#         x,y,k = que.popleft()
        
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]
            
            
#             if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] :
                
#                 if board[nx][ny][0] == 0 :
#                     board[nx][ny][1][k] = board[x][y][1][k] + 1
#                     visited[nx][ny] = True
#                     que.append([nx,ny,k])
                
#                 if board[nx][ny][0] == 1 and k < K :
                    
#                     board[nx][ny][1][k+1] = board[x][y][1][k] + 1
#                     visited[nx][ny] = True
#                     que.append([nx,ny,k+1])
                    
                  
                # if board[nx][ny][0] == 1 and board[nx][ny][1][-1] == 0 :
                #     board[nx][ny][1][k+1] = board[x][y][1][k] + 1
                #     visited[nx][ny] = True
                #     que.append([nx,ny,k+1])
        
# bfs(0,0)   

# for i in board :
#     print(i)
# maxNum = 0
# for i in board[-1][-1][1] :
#     maxNum = max(maxNum, i)

# if maxNum != 0 :
#     print(maxNum)
# else :
#     print(-1)

import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int,input().split())

board = [ list(map(int, input().rstrip())) for _ in range(N)]
visited = list( [ [0] * (K+1) for _ in range(M)] for _ in range(N))

print(board)
print(visited)

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def bfs(x,y,c) :
    que = deque()
    que.append([x,y,c])
    visited[x][y][c] = 1
    
    while que :
        x,y,c = que.popleft()
        
        if x == N -1 and y == M -1 :
            #print(visited)
            return visited[x][y][c]
        
        for i in range(4) :
            
            nx = x + dx[i]
            ny = y + dy[i]
                    
            if 0 <= nx < N and 0 <= ny < M :
                # 벽이 없다면
                if board[nx][ny] == 0 and visited[nx][ny][c] == 0 :
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    que.append([nx,ny,c])
                
                # 벽이 있고, K가 남아있다면
                if board[nx][ny] == 1 and c > 0 and visited[nx][ny][c-1] == 0 :
                    visited[nx][ny][c-1] = visited[x][y][c] + 1
                    que.append([nx, ny, c-1])
                 
    
    return -1


print(bfs(0,0,K)) 




