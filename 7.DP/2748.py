import sys

N = int(sys.stdin.readline())

dp = [0,1]

if N > 1 :
    for i in range(2, N+1) :

        dp.append(dp[i-2] + dp[i-1])

print(dp[N])


