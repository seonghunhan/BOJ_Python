# for문에서 T모양을 처리하기 위해 T함수를 썼는데 시간초과 발생
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


# 동,북,서,남
dx = [0,-1,0,1]
dy = [1,0,-1,0]
visited = [[0 for _ in range(M)] for _ in range (N)]
result = 0

# T모양을 제외한 모든 모양은 칸이 4개일경우 dfs로 모두 처리 가능
def dfs(x,y,total,cnt) :
    global result
    
    if cnt == 4 :
        result = max(result, total)
        return
    
    for i in range (4) :
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] :
            visited[nx][ny] = 1
            dfs(nx, ny, total + board[nx][ny], cnt + 1)
            visited[nx][ny] = 0
        
# T는 자기 자신에서 상하좌우만 살펴보면 되기 때문에 dfs사용 X
def T(x,y,T_total) :
    global result
    tmp = 1
    tmp2 = 0
    tmp2 += T_total
    
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <nx < N and 0 <= ny < M :
            tmp += 1
            tmp2 += board[nx][ny]

        if tmp == 4 :
            result = max(result, tmp2)
        
        

for i in range (N) :
    for j in range (M) :
        visited[i][j] = 1
        dfs(i,j,board[i][j],1)
        T(i,j,board[i][j])
        visited[i][j] = 0

print(result)