import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

dp = [0]
temp = 0

for i in arr :
    temp += i
    dp.append(temp)

for i in range (M) :
    start_num, finish_num = map(int, sys.stdin.readline().split())

    print(dp[finish_num] - dp[start_num - 1])

# DP에서 prefix_sum 알고리즘을 사용한 것