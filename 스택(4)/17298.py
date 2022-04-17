import sys

# N = int(sys.stdin.readline())
# list1 = list(map(int, sys.stdin.readline().split()))

# stack = []
# result = []

# for i in range(N-1,-1,-1) :
#     h = list1[i]
#     if stack :
#         while stack :
#             if stack[-1][1] > h :                
#                 result.append(stack[-1][1])
#                 stack.append([i,h])
#                 break
#             elif stack[-1][1] < h :
#                 stack.pop()
#                 if not stack :
#                     stack.append([i,h])
#                     result.append(-1)
#                     break
#     else :
#         stack.append([i,h])
#         result.append(-1)

# result.reverse()

# print(' '.join(map(str,result)))

import sys

N = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))
result = [-1] * N
stack = [0]


for i in range(1,N) :

    while stack and list1[stack[-1]] < list1[i] :
        result[stack.pop()] = list1[i]
    stack.append(i)

print(*result)

# for i in result :
#     print(i,end=' ')