import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for i in range(1,N+1) :
    dic[i] = set()    

for _ in range(M) :
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)
    
def bfs(start, target) :
    cnt = 1
    que = deque()
    que.append(start)
    visited[start] = True
    
    while que :
        x = que.popleft()
        
        for i in dic[x] :
            #print('i : '+str(i)+'  x :'+str(x))
            if i == target :
                dist[i] = dist[x] + 1
                return dist[i]
            
            if not visited[i] :
                visited[i] = True
                que.append(i)
                dist[i] = dist[x] + 1
                
result = []
for i in range(1, N+1) :
    temp = 0
    for j in range(1, N+1) :
        if i != j :
            visited = [False] * (N+1)
            dist = [0] * (N+1)
            #i는 출발, j는 타겟
            temp += bfs(i,j)
    result.append([i, temp])
    
result = sorted(result, key=lambda x : (x[1],x[0]))

print(result[0][0])