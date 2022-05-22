import sys

N = int(sys.stdin.readline())


for i in range (N) :
    P = int(sys.stdin.readline())
    dp = [0 for _ in range (100)]
    
    for j in range (3) :
        dp[j] = 1

    if P > 2 :
        for j in range (3, P) :
            dp[j] = dp[j-3] + dp[j-2]

    print(dp[P-1])