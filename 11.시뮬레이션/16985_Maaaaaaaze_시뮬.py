import sys
from itertools import permutations
from collections import deque

input = sys.stdin.readline

result = 5 ** 3 + 1
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
b = [[list(map(int, input().split())) for _ in range (5)] for _ in range (5)]
board = [[[0 for _ in range(5)] for _ in range(5)] for _ in range (5) ]



def rotate (board1) :
    rotatingBoard = [[0 for _ in range(5)] for _ in range(5)]
    
    for i in range(5) :
        for j in range(5) :
            rotatingBoard[j][4-i] = board1[i][j]
            
    return rotatingBoard

def dfs(x):
    # dfs를 이용한 완전 탐색
    global board
    if x == 5:
        if board[4][4][4]:
            bfs(board)
        return

    for _ in range(4):
        if board[0][0][0]:
            dfs(x + 1)
        board[x] = rotate(board[x])
        
def bfs(board) :
    
    global result
    visited = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    que = deque()
    que.append([0,0,0])
    
    
    while que :
        
        z,x,y = que.popleft()
        
        if [x,y,z] == [4,4,4] :
            temp = visited[z][x][y]
            result = min(result, temp)
            if result == 12: # 가장 짧은 경로의 경우 출력 후 종료
                print(result)
                exit()
            return     
            
            
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 :
                if visited[nz][nx][ny] == 0 and board[nz][nx][ny] == 1 :
                    visited[nz][nx][ny] += visited[z][x][y] + 1
                    que.append([nz, nx, ny])
    
        
 # 5!으로 5개의 판을 섞는 코드
for i in permutations([0,1,2,3,4]) :
    for j in range(5) :
        board[i[j]] = b[j] # i는 리스트임
    dfs(0)

if result == 5 ** 3 + 1 :
    result = -1
    
print(result)