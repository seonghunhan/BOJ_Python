import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
board = [[0 for _ in range (N)] for _ in range(N)]

K = int(input())

for i in range(K) :
    a,b = map(int, input().split())
    board[a-1][b-1] = 2
    
L = int(input())
changeDirection = deque([])

for i in range(L) :
    a, b = map(str, input().split())
    changeDirection.append([int(a), b])
 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0


def turn(chr, dir) :

    #왼쪽
    if chr == 'L' :
        dir = (dir - 1) % 4
    #오른쪽
    else :
        dir = (dir + 1) % 4
    
    return dir
        
        
def bfs(x,y,d) :
    global result
    direction = d
    board[x][y] = 1
    snakeBody = deque()
    snakeBody.append([x,y])    
    
    while True :

        #print("result는 : " + str(result))
        #print(changeDirection)
        
        # 마지막에 changeDirection이 없기 때문에 조건 넣어줘야 함
        if len(changeDirection) > 0 :
            if result == changeDirection[0][0] :
                #print("Asd")
                direction = turn(changeDirection[0][1], direction)
                #print("direction은 : " + str(direction))
                changeDirection.popleft()
        
        result += 1
        
        nx = x + dx[direction]
        ny = y + dy[direction]
        x = nx
        y = ny
        #print("X와 y는 : " + str(x) + str(y))
        if 0 <= nx < N and 0 <= ny < N :
            
            if board[nx][ny] == 1 :
                break
            
            elif board[nx][ny] == 0 :
                board[nx][ny] = 1
                snakeBody.append([nx, ny])
                # 꼬리 제거
                a,b = snakeBody.popleft()
                #print("a와 b는 : "+ str(a)+ str(b))
                board[a][b] = 0
                
            elif board[nx][ny] == 2 :
                board[nx][ny] = 1
                snakeBody.append([nx, ny])
                
                
        else :
            break
                
bfs(0,0,0)
print(result)
