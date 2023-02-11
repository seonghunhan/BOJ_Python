# 그리고 보통 25~27 for 1개로 max두개써서 해결함 -> 다른사람풀이 참고
# 이코드는 100%에서 인덱스오류뜸
import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T) :
    
    N = int(input())
    board = [ list(map(int, input().split())) for _ in range(2)]
    dp = [list(0 for _ in range(N)) for _ in range(2)]
    
    dp[0][0] = board[0][0]
    dp[0][1] = board[0][1] + board[1][0]
    dp[1][0] = board[1][0]
    dp[1][1] = board[1][1] + board[0][0]

    for i in range(2,N) :
        for j in range(2) :
            dp[j][i] = board[j][i] + max(dp[(j+1)%2][i-1], dp[(j+1)%2][i-2])
            #print(board)
            #print(dp)
            #print(dp)
    #print(dp)
    print(max( dp[0][N-1], dp[1][N-1] ))



# t = int(input())
# for i in range(t):
#   s = []
#   n = int(input())
#   for k in range(2):
#     s.append(list(map(int, input().split())))
#   for j in range(1, n):
#     if j == 1:
#       s[0][j] += s[1][j - 1]
#       s[1][j] += s[0][j - 1]
#     else:
#       s[0][j] += max(s[1][j - 1], s[1][j - 2])
#       s[1][j] += max(s[0][j - 1], s[0][j - 2])
#   print(max(s[0][n - 1], s[1][n - 1]))