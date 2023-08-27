import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dic = {}
for i in range(1, N+1) :
    dic[i] = set()

for _ in range(N-1) :
    a, b = map(int, input().split())
    
    dic[a].add(b)
    dic[b].add(a)

result = [0 for _ in range(N+1)]

print(dic)
def bfs(start, dic) :
    
    que = deque()
    que.append(start)
    
    while que :
        
        x = que.popleft()
        
        for i in dic[x] :
            
            if not result[i] :
                que.append(i)
                result[i] = x

bfs(1,dic)

for i in range(2,N+1) :
    print(result[i])