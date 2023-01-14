import sys
from collections import Counter
from functools import reduce
input = sys.stdin.readline

n,m,k = map(int, input().split())
n = n - 1
m = m - 1  #여기

board = [list(map(int, input().split())) for _ in range(3)]

def solve(arr) :
    
    maxCount = 0
    
    for i in range(len(arr)) :
        #print(arr[i])
        A = [ j for j in arr[i] if j != 0]
        A = Counter(A).most_common()
        A = sorted(A, key = lambda x : (x[1], x[0]))
        #print(A)    
        
        
        A = sorted(A, key = lambda x : (x[1], x[0]))
        if len(A) > 50 :
            A = A[:50]
        
        arr[i] = reduce(lambda x, y : list(x) + list(y), A[1:], list(A[0]))
        maxCount = max(maxCount, len(arr[i]))
    #print(maxCount)
    
    for i in range(len(arr)) :
        if len(arr[i]) < maxCount :
            arr[i].extend([0] * (maxCount - len(arr[i])))
    
    #print(arr)
    

for i in range(101) :
    try :
        if board[n][m] == k :
            print(i)
            break
    except : pass
    
    if len(board) >= len(board[0]) :
        solve(board)
    else :
        board = list(map(list, zip(*board)))
        solve(board)
        board = list(map(list, zip(*board)))
else :
    print(-1)


# 원래 밑에 코드 처럼 코드의 순서를 if로 출발하려 했더니 계속 실패함!
          
# if n < len(board) and m < len(board[0]) :
#     if board[n][m] == k :
#         print(0)
        
#     else : 
#         time = 0
#         while True :
            
#             if len(board) >= len(board[0]) :
#                 solve(board)
#             else :
#                 board = list(map(list, zip(*board)))
#                 solve(board)
#                 board = list(map(list, zip(*board)))
            
#             time += 1            
                
#             if time > 100 :
#                 print(-1)
#                 break

            
#             if n < len(board) and m < len(board[0]) :
#                 if board[n][m] == k :
#                     print(time)
#                     break