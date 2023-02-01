import sys

N, S = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

result = 0

def dfs(idx, sum) :
    
    global result

    if idx >= N :
        return
    
    sum += arr[idx]

    if S == sum :
        result += 1

    dfs(idx + 1, sum)

    dfs(idx + 1, sum - arr[idx])





dfs(0,0)

print(result)




































# import sys
# input = sys.stdin.readline
# n, s = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt = 0

# def subset_sum(idx, sub_sum):
#     global cnt

#     if idx >= n:
#         return

#     sub_sum += arr[idx]

#     if sub_sum == s:
#         cnt += 1
    
#     # 현재 arr[idx]를 선택한 경우의 가지
#     subset_sum(idx+1, sub_sum)

#     # 현재 arr[idx]를 선택하지 않은 경우의 가지
#     subset_sum(idx+1, sub_sum - arr[idx])

# subset_sum(0, 0)
# print(cnt)