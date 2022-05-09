import sys

T = int(sys.stdin.readline())
dp = [0,1,2,4]

for i in range(4,12) :
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])

for i in range(T) :
    a = int(sys.stdin.readline())

    print(dp[a])
