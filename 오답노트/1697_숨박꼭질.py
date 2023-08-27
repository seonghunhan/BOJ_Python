import sys
from collections import deque
input = sys.stdin.readline




def bfs(x) :
    que = deque()
    que.append(x)
    
    while que :
        x = que.popleft()
        
        for i in (x+1, x-1, 2*x) :
            
            if 0 <= i <= 100000 and not dist[i]:
                dist[i] = x + 1
                que.append(i)     
    
    
N, K = map(int, input().split())
dist = [0] * 100001
bfs(N)
print(dist[K])