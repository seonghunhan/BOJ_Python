# 읽으면 5분절약
# 2차원배열로 1개씩 탐색하면서 각 문자열에 맞는 실시간 부분수열을 Board에 적어나감 
# 점화식은 아래와 같음
# 서로 알파벳이 같다면 왼쪽위에서 +1
# 서로 알파벳이 같지 않다면 위나 왼쪽에서 큰걸로


import sys
input = sys.stdin.readline

firstString = input().rstrip()
secondString = input().rstrip()

board = [ list(0 for _ in range(len(firstString)+1)) for _ in range(len(secondString)+1)]
print(board)

for i in range(1, len(secondString)+1) :
    
    for j in range(1, len(firstString)+1) :
        
        if firstString[j-1] == secondString[i-1] :
            board[i][j] = board[i-1][j-1] + 1
        else :
            maxCount = max(board[i-1][j], board[i][j-1])
            board[i][j] = maxCount
            
print(board[-1][-1])