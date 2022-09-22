import sys
from collections import deque
from itertools import combinations
from itertools import p
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N)]
temp2 = copy.deepcopy(board)
virus_location = deque()
# 덱같은경우 양끝을 처리하는데 있어서 좋지만, 중간을 탐색할때는 list가 효율적이라 함
safezone = []
result = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 2와 0 좌표 탐색
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 2 :
            virus_location.append([i,j])
        elif board[i][j] == 0 :
            # 하나의 리스트에서 조합을 구하기 위하여 리스트안에 튜플형식으로 삽입
            safezone.append((i,j))
            
def bfs() :
    while virus_location :
        x, y = virus_location.popleft()
        visited[x][y] = 1
        
        for i in range(4) :   
            nx = x + dx[i]
            ny = y + dy[i]     
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 0 :
                visited[nx][ny] = 1
                board[nx][ny] = 2
                virus_location.append([nx, ny])

# 0인곳을 위주로 3개의 조합 형성
addWallList = list(combinations(safezone, 3))
temp = 0

for i in addWallList :
    # 0인 조합에 벽3개 세우기
    for j in range(3) :
        x = i[j][0]
        y = i[j][1]
        board[x][y] = 1
    # visited 초기화
    visited = [ [0 for _ in range(M)] for _ in range(N)]
    for n in range(N) :
        for m in range(M) :
            if board[n][m] == 2 :
                #바이러스존 초기화
                virus_location.append([n,m])

    bfs()
    # 안전지대 갯수 temp에 저장
    for k in range(N) :
        for l in range(M) :
            if board[k][l] == 0 :
                temp += 1
    # 최대 안전지대 도출
    result = max(result, temp)
    temp = 0
    board = copy.deepcopy(temp2)


print(result)