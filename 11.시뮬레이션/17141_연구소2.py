import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
copyboard = [list(map(int,input().split())) for _ in range(N)]
temp = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for i in range(N) :
    for j in range(N) :
        if copyboard[i][j] == 2 :
            temp.append([i, j])
            copyboard[i][j] = 0
        if copyboard[i][j] == 1 :
            copyboard[i][j] = '-'
            
virus_list = list(combinations(temp, M))



def bfs(virus) :
    que = deque(virus)
    print(que)
    
    while que :
        
        x,y = que.popleft()
        visited[x][y] = True
        
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N :
                if not visited[nx][ny] and board[nx][ny] != '-' and board[nx][ny] == 0 :
                    que.append([nx, ny])
                    visited[nx][ny] = True
                    board[nx][ny] = board[x][y] + 1
                    
result2 = 10e9
isTrue = True
temp3 = 0              
for i in virus_list :
    result = 0
    temp2 = 0

    visited = [[False for _ in range(N)] for _ in range(N)]
    board = copy.deepcopy(copyboard)
    #print(board)
    bfs(i)
    print(board)
                
    for i in range(N) :
        for j in range(N) :
            if board[i][j] != '-' :
                result = max(result, board[i][j])
                    

    for i in range(N) :
        for j in range(N) :
            if board[i][j] == 0 :
                temp2 += 1
                if temp2 > M :
                    result = 10e9
                    
                    break
    
    #print("resut : " + str(result))
    
    if temp2 != M :
        temp3 += 1

    # print(len(virus_list))
    # print(temp3)
    if temp3 == len(virus_list) :
        isTrue = False
            
    result2 = min(result2, result)

if isTrue == False :
    print(-1)
else :
    print(result2)
      
