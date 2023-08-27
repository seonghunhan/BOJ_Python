import sys
input = sys.stdin.readline

N, K = map(int, input().split())

stuff = [ [0,0]]

for i in range(N) :
    stuff.append(list(map(int, input().split())))
    
board = [ list(0 for _ in range(K+1)) for _ in range(N+1)]


for i in range(1, N+1) :
    
    weight = stuff[i][0]
    value = stuff[i][1]
    
    for j in range(1, K+1) :
        
        if weight > j :
            board[i][j] = board[i-1][j]
        
        else :
             maxValue = max(value + board[i-1][j-weight] , board[i-1][j]) # j-weight가 킬포
             board[i][j] = maxValue

#print(board)
print(board[-1][-1])