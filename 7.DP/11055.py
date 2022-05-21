n = int(input())

a = list(map(int, input().split()))

dp = [0 for i in range(n)]

dp[0] = a[0]

for i in range(1, n):

    s = []
    for j in range(i - 1, -1, -1):
        if a[i] > a[j]:
            s.append(dp[j])
    
    if not s:
        dp[i] = a[i]
    else:
        dp[i] = a[i] + max(s)


print(max(dp))
print(dp)

# 사각지대 case로 리스트가 3,1,100,2 일경우 19줄에서 max를 왜한지 알게된다.
# 리스트 인덱스가 2일때 리스트의 3,1중에 3을 가져갈수있다.
        













































# n = int(input())

# a = list(map(int, input().split()))

# dp = [0 for i in range(n)]

# dp[0] = a[0]

# for i in range(1, n):
#     s = []
#     for j in range(i - 1, -1, -1):
#         if a[i] > a[j]:
#             s.append(dp[j])
#     if not s:
#         dp[i] = a[i] 
#     else:
#         dp[i] = a[i] + max(s)

# print(dp)
# print(max(dp))

# 15줄 -> arr배열에서 해당 인덱스보다 그전에 큰값이 없을 경우 s는 [] 빈값유지
