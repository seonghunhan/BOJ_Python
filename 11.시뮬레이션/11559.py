import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = 0

map = [list(input().strip()) for _ in range (12)]


def bfs(i,j,char) :
    
    que = deque()
    que.append([i,j])
    chain.append([i,j])
    while que :
        x,y = que.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < 12 and 0 <= ny < 6 and visited[nx][ny] == 0 and map[nx][ny] == char :
                visited[nx][ny] = 1
                que.append([nx,ny])
                chain.append([nx,ny])
    
def drop() :
    for i in range (6) :
        for j in range (10,-1,-1) :
            for k in range(11, j, -1) :
                if map[j][i] != '.' and map[k][i] == '.' :
                    map[k][i] = map[j][i]
                    map[j][i] = '.'
                    break
    

while True :
    isTrue = False
    visited = [[0] * 6 for i in range(12)]
    
    for i in range(12) :
        
        for j in range(6) :
            
            if visited[i][j] == 0 and map[i][j] != '.' :
                chain = []
                visited[i][j] = 1
                bfs(i, j, map[i][j])
                
                if len(chain) > 3 :
                    isTrue = True
                    for x,y in chain :
                        map[x][y] = '.'
                          
    
    if not isTrue :
        break
    
    drop()
    result += 1 

print(result)
