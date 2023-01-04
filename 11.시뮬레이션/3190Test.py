import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())
board = [ [0 * N for _ in range(N)] for _ in range(N)]

for _ in range (K) :
    x, y = map(int, input().split())
    board[x-1][y-1] = 2
    
L = int(input())

directionList = deque()

for _ in range (L) :
    x, c = map(str, input().split())
    directionList.append([int(x), c])

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(dir, char) :
    
    if char == 'L' :
        dir = (dir - 1) % 4
    else : 
        dir = (dir + 1) % 4
        
    return dir

def bfs(x,y,dir) :
    cnt = 0
    snake = deque()
    snake.append([x, y])
    board[x][y] = 1
    while True :
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        cnt += 1
        if len(directionList) > 0 :
            if directionList[0][0] == cnt :
                dir = turn(dir,directionList[0][1])
                directionList.popleft()
                
    
        
        if 0 <= nx < N and 0 <= ny < N :
            
            if board[nx][ny] == 0 :
                board[nx][ny] = 1
                snake.append([nx, ny])
                a, b = snake.popleft()
                board[a][b] = 0
                x = nx
                y = ny
            elif board[nx][ny] == 2 :
                board[nx][ny] = 1
                snake.append([nx, ny])
                x = nx
                y = ny
            else :
                break
        else :
            # print("dir : " + str(dir))
            break
        
        # print("nx : " + str(nx) + "    ny : "+ str(ny) + "    cnt : " + str(cnt) + "    board : " + str(board))
        # print("snake : " + str(snake) + "    dir : " + str(dir))
        # print("directionList : " + str(directionList))
            
    return cnt            
        
    
    
print(bfs(0,0,0))