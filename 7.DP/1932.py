import sys

N = int(sys.stdin.readline())

dp = [ list(map(int, sys.stdin.readline().split())) for i in range(N)]
k = 2

for i in range (1, N) :

    for j in range (k) :

        if j == 0 :
            dp[i][j] = dp[i][j] + dp[i-1][j]
        
        elif j == i :
            dp[i][j] = dp[i][j] + dp[i-1][j-1]

        else :
            dp[i][j] = dp[i][j] + max(dp[i-1][j], dp[i-1][j-1])

    k += 1

print(max(dp[N-1]))

# 위에서 하나하나 경우의 수를 다 구한것
# 12,15줄은 배열의 양 끝 인덱스들을 고려한 것(오른,왼쪽 대각선의 선택지가 없기 때문)
# 19줄은 오른,왼쪽 대각선의 선택지가 있을 때 사용
# 마지막으로 dp의 마지막 배열이 최종 제일 수가 높은것들의 집합, 그 중에 가장 높은 수 출력




