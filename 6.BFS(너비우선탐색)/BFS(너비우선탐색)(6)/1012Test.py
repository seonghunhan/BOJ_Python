import sys
from collections import deque

input = sys.stdin.readline
r = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = []

def bfs(x,y) :
    global temp
    que = deque()
    que.append([x,y])
    board[x][y] = 0
    visited[x][y] = True
    
    #print("x : " + str(x) + " y : " + str(y))
    
    while que :
        x, y = que.popleft()
        #print("asdasd    " + str(x) + "asdasd " + str(y))
        
        for k in range(4) :
            
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < N and 0 <= ny < M :
                if board[nx][ny] == 1 and visited[nx][ny] == False :
                    board[nx][ny] += 1
                    visited[nx][ny] = True
                    que.append([nx, ny])
    
    #print(board)
    #print(visited)
    temp += 1
    

for _ in range (r) :
    
    temp = 0
    M, N, k = map(int, input().split())
    board = [[0] * M for _ in range (N)]
    visited = [[False] * M for _ in range(N)]
    
    #print(visited)
    
    for _ in range(k) :
        y, x = map(int, input().split())
        board[x][y] = 1
    
    for i in range(N) :
        for j in range(M) :
          if board[i][j] == 1 :
              bfs(i,j)  
    
    result.append(temp)

for i in result :
    print(i)
    