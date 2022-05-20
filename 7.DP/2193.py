import sys

N = int(sys.stdin.readline())

dp = [1, 1]

for i in range (2, N) :
    dp.append(dp[i-2] + dp[i-1])

print(dp[N-1])

