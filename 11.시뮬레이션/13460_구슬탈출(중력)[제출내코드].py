import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
que = deque()

rx = 0
ry = 0
bx = 0
by = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(N) :
    for j in range(M) :
        if board[i][j] == 'R' :
            rx = i
            ry = j
        elif board[i][j] == 'B' :
            bx = i
            by = j

def move(x,y,dx,dy) :
    
    cnt = 0
    # 여기서 오래걸림 !! 다음이 벽이거나 '현재'!!!가 O일 경우!
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O' :
        x += dx
        y += dy
        cnt += 1
        #print("nx, ny : " + str(nx) + str(ny))

    return x,y,cnt
    
def solve(rx,ry,bx,by,depth) :
    visited[rx][ry][bx][by] = True
    que.append([rx, ry, bx, by, depth])
    
    while que :
        rx, ry, bx, by, dpt = que.popleft()
        
        if dpt > 10 : 
            break
        
        for i in range(4) :
            
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            #print("nrx, nry, rcnt : " + str(nrx) + " " + str(nry) + " " +str(rcnt))
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            #print("nbx, nby, bcnt : " + str(nbx) + " " + str(nby) + " " +str(bcnt))
            # 실패조건(blue가 구멍에 들어갈 때)이 아니라면
            if board[nbx][nby] != 'O' :
                if board[nrx][nry] == 'O' :
                    print(dpt)
                    return
                # nrx == nbx and nry == nby
                if (nrx, nry) == (nbx, nby) :
                    
                    if rcnt > bcnt :
                        nrx -= dx[i]
                        nry -= dy[i]
                    else :
                        nbx -= dx[i]
                        nby -= dy[i] 
                    
                if not visited[nrx][nry][nbx][nby] :
                    visited[nrx][nry][nbx][nby] = True
                    que.append([nrx, nry, nbx, nby, dpt+1])
                    #print("bfs돌리기, dpt : "+str(dpt)) 
        
    print(-1)        


solve(rx,ry,bx,by,1)   
                
            
            