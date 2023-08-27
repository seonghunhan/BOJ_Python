from collections import deque
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def bfs(A, B) :
    temp = 0
    que = deque()
    isTrue = True
    result = 0
    que.append([A,0])
    while que :
        
        nx, cnt = que.popleft()
        
        if nx <= B :
            if nx == B :
                result += cnt + 1
                break
            else :
                temp = nx * 2
                que.append([temp, cnt+1])
                temp = int(str(nx) + '1')
                que.append([temp, cnt+1])        
    
    if result != 0 :
        print(result)
    else :
        print(-1)
    
    return

bfs(A,B)