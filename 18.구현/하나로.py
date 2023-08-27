import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int,input().split())

board = [ list(map(int, input().rstrip())) for _ in range(N)]
visited = list( [ [0] * (K+1) for _ in range(M)] for _ in range(N))

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
                # K를 내림차순으로 사용하니까 C > 0 이라는 조건이 필요함 
                # visited[nx][ny][c-1] == 0 이 조건 안달면 시초뜸
                if board[nx][ny] == 1 and c > 0 and visited[nx][ny][c-1] == 0 :
                    visited[nx][ny][c-1] = visited[x][y][c] + 1
                    que.append([nx, ny, c-1])
                
        
    
    return -1

#벽돌부수기 횟수는 벡터에서 K자리부터 0자리까지 내림차순으로 사용할거임
print(bfs(0,0,K))   
            
            
            
            
# import sys
# from collections import deque
# input = sys.stdin.readline

# N, M, K = map(int, input().split())
# board = [list(map(int, input().rstrip())) for _ in range(N)]
# dx = [0,-1,0,1]
# dy = [1,0,-1,0]


# def bfs(x, y, k) :
#     result = 10e9
#     que = deque()
#     que.append([x,y,k])
    
#     while que :
        
#         x,y,k = que.popleft()
        
#         for i in range(4) :
            
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if 0 <= nx < N and 0 <= ny < M :
                
    
    
    
# bfs(0,0,K)