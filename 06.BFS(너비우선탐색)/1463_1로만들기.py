import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = list(0 for _ in range(N+1))
que = deque()
que.append(N)

while que :
    # if board[1] != 0 :
    #     print(board[1])
    #     break
    
    x = que.popleft()
    
    if x > 0  :
        
        if x % 3 == 0 and not board[x//3]:
            nx = x // 3
            que.append(nx)
            board[nx] = board[x] + 1
        if x % 2 == 0 and not board[x//2]:
            nx = x // 2
            que.append(nx)
            board[nx] = board[x] + 1
        if not board[x-1] :
            nx = x - 1
            que.append(nx)
            board[nx] = board[x] + 1

print(board[1])
        
