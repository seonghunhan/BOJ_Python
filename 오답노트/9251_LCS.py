import sys
input = sys.stdin.readline

firstString = input().rstrip()
secondString = input().rstrip()

board = [ list(0 for _ in range(len(firstString)+1)) for _ in range(len(secondString)+1)]

for i in range(1, len(secondString)+1) :
    
    for j in range(1, len(firstString)+1) :
        
        if firstString[j-1] == secondString[i-1] :
            board[i][j] = board[i-1][j-1] + 1
        else :
            maxCount = max(board[i-1][j], board[i][j-1])
            board[i][j] = maxCount
            
print(board[-1][-1])