import sys

N = int(sys.stdin.readline())

term = []
pay = []
dp = []

for i in range(N) :
    a, b = map(int, sys.stdin.readline().split())

    term.append(a)
    pay.append(b)
    dp.append(b)

dp.append(0)

for i in range(N-1,-1,-1) :

    if i + term[i] > N :
        dp[i] = dp[i+1]
    
    else :
        dp[i] = max(dp[i+1], pay[i] + dp[i + term[i]])

print(dp[0])