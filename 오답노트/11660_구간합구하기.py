# prefix sum 구간합 알고리즘
# 누적합 문제!

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
target = []

originBoard = [ list(map(int, input().split())) for _ in range(N)]
target = [ list(map(int, input().split())) for _ in range(M)]

DP = [ list(0 for _ in range(N+1)) for _ in range(N+1)]

#누적합보드 형성(원점부터 좌표까지)
for i in range(1,N+1) :
    
    for j in range(1, N+1) :
        
        DP[i][j] = originBoard[i-1][j-1] + DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1]

print(DP)
#결과값 출력
for i in range(M) :
    
    x1, y1, x2, y2 = target.pop(0)
    
    print(DP[x2][y2] + DP[x1-1][y1-1] - DP[x1-1][y2] - DP[x2][y1-1])