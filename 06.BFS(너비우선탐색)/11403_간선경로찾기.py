import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [ list(map(int, input().split())) for _ in range(N)]
result = [ list( 0 for _ in range(N)) for _ in range(N)]


def bfs(x) :
    que = deque()
    que.append(x) 
    visited = list(0 for _ in range(N))
    while que :
        nx = que.popleft()
        #print('x :' + str(x)+'  nx :' + str(nx))
        
        for i in range(N) :
            
            if board[nx][i] and not visited[i] :
                visited[i] = 1
                result[x][i] = 1
                que.append(i)    
        
        
    

for i in range(N) :
    bfs(i)

for i in range(N) :
    print(' '.join(map(str,result[i])))