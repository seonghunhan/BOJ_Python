import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(M) ] for _ in range (N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = 1

def bfs (start_x,start_y, d) :
    global result
    direction = [0,1,2,3]
    wallCount = 0
    que = deque()
    que.append([start_x,start_y])

    
    while que :
        x, y = que.popleft()

        
        # 현재방향이 북쪽이고, 왼쪽 방향인 서쪽을 탐색할 때
        if d == 0 :
            nx = x + dx[2]
            ny = y + dy[3]
        # 현재방향이 동쪽이고, 왼쪽 방향인 북쪽을 탐색할 때
        elif d == 1 :
            nx = x + dx[1]
            ny = y + dy[0]
        # 현재방향이 남쪽이고, 왼쪽 방향인 동쪽을 탐색할 때
        elif d == 2 :
            nx = x + dx[2]
            ny = y + dy[2]
        # 현재방향이 서쪽이고, 왼쪽 방향인 남쪽을 탐색할 때
        elif d == 3 :
            nx = x + dx[0]
            ny = y + dy[0]
        
        
        
        if 0 <= nx < N and 0 <= ny < M :
            # 첫 번째 조건 (왼쪽 방향 청소 가능 -> 방향 회전, 그쪽 전진)
            if visited[nx][ny] == 0 and board[nx][ny] == 0 :
                result += 1
                visited[nx][ny] = 1
                board[nx][ny] = 1
                que.append([nx, ny])
                # 방향 전환
                d = direction[d-1]
                # 카운트 리셋
                wallCount = 0
            # 세 번째 조건 (네 방향 모두 청소완료 or 벽 -> 방향유지, 한칸 후진)
            if wallCount == 3 and visited[x][y] == 0 and board[x][y] == 0:
                d = direction[d-1]
                que.append([x,y])
                wallCount = 0
            elif wallCount == 3 and visited[x][y] == 1 and board[x][y] == 1:
                exit()
            # 두 번째 조건 (왼쪽 방향 청소할 공간없다 -> 방향 회전, 다시 반복)
            if board[nx][ny] == 1 or visited[nx][ny] == 1:
                d = direction[d-1]
                que.append([x,y])
                wallCount += 1

bfs(x,y,d)   
                
print(result)



