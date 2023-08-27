import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
que = deque()
que.append([N, 0])
isTrue = False
while que :
    
    num, cnt = que.popleft()
    
    if num == M :
        print(cnt+1)
        isTrue = True
        break

    if num < M :
        nx = num * 2
        que.append([nx, cnt+1])
        nx = int(str(num)+'1')
        que.append([nx, cnt+1])
        
if not isTrue :
    print(-1)


# ===============================================> 메모리초과(board,visited에서 M의 입력값이 10^9임)
# import sys
# from collections import deque
# input = sys.stdin.readline

# N, M = map(int, input().split())

# board = [ 0 for _ in range(M+1)]                                         
# visited = [False for _ in range(M+1)]

# def bfs(start) :
#     que = deque()
#     que.append(start)
#     visited[start] = True
    
#     while que :
#         x = que.popleft()
        
        
#         # X2
#         nx = x*2
#         if nx < M+1 and not visited[nx] :
#             board[nx] = board[x] + 1
#             visited[nx] = True
#             que.append(nx)
        
#         # 끝에 1 붙이기
#         temp = str(x) + '1'
#         nx = int(temp)
#         if nx < M+1 and not visited[nx] :
#             board[nx] = board[x] + 1
#             visited[nx] = True
#             que.append(nx)

# bfs(N)
# if board[M] == 0 :
#     print(-1)
# else :    
#     print(board[M] + 1)
 
# x = 123
# y = str(x) + '1'
# print(y)       