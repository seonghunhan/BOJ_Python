import sys
from collections import deque
import copy
input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 10e9

# 동 서 남 북
dx = [0,0,1,-1]
dy = [1,-1,0,0]

cctv_mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,1],[2,3]],
    [[0,3],[3,1],[1,2],[2,0]],
    [[0,3,1],[3,1,2],[1,2,0],[2,0,3]],
    [[1,2,3,4]]
]

cctv_list = []

for i in range (N) :
    for j in range(M) :
        if board[i][j] in (1,2,3,4,5) :
            cctv_list.append([board[i][j], i, j])
            
def bfs(direction, x, y):
    "asd"
    
            
def dfs(arr, depth) :
    global result
    
    if depth == len(cctv_list) :
        cnt = 0
        
        for i in range(N) :
            cnt += arr[i].count(0)
    
        result = min(result, min)
        return
    
    cctv_num, x, y = cctv_list[depth]
    cctv_direction = cctv_mode[cctv_num]
        
    for i in cctv_direction :
        bfs(i, x, y)
        dfs(arr, depth+1)
        arr = copy.deepcopy(board)    
