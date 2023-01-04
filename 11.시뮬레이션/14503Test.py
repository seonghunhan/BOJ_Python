import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


board[x][y] = 1
visited[x][y] = True
que = deque()
cnt = 1

def bfs(r,c,d) :
    global cnt
    que = deque()
    que.append([r,c])
    
    while que :
        flag = 0
        
        for _ in range(4) :
            x, y = que.popleft()
            
            nx = x + dx[(d+3)%4]
            ny = y + dy[(d+3)%4]
        
            d = (d+3)%4
            
            # 1번조건
            if 0 <= nx < N and 0 <= ny < M :
                if board[nx][ny] == 0 and visited[nx][ny] == False :
                    cnt += 1
                    board[nx][ny] = 1
                    visited[nx][ny] = True
                    que.append([nx, ny])
                    flag = 1
                    break
                else :
                    que.append([x, y])
                    
        #print(board)
        print("cnt = " + str(cnt)+"    flag = " + str(flag) + "   nx = " + str(nx) + "    ny = " + str(ny))
        if flag == 0 :
            # nx = nx + dx[(d+2)%4]
            # ny = ny + dy[(d+2)%4]
            if board[x-dx[d]][y-dx[d]] == 1:
                break
            else :
                que.append([x-dx[d]][y-dx[d]])

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
    
bfs(x,y,d)

print(cnt)