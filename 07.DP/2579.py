import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range (301)]
list1 = [0 for _ in range (301)]

for i in range(N) :
    list1[i] = int(sys.stdin.readline())

dp[0] = list1[0]
dp[1] = list1[0]+list1[1]
dp[2]  = max(list1[0]+list1[2], list1[1]+list1[2])

for i in range (3,N) :
    dp[i] = max(list1[i] + list1[i-1] + dp[i-3], list1[i] + dp[i-2])

print(dp[N-1])

# 밟은 계단이 "END - 1"일 경우 반드시 "END - 2" 계단을 밟으면 안 된다. - case_A
# 밟은 계단이 "END - 2"일 경우 그 전 계단은 신경 쓰지 않는다. - case_B

# dp[i] = max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1])

# 수식을 한국말로 해설해보면
# "i번 째 계단까지의 최대 가중치 합" = 
# "case_B : i - 2번째 계단까지의 최대 가중치 합 + 현재 계단의 가중 치"와 
# "case_A : i- 3번째 계단까지의 최대 가중치 합 + i - 1번째 계단의 가중치 + 현재 계단의 가중 치" 중 더 큰 값


