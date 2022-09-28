import sys
from collections import deque

input = sys.stdin.readline

M, H, N = map(int, input().split())
#ladderList = deque(list(map(int, input().split())) for _ in range(H))

board = [[1 for _ in range(M)] for _ in range(N)]

for _ in range (H) :
    a,b = map(int, input().split())
    board[a-1][b-1] = 2
    board[a-1][b] = 2
    
def bfs(x,y) :
    
    que = deque()
    que.append([x,y])
    
    
    while que :
        nx, ny = que.popleft()
        #print("nx : "+ str(nx) + " ny : "+str(ny))
        if 0 <= nx < N and 0 <= ny < M :
            if board[nx][ny] == 1 :
                # board[nx][ny] = 0
                visited[nx][ny] = True
                que.append([nx+1, ny])
                
            if board[nx][ny] == 2 :
                if 0 < ny < M-1 :
                    if board[nx][ny+1] == 2 and not visited[nx][ny+1]:
                        #board[nx][ny] = 0
                        visited[nx][ny] = True
                        que.append([nx, ny+1])
                    elif board[nx][ny-1] == 2 and not visited[nx][ny-1]:
                        #board[nx][ny] = 0
                        visited[nx][ny] = True
                        que.append([nx, ny-1])
                    elif not visited[nx][ny+1]  or not visited[nx][ny-1] :
                        #board[nx][ny] = 0
                        visited[nx][ny] = True
                        que.append([nx+1, ny])
                    continue
                if ny == 0 and not visited[nx][ny+1]:
                    #board[nx][ny] = 0
                    visited[nx][ny] = True
                    que.append([nx,ny+1])
                elif ny == 0 and visited[nx][ny+1] :
                    visited[nx][ny] = True
                    que.append([nx+1,ny])
                    
                elif ny == M-1 and not visited[nx][ny-1]:
                    #board[nx][ny] = 0
                    visited[nx][ny] = True
                    que.append([nx,ny-1])
                elif ny == M-1 and visited[nx][ny-1] :
                    visited[nx][ny] = True
                    que.append([nx+1,ny])




for i in range(M) :
    visited = [[False for _ in range(M)] for _ in range(N)]
    bfs(0,i)
    for j in range(M) :
        if visited[N-1][j] :
            print(str(i)+"번째 줄의 결과값은 "+str(j)+"입니다")

