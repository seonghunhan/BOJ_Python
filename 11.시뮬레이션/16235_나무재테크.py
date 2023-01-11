import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = []
treeList = []

for i in range(N) :
    a = list(map(int, input().split()))
    a.append(5)
    board.append(a)
    
print(board)

# for i in range(M) :
#     x,y,z = map(int, input().split())
#     board[x-1][y-1].append(z)
    
# [x,y,양분,나이]    
#3시 5만