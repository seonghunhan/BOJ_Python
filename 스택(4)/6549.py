
from contextlib import nullcontext
from logging import NullHandler

import sys

# h_list = []
# stack = []
# result = []
# area = []


# while len(h_list) == 1 and h_list[0] == 0 :
    
    
#     h_list = list(map(int, sys.stdin.readline().split()))
#     N = h_list[0]
    

#     for i in range (1,N) :
#         h = h_list[i]

#         if not stack :
#             stack.append(h)

#         elif h < stack[-1] :
#             area.append((h * (len(stack)+1)))

#         elif h > stack[-1] and h > area[-1] :
#             area.pop()
#             area.append()

n, *heights = list(map(int, sys.stdin.readline().split()))

print(n)
print(heights)


