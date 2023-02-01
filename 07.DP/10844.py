import sys

N = int(sys.stdin.readline())

dp = [ [0 for _ in range (10)] for _ in range (100)]

dp[0] = [0,1,1,1,1,1,1,1,1,1]
dp[1] = [1,1,2,2,2,2,2,2,2,1]
dp[2] = [1,3,3,4,4,4,4,4,3,2]

if N > 2 :

    for i in range (3,N) :

        for j in range(10) :

            if j == 0 :
                dp[i][j] = dp[i-1][j+1]
            
            elif j == 9 :
                dp[i][j] = dp[i-1][j-1]
            
            else :
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


print(sum(dp[N-1]) % 1000000000)
