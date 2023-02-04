import sys
from collections import deque
input = sys.stdin.readline


T = int(input())


for _ in range(T) :
    
    start, target = map(int, input().split())
    visited = [0] * 10001
    visited[start] = 1
    que = deque()
    que.append([start,''])

    
    while que :
        
        num, path = que.popleft()
        
        # 타겟도착!
        if num == target :
            print(path)
            #print(que)
            break
        
        # D
        newNum = (num * 2) % 10000
        if not visited[newNum] :
            visited[newNum] = 1
            que.append([newNum, path+'D'])
        # S
        newNum = (num - 1) % 10000
        if not visited[newNum] :
            visited[newNum] = 1
            que.append([newNum, path+'S'])
        # L
        newNum = (num % 1000)*10 + (num // 1000)
        if not visited[newNum] :
            visited[newNum] = 1
            que.append([newNum, path+'L'])
        # R
        newNum = (num % 10)*1000 + (num // 10)
        if not visited[newNum] :
            visited[newNum] = 1
            que.append([newNum, path+'R'])    
    
    