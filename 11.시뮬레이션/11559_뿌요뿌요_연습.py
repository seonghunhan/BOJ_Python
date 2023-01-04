import sys
input = sys.stdin.readline
from collections import deque

# asd -> 'a', 's', 'd'
#asd = list(input().rstrip())

# a s d => 'a', 's', 'd'
#asd = list(map(str, input().split()))

# https://shjz.tistory.com/114 -> SQL코테모음

board = [list(map(str, input().rstrip())) for _ in range(12)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]

def bfs(chr, x, y) :
    que = deque()
    chain = deque()
    que.append((x,y))
    chain.append((x,y))
    
    while que :
        x = que.popleft()
        y = que.popleft()
        board[x][y] = '.'
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 12 and 0 <= ny < 6 :
                if board[nx][ny] == chr :
                    que.append((nx,ny))
                    board[nx][ny] = '.'

