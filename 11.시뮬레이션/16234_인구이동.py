import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())

board = list(list(map(int, input().split())) for _ in range (N))
result = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x,y) :
    que = deque()
    que.append((x,y))
    que2 = deque()
    visited[x][y] = False
    count = 0
    
    while que :
        x,y = que.popleft()
        que2.append((x,y))
        
        for i in range (4) :
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N :
                if visited[nx][ny] == True :
                    visited[nx][ny] = False
                    que.append((nx, ny))
                    
    for i,j in que2 :
        # print("x : " + str(i) + "  y : "+str(j))
        count += board[i][j]

    count = count // len(que2)
    # print(count)
    
    for i,j in que2 :
        board[i][j] = count

while (True) :
    result += 1
    visited = [[False for _ in range(N)] for _ in range (N)]
    cnt = 0
    for i in range(N) :
        for j in range(N) :
            for k in range(4) :
                
                if 0 <= (i + dx[k]) < N and 0 <= (j + dy[k]) < N :
                    if L <= abs(board[i][j] - board[i + dx[k]][j + dy[k]]) <= R :
                        cnt += 1
                        visited[i][j] = True
    
    for i in range(N) :
        for j in range(N) :
            
            if visited[i][j] :
                bfs(i,j)
                                
    if cnt == 0 :
        break
    

print(board)
#print(result - 1)