# import sys

# N = int(sys.stdin.readline())
# stack = []
# result = []

# for i in range(N) :  
#     x = list(sys.stdin.readline())
#     if x[0] == ')' :
#         result.append("NO")
#         break
#     for j in range(len(x)) :
#         while stack :
#             if stack[-1] == '(' and x[j] == ')' :
#                 stack.pop()
#                 break
        
#             elif x[j] == '(' :
#                 stack.append(x[j])
#                 break

#             elif x[j] == ')' :
#                 break
       
#         if len(x) % 2 != 0 and x[j] == ')':
#             stack.append(x[j])
#         elif not stack and x[j] == ')' :
#             continue
#         elif not stack :
#             stack.append(x[j])
#     if len(stack) == 0 :
#         result.append("YES")
#         stack.clear() 
#     else : 
#         result.append("NO")
#         stack.clear()

# [print(i) for i in result]
        
import sys

N = int(sys.stdin.readline())
result = []

for i in range (N) :
    stack = []
    list1 = list(sys.stdin.readline())

    for j in list1 :
        if j == '(' :
            stack.append(j)
        elif stack :
            if stack[-1] == '(' and j == ')' :
                stack.pop()
                continue
        if not stack and j == ')' :
            stack.append(j)
            break
        
    if len(stack) == 0 :
        result.append("YES")
    else :
        result.append("NO")

[print(i) for i in result]        
