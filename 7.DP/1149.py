import sys

n = int(sys.stdin.readline())
dp = []

for i in range (n) :
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range (1, n) :

    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))


# 전체 dp코드를 보면 이해가가는데 dp의 첫번째는 rgb로 해놓는다
# 다음 0,1,2 자리에 각각 누적값을 넣는다
# 최종적으로 마지막 자리에 0,1,2자리값을 비교하면 최솟값을 구할 수 있다