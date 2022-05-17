import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range (N+1)]

for i in range(2,N+1) :
    dp[i] = dp[i-1] + 1

    if i % 2 == 0 and dp[i] > dp[i//2] + 1 :
        dp[i] = dp[i//2] + 1

    if i % 3 == 0 and dp[i] > dp[i//3] + 1 : #바킹독, min(dp[i], dp[i//3] +1)과 비슷
        dp[i] = dp[i//3] + 1

# print(dp[N])
print(dp) 

# 인풋 10은 3출력
# 이거는 그냥 12852번 참고