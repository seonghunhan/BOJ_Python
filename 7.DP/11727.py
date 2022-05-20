import sys

N = int(sys.stdin.readline())

dp = [0,1]

for i in range (1,N+1) :
    x = dp[i]

    if i % 2 == 0 :
        x = (2 * x) - 1
        dp.append(x)
    elif i % 2 != 0  :
        x = (2 * x) + 1
        dp.append(x)   
    
print(dp[N] % 10007)
