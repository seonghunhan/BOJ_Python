import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N)]
orderList = [ list(map(int, input().split())) for _ in range(M)]
DP = [ list(0 for _ in range(N+1)) for _ in range(N+1)]

# DP만들기
for i in range(1,N+1) :
    for j in range(1, N+1) :
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + board[i-1][j-1]

print(DP)


# DP의 위랑 왼쪽 더하고 대각선 위 빼주고 원래값 더해주고
# 1 3 6 10
# 3 8 15 24
# 6 15 27 42
# 10 24 42 64

