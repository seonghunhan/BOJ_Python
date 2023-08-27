# import sys

# input = sys.stdin.readline

# N, K = map(int, input().split())

# coinList = [int(input().rstrip()) for _ in range(N)]

# #coinList = sorted(coinList, key = lambda x : x[0])
# result = 0

# for i in range(N-1, -1, -1) :
#     if coinList[i] <= K :
#         result += K // coinList[i]
#         K = K % coinList[i]
    
#     if K == 0 :
#         break
    
# print(result)

import sys
input = sys.stdin.readline

N = int(input())

dp = [[1,0]]

for i in range(1,N+1) :
    a = dp[i-1][1]
    b = dp[i-1][0] + dp[i-1][1]
    dp.append([a,b])
print(dp[N][0], dp[N][1])
